import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
from src.encabezado import head





def page1():

    modelo = "Experto en Redacción"
    descripcion = "Transforma el texto ingresado de acuerdo al estilo y dialecto selecciona"

    st.write(head(modelo, descripcion))

    template = """
            Below is the email, estilo y dialecto:
            ESTILO: {estilo}
            DIALECTO: {dialecto}
            EMAIL: {email}

            TU RESPUESTA
        """

    prompt = PromptTemplate(
    input_variables=["estilo", "dialecto", "email"],
    template = template,
    )
        

    col1, col2 = st.columns(2)

    with col1:
            estilo_opcion = st.selectbox(
            'Qué estilo deseas para tu redacción de correo?',
            ('Formal', 'Informal'))
    
    with col2:
            dialecto_opcion = st.selectbox(
            'Qué dialecto de español prefieres?',
            ('Español España', 'Español Chile'))
    
        
    input_text = st.text_area(label="Redacta tu mensaje, para ejecutar la corrección presiona Ctrl + Enter",
                                   placeholder="Escribe tu mensaje", key="email_input")
    st.markdown("### Redacción corregida")

    if input_text:
            llm = OpenAI(temperature=.5)
            prompt_with_email = prompt.format(estilo=estilo_opcion, dialecto=dialecto_opcion, email=input_text)

            formatted_email = llm(prompt_with_email)

            st.write(formatted_email)



