import streamlit as st
from app_language import follow_chat
st.title("MathGPT")
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ("assistant", "Hola, soy MathGPT, un asistente con capacidades matemáticas a través de Python.")
    ]
user_input = st.chat_input(
    placeholder="Introduce aquí tu pregunta"
)
if user_input:
    st.session_state["messages"].append(("user", user_input))
    st.session_state["messages"].append(("assistant", follow_chat(user_input)))
for author, message in st.session_state["messages"]:
    st.chat_message(name=author).write(message)