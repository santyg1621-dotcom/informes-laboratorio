# Retroalimentación — Laboratorio 1: Fundamentos, complejidad y recurrencias

**Estudiante:** Santiago Stiven Gomez Montoya · **Laboratorio:** Laboratorio evaluativo 01 — Fundamentos, complejidad y recurrencias
**Fecha límite:** 2026-10-05 23:59 · **Versión revisada:** commit `0f26122`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 11 / 25 |
| Calidad de la explicación teórica | 7 / 25 |
| Corrección de la implementación | 12 / 20 |
| Calidad del análisis de las gráficas | 9 / 20 |
| Documentación y organización del informe | 4 / 10 |
| **Total** | **43 / 100** |
| **Nota (0–5)** | **2.15** |

## 1. Corrección conceptual (11 / 25)
**Lo que hizo bien:**
- Explica que la ventana de cuatro horas no se cumple y que un servidor más rápido no arregla el problema de fondo (el algoritmo O(n²)).
- Menciona el consumo de energía repetido todas las madrugadas.
- Reconoce que el orden de la lista decide a quién se llama primero.

**Lo que puede mejorar:**
- Diga de forma explícita la diferencia entre "da el resultado correcto" y "lo da a tiempo".
- El segundo ejemplo (aplicación de mapas) no dice cuántos datos hay ni qué límite se incumple.
- Falta un segundo perjuicio concreto y, en ambos, decir quién asume el costo (paciente, operador, Secretaría, equipo).

## 2. Calidad de la explicación teórica (7 / 25)
**Lo que hizo bien:**
- Escribió la predicción antes de medir y la dejó en el informe.
- Incluyó la tabla de complejidades de los dos algoritmos.

**Lo que puede mejorar:**
- No define peor caso, mejor caso y caso promedio (sobre qué entradas se toma el máximo, el mínimo o el promedio), ni dice cuál usaría para decidir si entra a producción.
- No plantea la recurrencia de merge sort (T(n) = 2T(n/2) + Θ(n)) ni la resuelve paso a paso con ningún método.
- Para insertion sort solo da una frase; falta el cálculo línea a línea.

## 3. Corrección de la implementación (12 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien (de mayor a menor), no cambian la lista recibida y cuentan comparaciones entre elementos. No usan `sorted()` en los algoritmos.
- Los generadores aceptan semilla.

**Lo que puede mejorar:**
- En `generar_casi_ordenado` y `generar_inverso` el orden queda al revés del que usan sus algoritmos: el "casi ordenado" no queda casi ordenado para ellos y se comporta como el peor caso. Por eso los resultados del escenario B no son los esperados.
- Los generadores usan números que se repiten (se pedían distintos) y usan `sorted()` para armar los lotes.
- `generar_inverso` agrega un parámetro que no estaba en la firma; los docstrings de `datos.py` no tienen `Args` ni `Returns`.
- Faltan líneas en blanco entre funciones (PEP 8).

## 4. Calidad del análisis de las gráficas (9 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, tienen título, ejes con nombre y leyenda, y se ven en el informe.
- La gráfica de la Parte 4 muestra claramente que insertion sort crece mucho más que merge sort, y la conclusión coincide con O(n²) frente a O(n log n).
- Recomienda merge sort y dice que cambiar el algoritmo vale más que el servidor.

**Lo que puede mejorar:**
- En la Parte 3 no dice con claridad cuál escenario es el peor, cuál el mejor y cuál se parece al promedio. Sus propios datos muestran A como el más barato y B casi igual a C; explique por qué (ver el punto del generador) en lugar de solo decir que le sorprendió.
- En 4.3 no cita ningún dato medido (gráfica y tamaño), ni estima si 1.200.000 registros caben en cuatro horas, ni discute otra consideración como memoria o estabilidad.
- No comenta qué pasa con tamaños pequeños en la gráfica de la Parte 4.

## 5. Documentación y organización del informe (4 / 10)
**Lo que hizo bien:**
- La carpeta del laboratorio está bien ubicada y tiene todos los archivos pedidos; el informe sigue el orden de las partes y las gráficas se ven.
- Incluye su nombre e instrucciones para reproducir.

**Lo que puede mejorar:**
- No enlaza el código (`algoritmos.py`, `datos.py`, `parte3_casos.py`, `parte4_complejidad.py`) en el informe.
- El laboratorio tiene un solo commit; se pedían al menos cinco que mostraran el avance.
- No siguió la estructura acordada: hay archivos `__pycache__` publicados dentro de la carpeta del laboratorio y carpetas ajenas en la raíz (`Laboratorio/`, `MEOW_ml/`, `ejemplos-tiem/`).
- La instrucción para activar el entorno usa una ruta de Windows y no es clara para otros sistemas.

## ¿El código funciona?
Sí. Los scripts corren sin errores, los algoritmos ordenan correctamente y se generan las tres gráficas.

## Para el próximo laboratorio
- Responda cada pregunta con todos los puntos que pide (definiciones, quién asume el costo, ejemplo con datos).
- Desarrolle las recurrencias paso a paso, no solo el resultado.
- Revise que los generadores sean coherentes con el sentido de orden que eligió.
- Cite datos medidos y declare las extrapolaciones como estimación.
- Haga commits frecuentes y enlace su código en el informe; no suba `__pycache__`.
