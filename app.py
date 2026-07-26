import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv("vehicles_us.csv")

st.header("Análisis de venta de vehículos")

hist_button = st.button('Construye un histograma') # crear un botón
     
if hist_button: # al hacer clic en el botón
         # escribir un mensaje
     st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
         
         # crear un histograma
     histogram_fig = px.histogram(car_data, x="odometer")
     
         # mostrar un gráfico Plotly interactivo
     st.plotly_chart(histogram_fig, use_container_width=True)

disp_button = st.button("Construye un gráfico de dispersión")

if disp_button: # al hacer clic en el botón
         # escribir un mensaje
     st.write('Relación entre el kilometraje y el precio.')
         
         # crear un grafico
     scatter_fig = px.scatter(car_data, x="odometer", y="price")
     
         # mostrar un gráfico Plotly 
     st.plotly_chart(scatter_fig, use_container_width=True)
     