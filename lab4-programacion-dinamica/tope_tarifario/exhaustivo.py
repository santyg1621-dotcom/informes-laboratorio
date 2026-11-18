"""Solucion exhaustiva para verificar la estrategia (Caso 1)."""

from estrategia import PASAJE, DIARIO, PASES


def costo_exhaustivo(viajes_por_dia: list[int], t: int = 1) -> int:
    """Calcula el mismo costo probando todas las combinaciones de productos.

    Args:
        viajes_por_dia: viajes de la tarjeta en cada dia del mes.
        t: Primer dia que todavia no esta pagado (1-indexado).

    Returns:
        El costo minimo en pesos.
    """
    d = len(viajes_por_dia)
    if t > d:
        return 0  # Caso base: no quedan dias

    if viajes_por_dia[t - 1] == 0:
        return costo_exhaustivo(viajes_por_dia, t + 1)  # Dia sin viajes

    # Opcion (a): pagar solo hoy
    sueltos = viajes_por_dia[t - 1] * PASAJE
    hoy = min(sueltos, DIARIO)
    mejor = hoy + costo_exhaustivo(viajes_por_dia, t + 1)

    # Opciones (b) y (c): pases de varios dias
    for _, precio, dias in PASES:
        candidato = precio + costo_exhaustivo(viajes_por_dia, t + dias)
        if candidato < mejor:
            mejor = candidato

    return mejor