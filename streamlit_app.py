import streamlit as st
import pandas as pd
from io import StringIO
import plotly.graph_objects as go

# Configuración de la página
st.set_page_config(
    page_title="Chat App Luiggi",
    page_icon="💬",
    layout="centered"
)

# Título de la aplicación
st.title("Aplicativo con flow")


uploaded_file = st.file_uploader("Sube tu archivo excel con el flujo de caja")

if uploaded_file is not None:
    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_excel(uploaded_file)
    st.session_state.data = dataframe

    
if st.button("Ejecutar Flow"):
    st.write(st.session_state.data)

    fig_flow = go.Figure()
    
    fig_flow.add_trace(go.Scatter(
        x=st.session_state.data['fecha'],
        y=st.session_state.data['flujo'],
        mode='lines',
        name='Flujo de caja',
        line=dict(color='#1f77b4', width=2)
    ))
    
    fig_flow.update_layout(
        xaxis_title="Fecha",
        yaxis_title="Valor (USD)",
        hovermode='x unified',
        height=500
    )
    
    st.plotly_chart(fig_flow, use_container_width=True)
    st.success("Flow ejecutado correctamente!")

with st.sidebar:
    st.header("ℹ️ Información")
    st.write("Esta aplicacion necesita lo siguiente:")
    st.write("Cargar un archivo excel con datos del flujo de caja")
    st.write("Darle click a ejecuta flow")
