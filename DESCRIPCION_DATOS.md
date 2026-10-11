# Descripción de los datos

## Fuente
Dataset de **muestra sintético** (`datos/demanda_transmilenio.csv`), generado con `generar_datos.py`.
Se creó porque la actividad permite desarrollar una muestra cuando no hay una fuente utilizable. Imita el comportamiento
real del sistema TransMilenio (Bogotá): más pasajeros en horas pico (6-8 am y 5-7 pm), menos en fines de semana y festivos,
y estaciones grandes (portales) con más demanda.

**Fuentes reales recomendadas para una versión futura:** datos abiertos de Bogotá (datos.bogota.gov.co) y de TransMilenio
(validaciones de entrada por estación) y datos.gov.co.

## Tamaño
- 52.704 filas, 9 columnas, sin valores vacíos.
- Periodo: 01-ene-2024 a 31-ago-2024. 12 estaciones. Horas de 5 am a 10 pm.

## Columnas

| Columna | Tipo | Descripción |
|---|---|---|
| fecha | fecha | Día de la observación |
| hora | entero (5-22) | Hora del día |
| dia_semana | entero (0-6) | 0 = lunes ... 6 = domingo |
| es_festivo | 0/1 | 1 si es día festivo |
| llueve | 0/1 | 1 si llovió ese día |
| estacion | texto | Nombre de la estación |
| troncal | texto | Troncal a la que pertenece |
| pasajeros | entero | Pasajeros que entran en esa hora (solo informativo) |
| **nivel_demanda** | texto | **Variable a predecir**: baja (<600), media (600-1399), alta (≥1400) |

## Nota importante
`pasajeros` **no** se usa como entrada del modelo, porque de ella se calcula `nivel_demanda` (sería una trampa / fuga de información).

## Distribución de la etiqueta
- media: 21.334 (40,5 %)
- baja: 19.393 (36,8 %)
- alta: 11.977 (22,7 %)
