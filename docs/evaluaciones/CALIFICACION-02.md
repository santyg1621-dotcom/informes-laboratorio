# Retroalimentación — Laboratorio 2: Dividir y vencer

**Estudiante:** Santiago Gómez Montoya · **Laboratorio:** Laboratorio evaluativo 02 — Dividir y vencer
**Fecha límite:** 2026-10-21 23:59 · **Versión revisada:** commit `4d99684`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 15 / 20 |
| Calidad de la explicación teórica | 16 / 20 |
| Corrección de la implementación | 21 / 25 |
| Calidad del análisis de las gráficas | 15 / 25 |
| Documentación y organización del informe | 6 / 10 |
| **Total** | **73 / 100** |
| **Nota (0–5)** | **3.65** |

## 1. Corrección conceptual (15 / 20)
**Lo que hizo bien:**
- En la pregunta 4 compara bien con el máximo de un arreglo: la recurrencia `T(n) = 2T(n/2) + Θ(1)` da `Θ(n)`, igual que recorrerlo una vez.
- Recomienda divide y vencerás y declara que la cifra de 1.000.000 es una estimación. Para la fuerza bruta usa el crecimiento al cuadrado y no una regla de tres.

**Lo que puede mejorar:**
- En la pregunta 3 dice que divide y vencerás gana desde n = 10, pero no muestra ningún valor medido que lo respalde.
- Para divide y vencerás solo dice "menos de un minuto" sin explicar cómo llegó a esa cifra. Haga el cálculo con `n log n` como lo hizo con `n²`.

## 2. Calidad de la explicación teórica (16 / 20)
**Lo que hizo bien:**
- Plantea `T(n) = 2T(n/2) + Θ(n)` y explica de dónde sale cada término.
- Aplica el método maestro (a = 2, b = 2, caso 2) y justifica el `Θ(n²)` de la fuerza bruta con la suma `n(n+1)/2`.

**Lo que puede mejorar:**
- Al verificar la condición del caso 2, diga explícitamente que `f(n) = Θ(n^(log_b a))` y de ahí concluya `Θ(n log n)`.

## 3. Corrección de la implementación (21 / 25)
**Lo que hizo bien:**
- Las tres funciones dan la suma correcta en todos los casos pedidos, no modifican la lista y `subarreglo_maximo` resuelve los tres casos sin usar la fuerza bruta.
- `pruebas.py` cubre todos los casos pedidos y las 20 listas aleatorias.

**Lo que puede mejorar:**
- En `medicion.py`, `medir_tiempo` no tiene tipos en el parámetro de la función y `ejecutar_experimento` no tiene tipo de retorno ni explicación (*docstring*) estilo Google.

## 4. Calidad del análisis de las gráficas (15 / 25)
**Lo que hizo bien:**
- La gráfica tiene título, ejes rotulados, leyenda y ambas curvas en los mismos ejes, con siete tamaños.
- Calcula el factor de crecimiento de la fuerza bruta de 4000 a 8000 (cerca de 4) y lo relaciona con `Θ(n²)`.

**Lo que puede mejorar:**
- No calcula el factor de crecimiento de divide y vencerás, así que falta compararlo con `Θ(n log n)`.
- El informe dice que la fuerza bruta pasa de unos 0.6 s a 2.6 s; en la gráfica se leen cerca de 0.67 s y 2.7 s. Apóyese en los valores que lee de la gráfica.
- Dice que repitió cada medición, pero el código mide una sola vez cada tamaño. El informe debe describir lo que realmente hizo.

## 5. Documentación y organización del informe (6 / 10)
**Lo que hizo bien:**
- Carpeta `lab2-divide-y-vencer/` en el lugar acordado, con todos los archivos pedidos.
- El informe sigue el orden pedido, la gráfica se ve y los enlaces al código funcionan.

**Lo que puede mejorar:**
- El laboratorio se subió en un solo commit; se pedían al menos tres commits descriptivos.
- Las instrucciones para activar el entorno usan una ruta de Windows y no es claro desde dónde se ejecutan.
- Se subió la carpeta `__pycache__/`; conviene agregarla a un `.gitignore`.

## ¿El código funciona?
Sí. Las pruebas pasan, ambos algoritmos coinciden en listas aleatorias y `medicion.py` corre y genera la gráfica sin errores.

## Para el próximo laboratorio
- Respalde cada afirmación con un valor medido (por ejemplo, con una tabla de tiempos).
- Calcule el factor de crecimiento de los dos algoritmos, no solo de uno.
- Haga commits pequeños y descriptivos a medida que avanza.
- Complete los tipos y *docstrings* de todas las funciones.
- Describa en el informe exactamente cómo midió.
