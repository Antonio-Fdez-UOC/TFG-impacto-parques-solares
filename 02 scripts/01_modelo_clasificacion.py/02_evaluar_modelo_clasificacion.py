import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_curve, auc
import matplotlib.pyplot as plt

# 1. Cargar el dataset con la variable fragmentada
df = pd.read_csv("rejilla_protegida_dataset_clasificacion.csv")

# 2. Definir variables predictora (X) y objetivo (y)
X = df[["distance"]]  # Solo una variable predictora
y = df["fragmentada"]

# 3. Dividir en entrenamiento y test (80/20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Entrenar el modelo de regresión logística
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# 5. Predecir y evaluar
y_pred = modelo.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Precisión (accuracy): {accuracy:.2f}")

# 6. Generar curva ROC
y_prob = modelo.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

# 7. Mostrar la curva ROC
plt.figure(figsize=(6, 6))
plt.plot(fpr, tpr, color="blue", lw=2, label=f"ROC (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], color="gray", linestyle="--")
plt.xlabel("Tasa de falsos positivos")
plt.ylabel("Tasa de verdaderos positivos")
plt.title("Curva ROC - Modelo de clasificación simple")
plt.legend(loc="lower right")
plt.grid(True)
plt.tight_layout()
plt.show()