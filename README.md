# Predicción de demanda en TransMilenio con aprendizaje supervisado

Actividad 3 - Métodos de aprendizaje supervisado (Inteligencia Artificial).

## Estructura
- `generar_datos.py`: crea el dataset de muestra.
- `modelo.py`: entrena y evalúa los modelos.
- `datos/demanda_transmilenio.csv`: fuente de datos.
- `DESCRIPCION_DATOS.md`: descripción de los datos.
- `PRUEBAS.md`: pruebas y resultados.
- `resultados/`: gráficos y salida del programa.
- `GUION_VIDEO.md`: guion del video.

## Cómo ejecutarlo
```
pip install -r requirements.txt
python generar_datos.py
python modelo.py
```

## Resumen
Se predice si la demanda de una estación es baja, media o alta según hora, día, festivo, lluvia y estación.
Mejor modelo: Random Forest (88,5 % de accuracy). Árbol de decisión: 80,2 %.
