
import streamlit as st
import google.generativeai as genai

# Configurar la API Key de Gemini
genai.configure(api_key="AIzaSyB_dSG6kxbmJVN2F5MwqrWYOjflwX-DZYg")

# Inicializamos el modelo Gemini-Pro
model = genai.GenerativeModel("gemini-pro")

# Interfaz de usuario Streamlit
st.title("BalancIA - Tutor de Destilación")
st.write("Haz tus preguntas sobre destilación, balances de materia y energía.")

# Prompt inicial de contexto para BalancIA
prompt_inicial = '''
Eres BalancIA, un tutor experto en procesos de destilación y balances de materia y energía. Tu misión es enseñar y ayudar a estudiantes de ingeniería química.
Responde con explicaciones claras, ejemplos cuando sea necesario, y pasos detallados. Siempre verifica que el estudiante entienda los conceptos de:
- Tipos de destilación
- Diseño de columnas
- Balances de materia y energía
- Cálculo de número de platos teóricos
- Parámetros operativos: reflujo, presión, temperatura.
Si el estudiante comete un error o tiene confusión, explícale pacientemente y sugiere cómo mejorar su razonamiento.

Pregunta: {pregunta}
Respuesta:
'''

# Campo de entrada
pregunta = st.text_area("Escribe tu pregunta aquí:")

# Botón de enviar
if st.button("Preguntar a BalancIA"):
    if pregunta.strip() == "":
        st.warning("Por favor escribe una pregunta.")
    else:
        prompt = prompt_inicial.format(pregunta=pregunta)
        respuesta = model.generate_content(prompt)
        st.success(respuesta.text)
