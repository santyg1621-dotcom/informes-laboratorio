"""Experimento de la Parte 3: comparación de escenarios con insertion sort."""

import time
import os
import matplotlib.pyplot as plt
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso
from algoritmos import insertion_sort

os.makedirs("graficas", exist_ok=True)

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]

def ejecutar_experimento():
    resultados_comp = {"A": [], "B": [], "C": []}
    resultados_tiempo = {"A": [], "B": [], "C": []}

    for n in TAMANOS:
        print(f"Midiendo tamaño {n}...")
        
        datos_a = generar_aleatorio(n)
        start = time.perf_counter()
        _, comp_a = insertion_sort(datos_a)
        tiempo_a = time.perf_counter() - start
        resultados_comp["A"].append(comp_a)
        resultados_tiempo["A"].append(tiempo_a)

        datos_b = generar_casi_ordenado(n)
        start = time.perf_counter()
        _, comp_b = insertion_sort(datos_b)
        tiempo_b = time.perf_counter() - start
        resultados_comp["B"].append(comp_b)
        resultados_tiempo["B"].append(tiempo_b)

        datos_c = generar_inverso(n)
        start = time.perf_counter()
        _, comp_c = insertion_sort(datos_c)
        tiempo_c = time.perf_counter() - start
        resultados_comp["C"].append(comp_c)
        resultados_tiempo["C"].append(tiempo_c)

    plt.figure()
    plt.plot(TAMANOS, resultados_comp["A"], label="A - Aleatorio")
    plt.plot(TAMANOS, resultados_comp["B"], label="B - Casi ordenado")
    plt.plot(TAMANOS, resultados_comp["C"], label="C - Orden inverso")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Número de comparaciones")
    plt.title("Comparaciones de Insertion Sort vs Tamaño")
    plt.legend()
    plt.savefig("graficas/parte3_comparaciones.png")

    plt.figure()
    plt.plot(TAMANOS, resultados_tiempo["A"], label="A - Aleatorio")
    plt.plot(TAMANOS, resultados_tiempo["B"], label="B - Casi ordenado")
    plt.plot(TAMANOS, resultados_tiempo["C"], label="C - Orden inverso")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de Insertion Sort vs Tamaño")
    plt.legend()
    plt.savefig("graficas/parte3_tiempo.png")

    print("¡Gráficas de la Parte 3 generadas!")

if __name__ == "__main__":
    ejecutar_experimento()