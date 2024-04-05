import streamlit as st
from transformers import pipeline

st.title('My AI Chatbot')
user_input = st.text_input("Talk to the chatbot:")

model = pipeline("text-generation", model="openai-gpt")

if user_input:
    response = model(user_input)[0]['generated_text']
    st.text_area("Chatbot says:", value=response, height=100, max_chars=None, key=None)
