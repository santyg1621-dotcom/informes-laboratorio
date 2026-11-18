"""Generador de instancias sinteticas (Caso 1)."""

import random

def generar_viajes_mes(dias: int, probabilidad_viaje: float = 0.7, semilla: int = 42) -> list[int]:
    """Genera una lista de viajes por dia para un mes.

    Args:
        dias: numero de dias del periodo.
        probabilidad_viaje: probabilidad de que un dia tenga al menos 1 viaje.
        semilla: semilla fija para reproducibilidad.

    Returns:
        Lista con los viajes diarios.
    """
    rng = random.Random(semilla)
    viajes = []
    for _ in range(dias):
        if rng.random() < probabilidad_viaje:
            # Entre 1 y 4 viajes por dia
            viajes.append(rng.randint(1, 4))
        else:
            viajes.append(0)
    return viajes