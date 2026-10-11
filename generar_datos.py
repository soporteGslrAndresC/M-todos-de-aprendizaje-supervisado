# generar_datos.py
# Crea un dataset de MUESTRA (sintético) de demanda en estaciones de TransMilenio.
# Se usa porque no se descargó un dataset oficial; los patrones imitan la realidad:
# más pasajeros en horas pico (6-8 y 17-19), entre semana y en estaciones grandes.

import numpy as np
import pandas as pd

np.random.seed(42)  # para que el resultado siempre sea igual

# Estaciones reales de TransMilenio con un "tamaño" (qué tan grande es su demanda base)
estaciones = {
    "Portal Norte": ("Autonorte", 1.6),
    "Portal Sur": ("Sur", 1.6),
    "Portal 80": ("Calle 80", 1.5),
    "Portal Américas": ("Américas", 1.4),
    "Portal Suba": ("Suba", 1.4),
    "Portal Usme": ("Usme", 1.3),
    "Av. Jiménez": ("Eje Ambiental", 1.2),
    "Museo del Oro": ("Eje Ambiental", 1.0),
    "Calle 100": ("Autonorte", 1.1),
    "Banderas": ("Américas", 0.9),
    "Ricaurte": ("NQS", 0.9),
    "Marly": ("Caracas", 0.8),
}

# Festivos de ejemplo (2024)
festivos = pd.to_datetime(["2024-01-01", "2024-01-08", "2024-03-25", "2024-03-28",
                           "2024-03-29", "2024-05-01", "2024-05-13", "2024-06-03",
                           "2024-06-10", "2024-07-01", "2024-07-20", "2024-08-07"])

filas = []
fechas = pd.date_range("2024-01-01", "2024-08-31")  # unos 8 meses

for fecha in fechas:
    dia_semana = fecha.dayofweek          # 0 = lunes ... 6 = domingo
    es_festivo = 1 if fecha in festivos else 0
    llueve = 1 if np.random.rand() < 0.3 else 0

    for estacion, (troncal, tamano) in estaciones.items():
        for hora in range(5, 23):         # de 5 am a 10 pm
            # Demanda base según la hora
            if hora in (6, 7, 8) or hora in (17, 18, 19):
                base = 1500               # hora pico
            elif hora in (9, 10, 16, 20):
                base = 900
            else:
                base = 450

            # Fines de semana y festivos hay menos gente
            if dia_semana == 5:
                base *= 0.65
            elif dia_semana == 6 or es_festivo:
                base *= 0.45

            # La lluvia sube un poco la demanda
            if llueve:
                base *= 1.1

            pasajeros = int(base * tamano * np.random.normal(1, 0.12))
            filas.append([fecha.date(), hora, dia_semana, es_festivo, llueve,
                          estacion, troncal, max(pasajeros, 0)])

df = pd.DataFrame(filas, columns=["fecha", "hora", "dia_semana", "es_festivo",
                                  "llueve", "estacion", "troncal", "pasajeros"])

# Etiqueta a predecir: nivel de demanda (baja / media / alta)
def nivel(p):
    if p < 600:
        return "baja"
    elif p < 1400:
        return "media"
    return "alta"

df["nivel_demanda"] = df["pasajeros"].apply(nivel)

df.to_csv("datos/demanda_transmilenio.csv", index=False)
print("Dataset creado:", df.shape[0], "filas")
print(df["nivel_demanda"].value_counts())
