import streamlit as st
from PIL import Image
import os

# --- CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="La Decisión Final", page_icon="💖")

# Función auxiliar para cargar imágenes de forma segura
# Esto evita el error rojo gigante si el nombre no coincide exacto
def cargar_imagen_segura(nombre_archivo):
    try:
        # Intenta abrir la imagen con el nombre exacto
        img = Image.open(nombre_archivo)
        return img
    except FileNotFoundError:
        # Si no la encuentra, devuelve None
        return None

# 1. GESTIÓN DEL ESTADO (La "memoria" de la app)
if 'etapa' not in st.session_state:
    st.session_state.etapa = 'inicio'

def reiniciar_juego():
    st.session_state.etapa = 'juego'

# --- ESCENA 1: PANTALLA DE INICIO ---
if st.session_state.etapa == 'inicio':
    st.title("💖 Bienvenida al Juego del Amor 💖")
    st.write("Estás a punto de responder la pregunta más importante de la historia.")
    st.write("¿Estás lista?")
    
    if st.button("JUGAR", type="primary", use_container_width=True):
        st.session_state.etapa = 'juego'
        st.rerun()

# --- ESCENA 2: EL JUEGO (SELECCIÓN) ---
elif st.session_state.etapa == 'juego':
    st.title("¿Quién es el más guapo? 🤔")
    st.write("Elige con sabiduría...")
    
    # DEFINICIÓN DE CANDIDATOS
    # IMPORTANTE: Los nombres de archivo "foto" deben ser EXACTOS (preferible minúsculas)
    candidatos = [
        {"nombre": "Jumpio", "foto": "jumpio.jpg", "es_correcto": False},
        {"nombre": "Jungkook", "foto": "jungkook.jpg", "es_correcto": False},
        {"nombre": "Mi Amor (Tú)", "foto": "yo.jpg", "es_correcto": True}, 
        {"nombre": "Pedrito Astorga", "foto": "pedrito.jpg", "es_correcto": False},
        {"nombre": "Pangal", "foto": "pangal.jpg", "es_correcto": False}
    ]

    # Crear columnas para las fotos
    cols = st.columns(len(candidatos))

    for i, candidato in enumerate(candidatos):
        with cols[i]:
            # Usamos la función segura para cargar la imagen
            img = cargar_imagen_segura(candidato["foto"])
            
            if img:
                st.image(img, use_container_width=True)
            else:
                # Si falla, muestra un recuadro gris con el nombre del archivo que falta
                st.warning(f"Falta: {candidato['foto']}")
            
            # Botón de selección
            if st.button(f"Elegir", key=candidato["nombre"]):
                if candidato["es_correcto"]:
                    st.session_state.etapa = 'ganaste'
                    st.rerun()
                else:
                    st.session_state.etapa = 'perdiste'
                    st.rerun()

# --- ESCENA 3: GANASTE (SI TE ELIGE A TI) ---
elif st.session_state.etapa == 'ganaste':
    st.balloons()
    st.title("¡GANASTE! 🎉❤️")
    st.header("Sabía que eras la indicada.")
    
    # Cargamos tu foto final de forma segura también
    img_final = cargar_imagen_segura("yo.jpg")
    if img_final:
         st.image(img_final, width=300, caption="El verdadero ganador de tu corazón")
    else:
         st.warning("🙈 (Aquí debería ir mi foto guapo, pero el archivo 'yo.jpg' no se encontró. ¡Revísalo!)")

    st.success("Te amo infinito.")
    
    if st.button("Jugar de nuevo"):
        st.session_state.etapa = 'inicio'
        st.rerun()

# --- ESCENA 4: PERDISTE (SI ELIGE A OTRO) ---
elif st.session_state.etapa == 'perdiste':
    st.title("Tienes muy mal gusto... 🤮")
    st.header("¡¿En serio?!")
    st.error("Tu elección ha sido incorrecta. Vuelve a intentarlo hasta que elijas bien.")
    
    st.button("Intentar de nuevo (y elegir bien esta vez)", on_click=reiniciar_juego)