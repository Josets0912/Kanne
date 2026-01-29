import streamlit as st
from PIL import Image

# Configuración básica de la página
st.set_page_config(page_title="La Decisión Final", page_icon="💖")

# 1. GESTIÓN DEL ESTADO (La "memoria" de la app)
# Iniciamos la variable 'etapa' si no existe
if 'etapa' not in st.session_state:
    st.session_state.etapa = 'inicio'

# Función para reiniciar el juego si pierde
def reiniciar_juego():
    st.session_state.etapa = 'juego'

# --- ESCENA 1: PANTALLA DE INICIO ---
if st.session_state.etapa == 'inicio':
    st.title("💖 Bienvenida al Juego del Amor 💖")
    st.write("Estás a punto de responder la pregunta más importante de la historia.")
    st.write("¿Estás lista?")
    
    # Botón grande para iniciar
    if st.button("JUGAR", type="primary", use_container_width=True):
        st.session_state.etapa = 'juego'
        st.rerun() # Recarga la página para cambiar de escena

# --- ESCENA 2: EL JUEGO (SELECCIÓN) ---
elif st.session_state.etapa == 'juego':
    st.title("¿Quién es el más guapo? 🤔")
    
    # Lista de candidatos y sus fotos
    # Asegúrate de que los nombres de archivo coincidan EXACTAMENTE
    candidatos = [
        {"nombre": "Jumpio", "foto": "jumpio.jpg", "es_correcto": False},
        {"nombre": "Jungkook", "foto": "jungkook.jpg", "es_correcto": False},
        {"nombre": "Mi Amor (Tú)", "foto": "yo.jpg", "es_correcto": True}, # ¡Esta es la correcta!
        {"nombre": "Pedrito Astorga", "foto": "pedrito.jpg", "es_correcto": False},
        {"nombre": "Pangal", "foto": "pangal.jpg", "es_correcto": False}
    ]

    # Crear columnas dinámicas
    cols = st.columns(len(candidatos))

    for i, candidato in enumerate(candidatos):
        with cols[i]:
            try:
                img = Image.open(candidato["foto"])
                st.image(img, use_container_width=True)
            except FileNotFoundError:
                st.error(f"Falta: {candidato['foto']}")
            
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
    st.balloons() # Efecto de globos
    st.title("¡GANASTE! 🎉❤️")
    st.header("Sabía que eras la indicada.")
    st.image("yo.jpg", width=300, caption="El verdadero ganador de tu corazón")
    st.success("Te amo infinito.")
    
    if st.button("Jugar de nuevo (por si dudas)"):
        st.session_state.etapa = 'inicio'
        st.rerun()

# --- ESCENA 4: PERDISTE (SI ELIGE A OTRO) ---
elif st.session_state.etapa == 'perdiste':
    st.title("Tienes muy mal gusto... 🤮")
    st.header("¡¿En serio?!")
    st.error("Tu elección ha sido incorrecta. Vuelve a intentarlo hasta que elijas bien.")
    
    # Botón para volver a intentar
    st.button("Intentar de nuevo (y elegir bien esta vez)", on_click=reiniciar_juego)