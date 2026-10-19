"""Pruebas para verificar los algoritmos de subarreglo maximo."""

import random
from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def probar_todo():
    # 1. Serie de 8 dias de la guia (suma 17)
    serie = [-3, 5, -2, 8, -6, 3, 9, -4]
    assert subarreglo_fuerza_bruta(serie)[2] == 17
    assert subarreglo_maximo(serie, 0, len(serie) - 1)[2] == 17

    # 2. Un solo elemento
    serie_uno = [5]
    assert subarreglo_fuerza_bruta(serie_uno)[2] == 5
    assert subarreglo_maximo(serie_uno, 0, 0)[2] == 5

    # 3. Todos negativos
    serie_neg = [-5, -2, -8, -1, -4]
    assert subarreglo_fuerza_bruta(serie_neg)[2] == -1
    assert subarreglo_maximo(serie_neg, 0, len(serie_neg) - 1)[2] == -1

    # 4. Todos positivos
    serie_pos = [1, 2, 3, 4, 5]
    assert subarreglo_fuerza_bruta(serie_pos)[2] == 15
    assert subarreglo_maximo(serie_pos, 0, len(serie_pos) - 1)[2] == 15

    # 5. Caso cruzado
    serie_cruce = [1, -2, 3, 4, -1, 2, -5, 1]
    assert subarreglo_fuerza_bruta(serie_cruce)[2] == subarreglo_maximo(serie_cruce, 0, len(serie_cruce) - 1)[2]

    # 6. 20 listas aleatorias
    random.seed(42)
    for _ in range(20):
        n = random.randint(1, 50)
        serie_rand = [random.randint(-100, 100) for _ in range(n)]
        assert subarreglo_fuerza_bruta(serie_rand)[2] == subarreglo_maximo(serie_rand, 0, len(serie_rand) - 1)[2]

    print("¡Todas las pruebas pasaron exitosamente!")


if __name__ == "__main__":
    probar_todo()