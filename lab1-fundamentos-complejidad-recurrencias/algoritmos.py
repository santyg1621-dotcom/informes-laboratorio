"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1."""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista con el método de inserción. No modifica la lista recibida.
    
    Args:
        datos: Lista de índices de riesgo a ordenar.
    
    Returns:
        Una tupla con la lista ordenada y el número total de comparaciones entre elementos.
    """
    lista = datos.copy()
    comparaciones = 0
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] < clave:
            comparaciones += 1
            lista[j + 1] = lista[j]
            j -= 1
        if j >= 0:
            comparaciones += 1
        lista[j + 1] = clave
    return lista, comparaciones


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista con el método de mezcla. No modifica la lista recibida.
    
    Args:
        datos: Lista de índices de riesgo a ordenar.
    
    Returns:
        Una tupla con la lista ordenada y el número total de comparaciones entre elementos.
    """
    lista = datos.copy()

    def _merge_sort(arr: list[int]) -> tuple[list[int], int]:
        if len(arr) <= 1:
            return arr, 0
        medio = len(arr) // 2
        izquierda, comp_izq = _merge_sort(arr[:medio])
        derecha, comp_der = _merge_sort(arr[medio:])
        combinada, comp_comb = _merge(izquierda, derecha)
        return combinada, comp_izq + comp_der + comp_comb

    def _merge(izq: list[int], der: list[int]) -> tuple[list[int], int]:
        result = []
        i = j = 0
        comps = 0
        while i < len(izq) and j < len(der):
            comps += 1
            if izq[i] >= der[j]:
                result.append(izq[i])
                i += 1
            else:
                result.append(der[j])
                j += 1
        result.extend(izq[i:])
        result.extend(der[j:])
        return result, comps

    lista_ordenada, comparaciones = _merge_sort(lista)
    return lista_ordenada, comparaciones