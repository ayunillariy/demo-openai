import streamlit as st
import openai
from src.encabezado import head

def page4():
    modelo ="Texto a Imagen"
    descripcion="Utiliza el modelo de OpenAI DALL-E para crear una imagen a partir de un texto ingresado"
    st.write(head(modelo, descripcion))

    st.info("""#### NOTA: Puedes descargar esta imagen haciendo click derecho \
    y seleccionando la opción *Save as* o *Guardar como*""")

    with st.form(key='form'):
        prompt = st.text_input(label='Indícale a DALL-E como quieres que genere tu imagen')
        size = st.selectbox('Selcciona el tamaño de la imagen', 
                            ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('Indica la cantidad de imágenes que deseas generar', (1,2,3,4))
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        if prompt:
            response = openai.Image.create(
                    prompt = prompt,
                    n = num_images,
                    size=size,
                )
            
            for idx in range(num_images):
                image_url = response["data"][idx]["url"]

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)
    