"""Regla actual simplificada de la organizacion (Caso 1)."""

from estrategia import costo_minimo

PASAJE: int = 3900
DIARIO: int = 9500
SEMANAL: int = 36000
MENSUAL: int = 135000

def costo_regla_actual(viajes_por_dia: list[int]) -> int:
    """Calcula lo que cobra hoy la regla simplificada del sistema.

    La regla cobra por dia lo mas barato entre pasajes y pase diario.
    Si la suma acumulada supera el pase semanal o mensual, se aplica ese pase.

    Args:
        viajes_por_dia: viajes de la tarjeta en cada dia del mes.

    Returns:
        El costo cobrado en pesos.
    """
    total = 0
    for viajes in viajes_por_dia:
        if viajes == 0:
            continue
        sueltos = viajes * PASAJE
        total += min(sueltos, DIARIO)

    # Aplicar topes de pase semanal y mensual si la suma ya lo supera
    if total > MENSUAL:
        return MENSUAL
    elif total > SEMANAL:
        return SEMANAL

    return total


def liquidar_tope(viajes_por_dia: list[int], cobrado: int) -> int:
    """Calcula la devolucion que corresponde al usuario.

    Args:
        viajes_por_dia: viajes de la tarjeta en cada dia del mes.
        cobrado: pesos que se le cobraron durante el mes.

    Returns:
        La diferencia entre lo cobrado y el costo minimo, nunca negativa.
    """
    minimo = costo_minimo(viajes_por_dia)
    return max(0, cobrado - minimo)