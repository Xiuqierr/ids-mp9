import streamlit as st
from transformers import pipeline

st.title('My AI Chatbot')
user_input = st.text_input("Talk to the chatbot:")

chat = pipeline('text-generation', model='microsoft/DialoGPT-medium')

if user_input:
    response = chat(user_input)[0]['generated_text']
    st.text_area("Chatbot says:", value=response, height=100, max_chars=None, key=None)
