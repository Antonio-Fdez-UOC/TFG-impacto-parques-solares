# Análisis de Impacto Ambiental de Parques Solares en Zonas Protegidas de Cataluña mediante SIG y Modelos Predictivos

Este proyecto evalúa la relación entre parques solares fotovoltaicos y la fragmentación ecológica en zonas protegidas de Cataluña, mediante el uso de herramientas SIG (QGIS) y modelos predictivos en Python.

## 📁 Estructura del repositorio

```
├── data/
│   ├── raw/                # Datos originales descargados (GeoTIFF, SHP, GPKG, etc.)
│   ├── processed/          # Capas procesadas y rejillas con variables y CSVs finales usados en los modelos
├── docs/
│   ├── 01_figuras
│   ├── 02_presentación
├── scripts/
│   ├── 01_modelo_clasificacion.py
│   ├── 02_modelo_regresion.py
├── memoria/
│   └── TFG_memoria.pdf
├── planificación/
│   ├── Gantt
└── README.md
```

## 🛠️ Requisitos

- Python 3.9+
- QGIS 3.28+ con GRASS y GDAL instalados

## ▶️ Cómo reproducir el análisis

1. Abrir los scripts en `scripts/` y ejecutar secuencialmente:
    - `modelo_regresion.py`: ejecuta el análisis de regresión
    - `modelo_clasificacion.py`: ejecuta el modelo de clasificación

2. Los datos necesarios están en la carpeta `data/`. Puedes regenerarlos desde QGIS usando las instrucciones del apartado 3.2 de la memoria.

## 📌 Referencias

- Memoria completa del proyecto: `memoria/TFG_memoria.pdf`
