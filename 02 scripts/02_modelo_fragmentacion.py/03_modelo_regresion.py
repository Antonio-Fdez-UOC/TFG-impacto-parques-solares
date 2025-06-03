# Modelo de regresión lineal

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error

# 1. Cargar el dataset limpio
df = pd.read_csv("rejilla_protegida_dataset_limpio.csv")

# 2. Definir variables predictoras (X) y objetivo (y)
X = df[["distance", "alt_mean", "conn_eco_mean"]]
y = df["perc_natural"]

# 3. Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Crear y entrenar el modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# 5. Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# 6. Evaluar el modelo
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("RESULTADOS DEL MODELO DE REGRESIÓN:")
print("-----------------------------------")
print(f"Coeficiente de determinación (R²): {r2:.4f}")
print(f"Error absoluto medio (MAE): {mae:.2f}")