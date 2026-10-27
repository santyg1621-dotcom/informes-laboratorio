"""Medicion de lista enlazada vs tabla hash."""

import time
import os
import random
import matplotlib.pyplot as plt
from estructuras import ListaEnlazada, TablaHash

os.makedirs("graficas", exist_ok=True)


def generar_guias_inexistentes(existentes: set[int], cantidad: int, semilla: int = 7) -> list[int]:
    """Genera guias de diez digitos que no estan en la coleccion."""
    azar = random.Random(semilla)
    inexistentes = []
    while len(inexistentes) < cantidad:
        guia = azar.randint(10**9, 10**10 - 1)
        if guia not in existentes:
            inexistentes.append(guia)
    return inexistentes


def es_primo(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def primo_cercano(n: int) -> int:
    if n % 2 == 0:
        n -= 1
    while n > 2:
        if es_primo(n):
            return n
        n -= 2
    return 2


def experimento_a():
    tamanos = [100, 500, 1000, 5000, 20000, 50000]
    tiempos_lista = []
    tiempos_tabla = []

    for n in tamanos:
        print(f"Experimento A: n={n}...")
        rng = random.Random(42)
        guias = [rng.randint(10**9, 10**10 - 1) for _ in range(n)]
        existentes = set(guias)

        # Construir estructuras
        lista = ListaEnlazada()
        m = primo_cercano(max(1, n // 2))
        tabla = TablaHash(m)
        for guia in guias:
            lista.insertar(guia, "ok")
            tabla.insertar(guia, "ok")

        # Guías inexistentes
        inexistentes = generar_guias_inexistentes(existentes, 200)

        # Medir lista
        inicio = time.perf_counter()
        for guia in inexistentes:
            lista.buscar(guia)
        tiempos_lista.append((time.perf_counter() - inicio) / 200)

        # Medir tabla
        inicio = time.perf_counter()
        for guia in inexistentes:
            tabla.buscar(guia)
        tiempos_tabla.append((time.perf_counter() - inicio) / 200)

    plt.figure()
    plt.plot(tamanos, tiempos_lista, label="Lista Enlazada Θ(n)", marker='o')
    plt.plot(tamanos, tiempos_tabla, label="Tabla Hash Θ(1+α)", marker='s')
    plt.xlabel("Número de guías (n)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.title("Búsqueda de guía inexistente: Lista vs Tabla Hash")
    plt.legend()
    plt.savefig("graficas/lista_vs_tabla.png")
    print("¡Gráfica lista_vs_tabla generada!")


def experimento_b():
    n = 20000
    alfas = [0.5, 1, 4, 10]
    tiempos = []

    rng = random.Random(42)
    guias = [rng.randint(10**9, 10**10 - 1) for _ in range(n)]
    existentes = set(guias)
    inexistentes = generar_guias_inexistentes(existentes, 200)

    for alpha in alfas:
        m = primo_cercano(int(n / alpha))
        tabla = TablaHash(m)
        for guia in guias:
            tabla.insertar(guia, "ok")

        inicio = time.perf_counter()
        for guia in inexistentes:
            tabla.buscar(guia)
        tiempos.append((time.perf_counter() - inicio) / 200)

    plt.figure()
    plt.plot(alfas, tiempos, label="Tabla Hash", marker='o', color='green')
    plt.xlabel("Factor de carga (α = n/m)")
    plt.ylabel("Tiempo medio por búsqueda (segundos)")
    plt.title("Efecto del factor de carga en la búsqueda")
    plt.legend()
    plt.savefig("graficas/tiempo_vs_alfa.png")
    print("¡Gráfica tiempo_vs_alfa generada!")


if __name__ == "__main__":
    experimento_a()
    experimento_b()