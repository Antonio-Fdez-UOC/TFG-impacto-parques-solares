# Preparar modelo de clasificación

import pandas as pd

# Cargar el dataset limpio
df = pd.read_csv("rejilla_protegida_dataset_limpio.csv")

# Crear la variable binaria 'fragmentada': 1 si perc_natural < 30, 0 si no
df["fragmentada"] = df["perc_natural"].apply(lambda x: 1 if x < 30 else 0)

# Ver distribución de clases
print("Distribución de clases (fragmentada):")
print(df["fragmentada"].value_counts())

# Guardar dataset con la nueva variable
df.to_csv("rejilla_protegida_dataset_clasificacion.csv", index=False)
print("Nuevo dataset guardado como 'rejilla_protegida_dataset_clasificacion.csv'")