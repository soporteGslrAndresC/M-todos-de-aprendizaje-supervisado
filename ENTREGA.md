---
title: "Actividad 3 - Métodos de aprendizaje supervisado"
subtitle: "Predicción de demanda en TransMilenio (Bogotá)"
---

**Estudiante:** ________________________  **Curso:** Inteligencia Artificial  **Fecha:** 11 de octubre de 2026

**Tutor agregado como colaborador del repositorio:** ☐ Sí

## Enlaces de entrega

| # | Elemento | Enlace |
|---|---|---|
| 1 | Repositorio Git (raíz) | https://github.com/USUARIO/transmilenio-ia |
| 2 | Archivos de fuentes de datos | https://github.com/USUARIO/transmilenio-ia/tree/main/datos |
| 3 | Código fuente en Python | https://github.com/USUARIO/transmilenio-ia/blob/main/modelo.py |
| 4 | Descripción de los datos | https://github.com/USUARIO/transmilenio-ia/blob/main/DESCRIPCION_DATOS.md |
| 5 | Pruebas realizadas | https://github.com/USUARIO/transmilenio-ia/blob/main/PRUEBAS.md |
| 6 | Video (máx. 10 min) | https://LINK_DEL_VIDEO |

## Resumen del proyecto

Se desarrolló un modelo de aprendizaje supervisado (clasificación) que predice si la demanda de una estación de TransMilenio
será **baja, media o alta**, usando como entradas la hora, el día de la semana, si es festivo, si llueve y la estación.

Como no se usó una fuente oficial, se creó un dataset de muestra de 52.704 registros que imita los patrones reales del sistema.
Se compararon tres modelos:

| Modelo | Accuracy | F1 |
|---|---|---|
| Regresión logística | 0,4875 | 0,4625 |
| Árbol de decisión | 0,8018 | 0,8030 |
| Random Forest | 0,8854 | 0,8852 |

El mejor modelo fue Random Forest. La variable más influyente fue la hora del día.
