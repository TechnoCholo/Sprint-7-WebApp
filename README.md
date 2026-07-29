# Dashboard de Venta de Vehículos

## Descripción del proyecto

Este proyecto realiza un análisis exploratorio de datos de anuncios de venta de vehículos. Incluye una aplicación web interactiva desarrollada con Streamlit para visualizar información del conjunto de datos.

## Estructura del repositorio

```text
Sprint7_GitHub/
│
├── app.py                  # Aplicación web desarrollada con Streamlit
├── vehicles_us.csv         # Conjunto de datos de vehículos
├── requirements.txt        # Dependencias de Python
└── notebooks/
    └── EDA.ipynb           # Análisis exploratorio de datos
```

## Aplicación de Streamlit

La aplicación permite explorar visualmente el conjunto de datos mediante gráficos interactivos:

* Histograma del kilometraje de los vehículos (`odometer`).
* Gráfico de dispersión que muestra la relación entre kilometraje y precio.
* Casilla de verificación para generar un histograma del kilometraje.

## Principales librerías utilizadas

* **Pandas:** carga y manipulación de datos.
* **Plotly Express:** creación de visualizaciones interactivas.
* **Streamlit:** desarrollo de la aplicación web.
* **Jupyter Notebook:** análisis exploratorio de datos.

## Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install -r requirements.txt
```

## Ejecución local

Para ejecutar la aplicación localmente:

```bash
streamlit run app.py
```

Streamlit proporcionará una dirección local para acceder a la aplicación desde el navegador.

## Aplicación pública

La aplicación está desplegada en Render y puede consultarse desde cualquier navegador:

**[PEGAR AQUÍ EL ENLACE PÚBLICO DE RENDER]**
