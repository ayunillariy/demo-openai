import streamlit as st
from src.encabezado import head

def page3():
    modelo ="Experto en Migración CA"
    descripcion="Responde preguntas relacionadas con las normativas de migración hacia Canadá"
    st.write(head(modelo, descripcion))