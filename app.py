import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# URLs de los archivos CSV (asegúrate de usar el mismo nombre de repo si es el mismo)
base_url = "https://raw.githubusercontent.com/TU_USUARIO/Dashboard-ChocolateExport/main/"

clientes_url = base_url + "clientes.csv"
mercados_url = base_url + "mercados.csv"
exportaciones_url = base_url + "exportaciones.csv"
barreras_url = base_url + "barreras.csv"

# Cargar datos
clientes = pd.read_csv(clientes_url)
mercados = pd.read_csv(mercados_url)
exportaciones = pd.read_csv(exportaciones_url)
barreras = pd.read_csv(barreras_url)

# Título del Dashboard
st.title("Dashboard Interactivo de Exportaciones de Chocolates")

# Filtro de país
paises = exportaciones["País"].unique()
pais_seleccionado = st.selectbox("Selecciona un país para ver los detalles", paises)

# Mostrar datos de clientes
st.subheader("Clientes")
clientes_filtrados = clientes[clientes["País"] == pais_seleccionado]
st.dataframe(clientes_filtrados)

# Mostrar datos de exportaciones
st.subheader("Exportaciones de Chocolates")
exportaciones_filtradas = exportaciones[exportaciones["País"] == pais_seleccionado]
fig, ax = plt.subplots()
ax.bar(exportaciones_filtradas["País"], exportaciones_filtradas["Exportaciones (USD millones)"], color='#2E86C1')
ax.set_xlabel("País")
ax.set_ylabel("
