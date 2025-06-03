import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Cargar el dataset limpio
df = pd.read_csv("rejilla_protegida_dataset_limpio.csv")

# Variables
X = df[["distance", "alt_mean", "conn_eco_mean"]]
y = df["perc_natural"]

# Dividir en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# Visualizar resultados
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, alpha=0.4, label="Predicciones")
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', label="Línea ideal (y = x)")
plt.xlabel("Valores reales (%)")
plt.ylabel("Predicción del modelo (%)")
plt.title("Modelo de regresión: valores reales vs. predichos")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()