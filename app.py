import os
import streamlit as st
from langchain.chat_models import ChatOllama
from langchain.schema import AIMessage, HumanMessage

# Use Ollama with DeepSeek
llm = ChatOllama(model="deepseek")

# Streamlit Chat UI
st.title("🤖 Kaggle Chatbot with Ollama & DeepSeek")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    role = "You" if msg["role"] == "user" else "Assistant"
    st.text_area(role, msg["content"], disabled=True)

# User input
user_input = st.text_input("Type your message:")

if user_input:
    # Add user input to history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get response from DeepSeek via Ollama
    response = llm.invoke([HumanMessage(content=user_input)])

    # Store response
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    # Show response
    st.text_area("Assistant:", response.content, disabled=True)
