#https://www.datos.gov.co/Ambiente-y-Desarrollo-Sostenible/CORPOBOYACA-REPORTE-DE-INCENDIOS-DE-LA-COBERTURA-V/ryr5-rs2a/about_data
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sodapy import Socrata

# Crear una instancia de Socrata con app_token válido
clientes = Socrata("www.datos.gov.co", None)

# Obtener los resultados del conjunto de datos
results = clientes.get("ryr5-rs2a")

# Convertir los resultados a un DataFrame de pandas
df = pd.DataFrame.from_records(results)

# Mostrar las primeras filas del DataFrame
print(df.head())

# Limitar el DataFrame pasando de 119 columnas a 30 columnas en donde no aparezcan valores nulos
df = df.dropna(axis=1, thresh=len(df) - 1)
print(df.head())

# Verificar las columnas del DataFrame
print(df.columns)

# Grafica acorde a los datos que se nos presentan
sns.set(style="whitegrid")
plt.figure(figsize=(10, 6))
sns.countplot(x="municipio", data=df, palette="Set2")
plt.xticks(rotation=45)
plt.legend([],[], frameon=False) 
plt.show()

# Convertir las columnas fecha_de_inicio y fecha_de_finalizaci_n a objetos de tipo fecha
df["fecha_de_inicio"] = pd.to_datetime(df["fecha_de_inicio"], format='%Y-%m-%d', errors='coerce')
df["fecha_de_finalizaci_n"] = pd.to_datetime(df["fecha_de_finalizaci_n"], format='%Y-%m-%dT%H:%M:%S.%f', errors='coerce')

# Eliminar filas con valores nulos en fecha_de_finalizaci_n
df = df.dropna(subset=["fecha_de_finalizaci_n"])

# Calcular la duración en horas
df["duracion"] = (df["fecha_de_finalizaci_n"] - df["fecha_de_inicio"]).dt.total_seconds() / 3600

# Mostrar el promedio de duración en horas
promedio_duracion = df["duracion"].mean()
print(f"Promedio de duración en horas: {promedio_duracion}")

# Histograma de la duración de los incendios en horas
plt.figure(figsize=(10, 6))
sns.histplot(df["duracion"], bins=30, kde=True)
plt.title("Distribución de la duración en horas")
plt.xlabel("Duración en horas")
plt.ylabel("Frecuencia")
plt.show()

# Violin plot de la duración en horas
plt.figure(figsize=(10, 6))
sns.violinplot(x=df["duracion"])
plt.title("Violin plot de la duración en horas")
plt.xlabel("Duración en horas")
plt.show()

# Gráfico de barras de la duración promedio por municipio
plt.figure(figsize=(12, 8))
sns.barplot(x="municipio", y="duracion", data=df, estimator=lambda x: sum(x) / len(x), ci=None, palette="Set2")
plt.title("Duración promedio por municipio")
plt.xlabel("Municipio")
plt.ylabel("Duración promedio en horas")
plt.xticks(rotation=45)
plt.show()

# Explicacion de graficas
print("En la primera gráfica se muestra la cantidad de incendios por municipio, en donde se puede observar que el municipio de Sogamoso es el que más incendios presenta.")
print("En la segunda gráfica se muestra la distribución de la duración de los incendios en horas, en donde se puede observar que la mayoría de los incendios duran menos de 100 horas.")
print("En la tercera gráfica se muestra un violin plot de la duración de los incendios en horas, en donde se puede observar que la mayoría de los incendios duran menos de 100 horas.")