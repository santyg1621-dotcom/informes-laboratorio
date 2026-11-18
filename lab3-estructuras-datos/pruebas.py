"""Pruebas para verificar lista enlazada y tabla hash."""

import random
from estructuras import ListaEnlazada, TablaHash


def probar_todo():
    # 1. Búsqueda exitosa e infructuosa en lista
    lista = ListaEnlazada()
    lista.insertar(1000000010, "en bodega")
    assert lista.buscar(1000000010) == "en bodega"
    assert lista.buscar(9999999999) is None

    # 2. Búsqueda exitosa e infructuosa en tabla
    tabla = TablaHash(7)
    tabla.insertar(1000000010, "en bodega")
    assert tabla.buscar(1000000010) == "en bodega"
    assert tabla.buscar(9999999999) is None

    # 3. Colisión forzada con m=7: 10, 24 y 17 caen en casilla 3
    tabla_colision = TablaHash(7)
    for guia in (10, 24, 17):
        tabla_colision.insertar(guia, "en bodega")
    assert tabla_colision.buscar(10) == "en bodega"
    assert tabla_colision.buscar(24) == "en bodega"
    assert tabla_colision.buscar(17) == "en bodega"
    assert tabla_colision.casillas[3].tamano == 3

    # 4. Factor de carga
    assert abs(tabla_colision.factor_carga() - 3 / 7) < 1e-9

    # 5. 20 colecciones aleatorias
    random.seed(42)
    for _ in range(20):
        n = random.randint(1, 50)
        lista_rand = ListaEnlazada()
        tabla_rand = TablaHash(13)
        guias = [random.randint(10**9, 10**10 - 1) for _ in range(n)]
        for guia in guias:
            lista_rand.insertar(guia, "ok")
            tabla_rand.insertar(guia, "ok")

        for guia in guias:
            assert lista_rand.buscar(guia) == tabla_rand.buscar(guia)

        # Una guía que no existe
        assert lista_rand.buscar(1) == tabla_rand.buscar(1)

    print("¡Todas las pruebas pasaron exitosamente!")


if __name__ == "__main__":
    probar_todo()