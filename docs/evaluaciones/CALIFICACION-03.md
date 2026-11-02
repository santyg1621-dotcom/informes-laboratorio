# Retroalimentación — Laboratorio 03: Estructuras de datos

**Estudiante:** Santiago Stiven Gomez Montoya · **Laboratorio:** Laboratorio evaluativo 03 — Estructuras de datos
**Fecha límite:** 2026-11-01 23:59 · **Versión revisada:** commit `f9623d9`

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 18 / 20 |
| Calidad de la explicación teórica | 20 / 20 |
| Corrección de la implementación | 12 / 25 |
| Calidad del análisis de las gráficas | 21 / 25 |
| Documentación y organización del informe | 7 / 10 |
| **Total** | **78 / 100** |
| **Nota (0–5)** | **3.90** |

## 1. Corrección conceptual (18 / 20)
**Lo que hizo bien:**
- Explica bien qué es una colisión y por qué ocurre aunque sobren casillas, y usa el ejemplo de 10, 24 y 17 con m = 7.
- Compara encadenamiento y direccionamiento abierto con ventaja y costo de cada uno.
- Dice con claridad que la tabla hash no sirve para rangos y por qué.
- Declara que la cifra de 5.000.000 es una estimación.

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 4 dice que el árbol degenerado hace Θ(n) comparaciones, pero no estima el número aproximado de comparaciones al insertar las 400.000 guías una a una.
  → *Cómo corregirlo:* piense cuántos nodos hay que recorrer para colocar la guía número 1, la 2, la 3... y sume ese esfuerzo; compare con el mismo conteo en un árbol de altura cercana a 19.
- En la pregunta 5 estima el tiempo de la lista pero no da un número para la tabla; solo dice que sería "casi constante".
  → *Cómo corregirlo:* mire en su gráfica de α qué tiempo corresponde al α que usaría con 5.000.000 de envíos y explique por qué la forma de esa curva le permite estimar.
- La regla de tres para la lista se aplica sin explicar por qué la curva es una recta.
  → *Cómo corregirlo:* apóyese en lo que ve en su primera gráfica para justificar la forma antes de proyectar.

## 2. Calidad de la explicación teórica (20 / 20)
**Lo que hizo bien:**
- Justifica el Θ(n) de la lista y el Θ(1 + α) de la tabla, separando el costo de calcular el hash del costo de recorrer la casilla.
- Nombra el supuesto de hash uniforme y explica que, si todo cae en una casilla, la tabla se comporta como una lista.

## 3. Corrección de la implementación (12 / 25)
**Lo que hizo bien:**
- `ListaEnlazada` y `TablaHash` funcionan: las búsquedas exitosas e infructuosas dan el resultado correcto, la colisión con m = 7 queda en la casilla 3 con tres elementos y `factor_carga` da 3/7.
- La tabla reutiliza la lista y no usa `dict`, `set` ni `hash()`; `buscar` es iterativa.
- Lista y tabla coincidieron en colecciones aleatorias que probé por mi cuenta.
- `estructuras.py` tiene docstrings con `Args` y `Returns` y type hints.

**Lo que puede mejorar (y cómo corregirlo):**
- El archivo `pruebas.py` está vacío (0 bytes). No hay ninguna prueba con `assert`: ni búsquedas, ni la colisión forzada, ni el factor de carga, ni las veinte colecciones aleatorias. El README dice que las hizo, pero lo publicado no lo respalda.
  → *Cómo corregirlo:* escriba en `pruebas.py` los `assert` que describe en el README, cuide que el archivo quede guardado antes de hacer `git add`, y confirme en GitHub que el archivo tiene contenido.
- En `medicion.py`, `es_primo`, `primo_cercano`, `experimento_a` y `experimento_b` no tienen docstring ni type hints, y `generar_guias_inexistentes` no tiene las secciones `Args` y `Returns`.
  → *Cómo corregirlo:* agregue a cada función un docstring estilo Google con `Args` y `Returns` y anote tipos en parámetros y retorno (por ejemplo `-> None`).
- No hay dos líneas en blanco entre algunas funciones (el archivo no usa la separación completa en todos los casos) ni se verifica en la medición que lista y tabla devuelvan lo mismo para guías existentes.
  → *Cómo corregirlo:* dentro del experimento, tome una muestra de guías existentes y compare con `assert` los resultados de las dos estructuras antes de cronometrar.

## 4. Calidad del análisis de las gráficas (21 / 25)
**Lo que hizo bien:**
- Las dos gráficas existen, con título, ejes rotulados y leyenda; la primera tiene seis valores de n con ambas curvas en los mismos ejes y la segunda cuatro valores de α.
- Cronometra solo las búsquedas con `time.perf_counter()` y usa semilla fija.
- La descripción general coincide con lo que se ve: la lista sube casi en línea recta y la tabla queda pegada al eje.
- Lee en la segunda gráfica valores aproximados (de cerca de 0.45 a cerca de 1.25 microsegundos) y los relaciona con Θ(1 + α).

**Lo que puede mejorar (y cómo corregirlo):**
- En la pregunta 2 dice que de n = 20.000 a 50.000 el tiempo de la lista se multiplica "cerca de 2.5", pero no muestra los dos tiempos ni la división. En la gráfica publicada la lista pasa de aproximadamente 0.0021 s a 0.0049 s.
  → *Cómo corregirlo:* lea los dos valores en la gráfica, divídalos y compare ese resultado con el factor en que creció n.
- En la segunda gráfica el tiempo baja un poco de α = 0.5 a α = 1, y no lo comenta; tampoco calcula cuánto crece el tiempo cuando α se multiplica.
  → *Cómo corregirlo:* mencione ese comportamiento y proponga una razón posible (por ejemplo, el ruido al medir microsegundos); calcule el cociente entre dos valores de α y el cociente de tiempos.

## 5. Documentación y organización del informe (7 / 10)
**Lo que hizo bien:**
- La carpeta `lab3-estructuras-datos/` está en la raíz del repositorio con los archivos pedidos.
- El README sigue el orden pedido, las imágenes se incrustan con ruta relativa que funciona y cada parte práctica enlaza su código.
- Incluye instrucciones de reproducción y las notas de medición (valores de n, α y semilla).

**Lo que puede mejorar (y cómo corregirlo):**
- Solo hay un commit del laboratorio ("Laboratorio 3 completo"); se piden al menos tres commits descriptivos.
  → *Cómo corregirlo:* haga un commit por cada avance (estructuras, pruebas, medición, informe) con un mensaje que diga qué cambió.
- La ruta para activar el entorno virtual (`..\..\venv\Scripts\activate`) no corresponde con la estructura del repositorio ni sirve en Mac o Linux.
  → *Cómo corregirlo:* escriba la ruta real del entorno respecto a la raíz de su repositorio e indique también el comando para otros sistemas.
- Se subió la carpeta `__pycache__/` al repositorio; no descuenta puntos, pero conviene agregarla a `.gitignore`.
  → *Cómo corregirlo:* agregue la línea `__pycache__/` a `.gitignore`.

## ¿El código funciona?
Las estructuras de `estructuras.py` funcionan bien y `medicion.py` se ejecuta y genera las gráficas. Sin embargo, `pruebas.py` está vacío, así que las pruebas que describe el informe no existen.
