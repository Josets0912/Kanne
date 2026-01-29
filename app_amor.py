import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(page_title="La Gran Encuesta", page_icon="❤️")

st.title("❤️ Una pregunta muy importante ❤️")
st.subheader("¿Quién es el hombre más guapo del mundo?")

# Definición de los candidatos
candidatos = {
    "Jumpio el Coreano": "jumpio.jpg",
    "Jungkook": "jungkook.jpg",
    "Pedrito Astorga": "pedrito.jpg",
    "Pangal Andrade": "pangal.jpg",
    "Tú (El amor de mi vida)": "yo.jpg" # Cambia esto por tu nombre real si quieres
}

# Crear columnas para mostrar las fotos
cols = st.columns(len(candidatos))

# Mostrar las imágenes y un botón debajo de cada una
for i, (nombre, archivo) in enumerate(candidatos.items()):
    with cols[i]:
        try:
            img = Image.open(archivo)
            st.image(img, use_container_width=True)
        except FileNotFoundError:
            st.warning(f"Falta foto: {archivo}")
        
        if st.button(f"Elegir a {nombre.split()[0]}", key=nombre):
            if nombre == "Tú (El amor de mi vida)":
                st.balloons()
                st.success("¡GANASTE! ❤️ Sabía que tenías buen gusto. ¡Te amo!")
            else:
                st.error("Error 404: Respuesta incorrecta. Inténtalo de nuevo. ❌")

# Pie de página romántico
st.markdown("---")
st.write("Hecho con ❤️ por tu ingeniero favorito.")