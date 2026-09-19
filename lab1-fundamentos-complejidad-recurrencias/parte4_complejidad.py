"""Experimento de la Parte 4: comparación de Merge Sort vs Insertion Sort en escenario A."""

import time
import os
import matplotlib.pyplot as plt
from datos import generar_aleatorio
from algoritmos import insertion_sort, merge_sort

os.makedirs("graficas", exist_ok=True)

TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]


def ejecutar_experimento():
    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMANOS:
        print(f"Midiendo tamaño {n}...")
        datos = generar_aleatorio(n)

        start = time.perf_counter()
        insertion_sort(datos)
        tiempos_insertion.append(time.perf_counter() - start)

        start = time.perf_counter()
        merge_sort(datos)
        tiempos_merge.append(time.perf_counter() - start)

    plt.figure()
    plt.plot(TAMANOS, tiempos_insertion, label="Insertion Sort")
    plt.plot(TAMANOS, tiempos_merge, label="Merge Sort")
    plt.xlabel("Tamaño de entrada (n)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo de ejecución: Insertion Sort vs Merge Sort (Escenario A)")
    plt.legend()
    plt.savefig("graficas/parte4_tiempo.png")
    print("¡Gráfica de la Parte 4 generada!")


if __name__ == "__main__":
    ejecutar_experimento()