"""Liquidacion del tope tarifario de una tarjeta (Caso 1).

Estrategia: programacion dinamica sobre los dias del mes.
"""

PASAJE: int = 3900
DIARIO: int = 9500
SEMANAL: int = 36000
MENSUAL: int = 135000

# (nombre, precio, dias que cubre)
PASES: list[tuple[str, int, int]] = [
    ("semanal", SEMANAL, 7),
    ("mensual", MENSUAL, 30),
]


def costo_minimo(viajes_por_dia: list[int]) -> int:
    """Calcula el costo de la combinacion mas barata que cubre los viajes.

    Args:
        viajes_por_dia: viajes de la tarjeta en cada dia del mes. El
            indice 0 es el primer dia; un dia sin viajes vale 0.

    Returns:
        El costo minimo en pesos.
    """
    d = len(viajes_por_dia)
    if d == 0:
        return 0

    # costo[t] = C(t): lo minimo para pagar del dia t al final.
    # Se indexa de 1 a d; costo[d + 1] = 0 es el caso base.
    costo = [0] * (d + 2)

    # Pregunta 5: se llena de atras hacia adelante.
    for t in range(d, 0, -1):
        if viajes_por_dia[t - 1] == 0:
            # Dia sin viajes: no se compra nada.
            costo[t] = costo[t + 1]
            continue

        # Opcion (a): pagar solo hoy, con pasajes o pase diario.
        sueltos = viajes_por_dia[t - 1] * PASAJE
        costo[t] = min(sueltos, DIARIO) + costo[t + 1]

        # Opciones (b) y (c): un pase que empieza hoy.
        for _, precio, dias in PASES:
            siguiente = min(t + dias, d + 1)
            candidato = precio + costo[siguiente]
            if candidato < costo[t]:
                costo[t] = candidato

    return costo[1]