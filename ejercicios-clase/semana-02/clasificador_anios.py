"""Clasificador de años bisiestos (Parte 4)."""

def es_bisiesto(anio: int) -> bool:
    """Determina si un año es bisiesto según las reglas dadas."""
    if anio % 400 == 0:
        return True
    elif anio % 100 == 0:
        return False
    elif anio % 4 == 0:
        return True
    else:
        return False

def contar_bisiestos(anios: list[int]) -> int:
    """Cuenta la cantidad de años bisiestos en una lista (sin bucles for)."""
    return sum(1 for anio in anios if es_bisiesto(anio))

def listar_bisiestos(anios: list[int]) -> list[int]:
    """Devuelve una lista con solo los años bisiestos."""
    return [anio for anio in anios if es_bisiesto(anio)]

if __name__ == "__main__":
    # Ejemplo de prueba
    años = [2000, 1900, 2024, 2023, 2025, 2028]
    print(es_bisiesto(2000))
    print(contar_bisiestos(años))
    print(listar_bisiestos(años))