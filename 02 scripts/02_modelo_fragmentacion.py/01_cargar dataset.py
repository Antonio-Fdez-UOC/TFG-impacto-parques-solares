import pandas as pd

# Cargar el dataset CSV generado en QGIS
df = pd.read_csv("rejilla_protegida_dataset_completo_filtrado.csv")

# Mostrar las primeras filas
print(df.head())
print(df.columns)