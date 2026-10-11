# Pruebas realizadas

## Configuración
- Problema: clasificación del nivel de demanda (baja / media / alta).
- División de datos: 80 % entrenamiento (42.163 filas) y 20 % prueba (10.541 filas), con `random_state=42` y estratificada.
- Métricas: accuracy y F1 (promedio macro).
- Comando: `python modelo.py` (salida completa en `resultados/salida_consola.txt`).

## Prueba 1: comparación de modelos

| Modelo | Accuracy | F1 |
|---|---|---|
| Regresión logística (línea base) | 0,4875 | 0,4625 |
| Árbol de decisión (profundidad 6) | 0,8018 | 0,8030 |
| Random Forest (100 árboles) | 0,8854 | 0,8852 |

**Análisis:** la regresión logística rinde mal porque la relación entre hora y demanda no es lineal (la demanda sube en la mañana,
baja al mediodía y vuelve a subir en la tarde). El árbol de decisión captura esas reglas y llega a ~80 %. Random Forest, que combina
muchos árboles, es el mejor con ~88,5 %.

## Prueba 2: matriz de confusión del árbol de decisión
(filas = real, columnas = predicho; orden baja, media, alta)

|  | baja | media | alta |
|---|---|---|---|
| **baja** | 3544 | 327 | 8 |
| **media** | 883 | 2965 | 419 |
| **alta** | 0 | 452 | 1943 |

Los errores ocurren sobre todo entre clases vecinas (baja↔media, media↔alta). Casi nunca confunde "baja" con "alta"
(8 y 0 casos). Imagen: `resultados/matriz_confusion.png`.

## Prueba 3: variables más importantes (árbol)
1. hora (0,704)
2. dia_semana (0,099)
3. estación Portal Norte (0,050)
4. es_festivo (0,048)
5. troncal Sur (0,040)

Coincide con lo esperado: la hora es lo que más define la demanda. Árbol dibujado en `resultados/arbol_decision.png`.

## Prueba 4: caso nuevo
Entrada: lunes, 7 am, Portal Norte, sin lluvia. Resultado: **alta**, coherente con la hora pico de la mañana.

## Prueba 5: calidad de los datos
- 0 valores vacíos.
- Las tres clases están representadas (no hay desbalance extremo).

## Limitaciones
Los datos son sintéticos, por lo que los resultados muestran que el método funciona, pero no son la demanda real de Bogotá.
Con datos reales se espera menor exactitud y habría que añadir más variables (eventos, paros, clima por hora).
