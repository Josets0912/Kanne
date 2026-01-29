import streamlit as st
from PIL import Image

# --- CONFIGURACIÓN ---
# Aquí ya puse el nombre exacto de tu archivo
NOMBRE_TU_FOTO = "mifoto.jpg" 

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="La Decisión Final", page_icon="💖")

# Función para cargar imagen sin errores
def cargar_imagen(nombre_archivo):
    try:
        return Image.open(nombre_archivo)
    except FileNotFoundError:
        return None

# 1. GESTIÓN DE ESTADO (MEMORIA)
if 'etapa' not in st.session_state:
    st.session_state.etapa = 'inicio'

def reiniciar():
    st.session_state.etapa = 'juego'

# --- ESCENA 1: INICIO ---
if st.session_state.etapa == 'inicio':
    st.title("💖 Bienvenida al Juego del Amor 💖")
    st.write("Estás a punto de responder la pregunta más importante...")
    if st.button("JUGAR AHORA", type="primary", use_container_width=True):
        st.session_state.etapa = 'juego'
        st.rerun()

# --- ESCENA 2: JUEGO ---
elif st.session_state.etapa == 'juego':
    st.title("¿Quién es el más guapo? 🤔")
    
    # Lista de candidatos
    candidatos = [
        {"nombre": "Jumpio", "foto": "jumpio.jpg", "correcto": False},
        {"nombre": "Jungkook", "foto": "jungkook.jpg", "correcto": False},
        {"nombre": "Mi Amor (Tú)", "foto": NOMBRE_TU_FOTO, "correcto": True}, # Usa mifoto.jpg
        {"nombre": "Pedrito Astorga", "foto": "pedrito.jpg", "correcto": False},
        {"nombre": "Pangal", "foto": "pangal.jpg", "correcto": False}
    ]

    cols = st.columns(len(candidatos))
    
    for i, c in enumerate(candidatos):
        with cols[i]:
            img = cargar_imagen(c["foto"])
            if img:
                st.image(img, use_container_width=True)
            else:
                st.warning(f"Falta: {c['foto']}")
            
            if st.button("Elegir", key=c["nombre"]):
                if c["correcto"]:
                    st.session_state.etapa = 'ganaste'
                    st.rerun()
                else:
                    st.session_state.etapa = 'perdiste'
                    st.rerun()

# --- ESCENA 3: GANASTE ---
elif st.session_state.etapa == 'ganaste':
    st.balloons()
    st.title("¡GANASTE! 🎉❤️")
    st.header("Sabía que eras la indicada.")
    
    # Muestra tu foto
    img_final = cargar_imagen(NOMBRE_TU_FOTO)
    if img_final:
        st.image(img_final, width=300, caption="El hombre de tu vida")
    else:
        st.error(f"No encuentro la foto: {NOMBRE_TU_FOTO}")
        
    st.success("Te amo infinito.")
    if st.button("Reiniciar"):
        st.session_state.etapa = 'inicio'
        st.rerun()

# --- ESCENA 4: PERDISTE ---
elif st.session_state.etapa == 'perdiste':
    st.title("Tienes muy mal gusto... 🤮")
    st.error("Respuesta incorrecta. Vuelve a intentarlo.")
    st.button("Intentar de nuevo", on_click=reiniciar)