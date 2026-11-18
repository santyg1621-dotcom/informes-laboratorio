"""Medicion de estrategia, exhaustiva y regla actual (Caso 1)."""

import time
import os
import matplotlib.pyplot as plt
from estrategia import costo_minimo
from exhaustivo import costo_exhaustivo
from regla_actual import costo_regla_actual
from datos import generar_viajes_mes

# Asegurarnos de que la carpeta de graficas exista usando ruta absoluta
CARPETA_GRAFICAS = os.path.join(os.path.dirname(os.path.dirname(__file__)), "graficas")
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

def experimento_tiempos():
    # Tamaños para la exhaustiva (no puede ser muy grande porque es exponencial)
    tamanos_exhaustiva = [5, 10, 15, 20, 25]
    
    # Tamaños grandes solo para la estrategia y la regla actual
    tamanos_grandes = [30, 60, 90, 120, 150, 180]

    tiempos_est = []
    tiempos_exh = []
    tiempos_regla = []

    print("Midiendo exhaustiva y estrategia...")
    for n in tamanos_exhaustiva:
        viajes = generar_viajes_mes(n, probabilidad_viaje=0.8, semilla=42)
        
        # Tiempo Estrategia
        inicio = time.perf_counter()
        costo_minimo(viajes)
        t_est = time.perf_counter() - inicio
        tiempos_est.append(t_est)

        # Tiempo Exhaustiva
        inicio = time.perf_counter()
        costo_exhaustivo(viajes)
        t_exh = time.perf_counter() - inicio
        tiempos_exh.append(t_exh)

        # Tiempo Regla Actual
        inicio = time.perf_counter()
        costo_regla_actual(viajes)
        t_regla = time.perf_counter() - inicio
        tiempos_regla.append(t_regla)

    # Extrapolación de la estrategia para tamaños grandes
    for n in tamanos_grandes:
        viajes = generar_viajes_mes(n, probabilidad_viaje=0.8, semilla=42)
        
        inicio = time.perf_counter()
        costo_minimo(viajes)
        tiempos_est.append(time.perf_counter() - inicio)

        # La regla actual también se mide en tamaños grandes
        inicio = time.perf_counter()
        costo_regla_actual(viajes)
        tiempos_regla.append(time.perf_counter() - inicio)

    # Graficar Tiempo
    plt.figure()
    # Para la exhaustiva solo graficamos los tamaños donde corrió
    plt.plot(tamanos_exhaustiva, tiempos_exh, label="Exhaustiva (Exponencial)", marker='o', color='red')
    
    # Estrategia y Regla actual se grafican con todos los tamaños
    todos_los_tamanos = tamanos_exhaustiva + tamanos_grandes
    plt.plot(todos_los_tamanos, tiempos_est, label="Estrategia (PD Θ(d))", marker='s', color='blue')
    plt.plot(todos_los_tamanos, tiempos_regla, label="Regla Actual Θ(d)", marker='^', color='orange')

    plt.xlabel("Número de días (d)")
    plt.ylabel("Tiempo de ejecución (segundos)")
    plt.title("Tiempo: Exhaustiva vs Estrategia vs Regla Actual")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # CORREGIDO AQUÍ: Usando la ruta absoluta
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "tiempo_vs_n.png"))
    print("Gráfica tiempo_vs_n.png generada.")

    # Para la gráfica de operaciones vs n
    plt.figure()
    plt.plot(tamanos_exhaustiva, [3**n for n in tamanos_exhaustiva], label="Exhaustiva O(3^d)", marker='o', color='red')
    plt.plot(todos_los_tamanos, [3*n for n in todos_los_tamanos], label="Estrategia y Regla O(d)", marker='s', color='blue')
    plt.yscale('log') # Escala logarítmica porque la diferencia es abismal
    plt.xlabel("Número de días (d)")
    plt.ylabel("Operaciones estimadas")
    plt.title("Operaciones: Exhaustiva vs Estrategia")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # CORREGIDO AQUÍ: Usando la ruta absoluta
    plt.savefig(os.path.join(CARPETA_GRAFICAS, "operaciones_vs_n.png"))
    print("Gráfica operaciones_vs_n.png generada.")


if __name__ == "__main__":
    experimento_tiempos()