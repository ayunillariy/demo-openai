import streamlit as st 


def head(modelo, descripcion):

    col1, col2 = st.columns(2)


    with col1:
        st.title("Demo OpenAI")
        st.markdown(modelo)
        st.markdown(descripcion)
    with col2:
        st.image(image='chat.png', width=200)
        