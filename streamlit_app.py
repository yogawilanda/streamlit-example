import streamlit as st

st.title("Local AI With Streamlit")

with st.sidebar:
    messages = st.container(height=800)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        messages.chat_message("assistant").write(f"Echo: {prompt}")