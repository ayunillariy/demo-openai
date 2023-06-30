import streamlit as st
import openai
from src.encabezado import head
from PIL import Image
from src.utils import get_width_height, resize_image

def page5():
    modelo ="Transforma Imagen"
    descripcion="Transforma imagen selecionada mediante una instrucción de texto"
    st.write(head(modelo, descripcion))
    st.info("""#### NOTA: Puedes descargar esta imagen haciendo click derecho \
    y seleccionando la opción *Save as* o *Guardar como*""")

    with st.form(key='form'):
        uploaded_file = st.file_uploader("Selecciona archivo de imagen", type=['png', 'jpg'])
        size = st.selectbox('Selcciona el tamaño de la imagen', 
                            ('256x256', '512x512', '1024x1024'))
        num_images = st.selectbox('Indica la cantidad de imágenes que deseas generar', (1,2,3,4))
        submit_button = st.form_submit_button(label='Enviar')

    if submit_button:
        if uploaded_file is not None:

            image = Image.open(uploaded_file)
            
            st.image(image, caption="Uploaded image", use_column_width=True)
            
            width, height = get_width_height(size)
            image = resize_image(image, width, height)
            
            response = openai.Image.create_variation(
                    image=image,
                    n = num_images,
                    size=size,
                )
            
            for idx in range(num_images):
                image_url = response["data"][idx]["url"]

                st.image(image_url, caption=f"Generated image: {idx+1}",
                         use_column_width=True)

    