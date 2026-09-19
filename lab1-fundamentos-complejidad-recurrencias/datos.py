"""Generadores de lotes de registros para los escenarios de Tamiza."""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A)."""
    rng = random.Random(semilla)
    return [rng.randint(0, 1000) for _ in range(n)]


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B)."""
    rng = random.Random(semilla)
    cantidad_ordenada = int(n * 0.98)
    parte_ordenada = sorted(rng.randint(0, 1000) for _ in range(cantidad_ordenada))
    cantidad_desordenada = n - cantidad_ordenada
    parte_desordenada = [rng.randint(0, 1000) for _ in range(cantidad_desordenada)]
    return parte_ordenada + parte_desordenada


def generar_inverso(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote en orden inverso al que el algoritmo produce (escenario C)."""
    rng = random.Random(semilla)
    return sorted(rng.randint(0, 1000) for _ in range(n))