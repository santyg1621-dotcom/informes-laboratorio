# Laboratorio 4 - Programación dinámica (Caso 1: Tope tarifario)

**Nombre completo:** [santiago gomez montoya]
**Curso:** Análisis de Algoritmos

## 1. Análisis del problema
Básicamente, lo que hacemos acá es calcularle a cada usuario cuál es la forma más barata de pagar todos los viajes que hizo en el mes, para devolverle la diferencia a su tarjeta. 
- **Qué entra:** Una lista con los viajes que hizo por día en el mes.
- **Qué sale:** El costo mínimo .
- **La regla de oro:** La devolución tiene que ser exacta. No le podemos quitar un peso al usuario ni pagarle de más.
- **Un supuesto clave:** Asumimos que el mes tiene **30 días**, para que el pase mensual de 135.000 pesos cubra el mes completo.

## 2. Diseño de la solución
El problema pide a gritos **Programación Dinámica** porque tiene *subestructura óptima*: si yo compro un pase de 7 días, los días que quedan por pagar son un problema exactamente igual pero más pequeño. Además, hay *subproblemas traslapados*: para saber cuánto me cuesta desde el día 1, necesito saber cuánto cuesta desde el día 2, 3 o 8.

**El ejemplo a mano (con 4 días):**
Imagina que un usuario viaja así: `[3, 2, 2, 0]`. 
- **La regla actual (día a día):** Día 1 (3 viajes = 11.700, toca pase diario 9.500). Día 2 (2 viajes = 7.800). Día 3 (2 viajes = 7.800). Total = **25.100 pesos**.
- **La estrategia óptima:** Si compramos un pase semanal para esos días, nos cuesta **36.000**. ¿Es más caro? Sí. Pero si en vez de eso, miráramos los primeros 3 días juntos, resulta que la regla actual falló. 

**La recurrencia:**
Para un día `t`, el costo mínimo `C(t)` es el menor entre tres opciones:
1. Pagar solo el día de hoy (pasajes o pase diario) + lo que cueste desde `t+1`.
2. Comprar pase semanal (36.000) + lo que cueste desde `t+7`.
3. Comprar pase mensual (135.000) + lo que cueste desde `t+30`.
- *Caso base:* `C(31) = 0` (cuando se acaba el mes, no debes nada).
- *Orden:* Llenamos la tabla de atrás hacia adelante, desde el día 30 hasta el día 1.

## 3. Implementación
Todo el código está en la carpeta `tope_tarifario/`:
- [estrategia.py](tope_tarifario/estrategia.py) (La solución rápida con Programación Dinámica).
- [exhaustivo.py](tope_tarifario/exhaustivo.py) (La solución lenta que prueba todo, para verificar que la rápida no falle).
- [regla_actual.py](tope_tarifario/regla_actual.py) (La regla que usa hoy la empresa).
- [pruebas.py](tope_tarifario/pruebas.py) (Los `assert` para validar todo).

## 4. Evaluación del desempeño
- **Estrategia (PD):** Su complejidad es **Θ(d)** en tiempo y espacio. Se demora milisegundos.
- **Exhaustiva:** Es **exponencial**. Crece tan rápido que para 25 días ya tarda una eternidad.
- **Lo que dicen las gráficas:** En la primera gráfica se ve clarísimo cómo la línea roja (exhaustiva) se dispara hacia arriba, mientras que la estrategia (azul) se mantiene plana. En la segunda (operaciones), la exhaustiva llega a los miles de millones de operaciones, mientras que nuestra estrategia solo da unos cuantos pasos. ¡Es la noche y el día!

![Tiempo vs N](graficas/tiempo_vs_n.png)
![Operaciones vs N](graficas/operaciones_vs_n.png)

## 5. Análisis comparativo (El contraejemplo)
La regla actual falla porque **es corta de vista**: decide día por día sin mirar el panorama completo. 
**El contraejemplo calculado:** Un usuario con viajes `[2, 3, 3, 0, 1, 0, 2]` (7 días).
- **Lo que cobra la regla actual hoy:** Día 1 (2 viajes = 7.800) + Día 2 (pase diario = 9.500) + Día 3 (pase diario = 9.500) + Día 5 (1 viaje = 3.900) + Día 7 (2 viajes = 7.800). Total = **38.500 pesos**.
- **Lo que cobra la Estrategia (el mínimo real):** Compra un **pase semanal** (36.000) que cubre los primeros 7 días y ya. Total = **36.000 pesos**.
- **Diferencia:** ¡Le estamos cobrando **2.500 pesos de más** al usuario con la regla actual!

**La condición contraria:** Si el sistema no tuviera pases de varios días (ni semanal ni mensual), la regla actual sí sería perfecta, porque las decisiones de un día no afectarían a los otros. Pero como los pases existen, necesitamos la PD.

## 6. Implicaciones ambientales y energía
*(Para el volumen real de 950.000 tarjetas en un servidor de 500W)*
Para el volumen real, la regla actual y nuestra estrategia demoran prácticamente lo mismo (ambas son Θ(d), es decir, súper rápidas). Entonces, ¿dónde está el ahorro? En que la estrategia **no genera devoluciones erróneas**. Al ser exacta, evita que el sistema tenga que procesar reclamos, quejas y ajustes manuales al mes siguiente. La mejora no está en el tiempo de cómputo (que ya es mínimo), sino en la **exactitud financiera** y en la satisfacción de los usuarios.

## 7. Cómo reproducir esto
1. Activar el entorno virtual: `..\..\venv\Scripts\activate`
2. Entrar a la carpeta: `cd tope_tarifario`
3. Correr las pruebas: `python pruebas.py`
4. Generar las gráficas: `python medicion.py`