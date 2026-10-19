"""Medicion de tiempo para fuerza bruta vs divide y venceras."""

import time
import os
import random
import matplotlib.pyplot as plt
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

os.makedirs("graficas", exist_ok=True)

TAMANOS = [10, 50, 100, 500, 1000, 4000, 8000]
SEMILLA = 42


def generar_datos(n: int) -> list[float]:
    """Genera una lista de n enteros aleatorios entre -100 y 100."""
    rng = random.Random(SEMILLA)
    return [rng.randint(-100, 100) for _ in range(n)]


def medir_tiempo(func, *args) -> float:
    """Mide el tiempo de ejecucion de una funcion."""
    inicio = time.perf_counter()
    func(*args)
    fin = time.perf_counter()
    return fin - inicio


def ejecutar_experimento():
    tiempos_fb = []
    tiempos_dv = []

    for n in TAMANOS:
        print(f"Midiendo tamaño {n}...")
        datos = generar_datos(n)

        # Medir fuerza bruta
        t_fb = medir_tiempo(subarreglo_fuerza_bruta, datos)
        tiempos_fb.append(t_fb)

        # Medir divide y vencerás
        t_dv = medir_tiempo(subarreglo_maximo, datos, 0, n - 1)
        tiempos_dv.append(t_dv)

        # Verificar que dan la misma suma
        suma_fb = subarreglo_fuerza_bruta(datos)[2]
        suma_dv = subarreglo_maximo(datos, 0, n - 1)[2]
        assert suma_fb == suma_dv, f"Error en n={n}: {suma_fb} != {suma_dv}"

    # Graficar
    plt.figure()
    plt.plot(TAMANOS, tiempos_fb, label="Fuerza Bruta Θ(n²)", marker='o')
    plt.plot(TAMANOS, tiempos_dv, label="Divide y Vencerás Θ(n log n)", marker='s')
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Subarreglo Máximo: Fuerza Bruta vs Divide y Vencerás")
    plt.legend()
    plt.savefig("graficas/tiempo_vs_n.png")
    print("¡Gráfica generada en graficas/tiempo_vs_n.png!")


if __name__ == "__main__":
    ejecutar_experimento()