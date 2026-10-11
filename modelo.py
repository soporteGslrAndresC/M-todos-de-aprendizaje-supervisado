# modelo.py
# Predice el nivel de demanda (baja / media / alta) de una estación de TransMilenio
# usando aprendizaje supervisado (clasificación).

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # permite guardar imágenes sin abrir ventana
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, ConfusionMatrixDisplay

# 1. Cargar los datos
df = pd.read_csv("datos/demanda_transmilenio.csv")
print("Filas y columnas:", df.shape)
print(df.head())
print("Valores vacíos:", df.isnull().sum().sum())

# 2. Preparar los datos
# OJO: NO usamos 'pasajeros' como entrada, porque de ahí sale la etiqueta (sería trampa).
df = pd.get_dummies(df, columns=["estacion", "troncal"])  # texto -> números (0/1)
X = df.drop(columns=["fecha", "pasajeros", "nivel_demanda"])  # variables de entrada
y = df["nivel_demanda"]                                       # lo que queremos predecir

# 3. Separar 80% para entrenar y 20% para probar
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y)

# 4. Definir los 3 modelos
modelos = {
    "Regresión logística": LogisticRegression(max_iter=2000),
    "Árbol de decisión": DecisionTreeClassifier(max_depth=6, random_state=42),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
}

# 5. Entrenar y evaluar cada modelo
resultados = []
mejores_pred = {}
for nombre, modelo in modelos.items():
    modelo.fit(X_train, y_train)              # entrenar
    pred = modelo.predict(X_test)             # predecir sobre datos nuevos
    acc = accuracy_score(y_test, pred)
    f1 = f1_score(y_test, pred, average="macro")
    resultados.append([nombre, round(acc, 4), round(f1, 4)])
    mejores_pred[nombre] = pred

tabla = pd.DataFrame(resultados, columns=["Modelo", "Accuracy", "F1"])
print("\nRESULTADOS:")
print(tabla.to_string(index=False))
tabla.to_csv("resultados/comparacion_modelos.csv", index=False)

# 6. Matriz de confusión del árbol de decisión
etiquetas = ["baja", "media", "alta"]
arbol = modelos["Árbol de decisión"]
cm = confusion_matrix(y_test, mejores_pred["Árbol de decisión"], labels=etiquetas)
print("\nMatriz de confusión (árbol):\n", cm)
ConfusionMatrixDisplay(cm, display_labels=etiquetas).plot(cmap="Blues")
plt.title("Matriz de confusión - Árbol de decisión")
plt.savefig("resultados/matriz_confusion.png", dpi=120, bbox_inches="tight")
plt.close()

# 7. Dibujar el árbol (solo los primeros niveles para que se lea bien)
plt.figure(figsize=(16, 7))
plot_tree(arbol, max_depth=3, feature_names=X.columns, class_names=arbol.classes_,
          filled=True, fontsize=7)
plt.savefig("resultados/arbol_decision.png", dpi=120, bbox_inches="tight")
plt.close()

# 8. Variables más importantes para el árbol
imp = pd.Series(arbol.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop 5 variables importantes:\n", imp.head(5).round(3))

# 9. Prueba con un caso nuevo: lunes, 7 am, sin lluvia, Portal Norte
caso = pd.DataFrame([[0] * len(X.columns)], columns=X.columns)
caso["hora"] = 7
caso["dia_semana"] = 0
caso["estacion_Portal Norte"] = True
caso["troncal_Autonorte"] = True
print("\nPredicción lunes 7am en Portal Norte:", arbol.predict(caso)[0])
