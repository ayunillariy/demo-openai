import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import dotenv
import os
from src.emailprofesional import page1
#from src.expertocosntitucional import page2
from src.age_exp_mig_ca import page3
from src.textoaimagen import page4
from src.modificaimagen import page5
#from src.mezcladosimagenes import page6

st.set_page_config(page_title="Demo OpenAI", page_icon="favicon.png")

OpenAI.api_key = os.getenv("OPENAI_API_KEY")

pages = {
    "Experto en Redacción": page1,
    #"Experto Constitucional": page2,
    "Agente Migración CA": page3,
    "Texto a Imagen": page4,
    "Transformar Imagen": page5,
    #"Mezcla Imagen": page6

}
st.sidebar.header("Selecciona el Modelo")
page = st.sidebar.selectbox('Qué modelo quieres utilizar?', list(pages.keys()))
modelo =""
#st.write(page)
pages[page]()







