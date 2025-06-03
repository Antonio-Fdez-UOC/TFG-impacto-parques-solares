# Limpiar dataset
import pandas as pd

# Cargar el dataset original
df = pd.read_csv("rejilla_protegida_dataset_completo_filtrado.csv")

# Mostrar cuántas filas y columnas hay antes
print("Antes de limpiar:", df.shape)

# Eliminar filas con valores nulos en las columnas que usaremos
df = df.dropna(subset=["perc_natural", "alt_mean", "conn_eco_mean", "distance"])

# Mostrar cuántas quedan
print("Después de limpiar:", df.shape)

# Guardar el resultado limpio
df.to_csv("rejilla_protegida_dataset_limpio.csv", index=False)