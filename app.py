import os
import re
import streamlit as st
from langchain.chat_models import ChatOllama
from langchain.schema import HumanMessage

# Use Ollama with DeepSeek
llm = ChatOllama(model="deepseek-r1:1.5b", base_url="http://127.0.0.1:11434",keep_alive=True)

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

    # Extract content from the response by removing <think></think> tags
    response_content = response.content

    # Use regex to remove the <think></think> wrapper
    cleaned_response = re.sub(r'<think>.*?</think>', '', response_content).strip()

    # Store cleaned response
    st.session_state.messages.append({"role": "assistant", "content": cleaned_response})

    # Show cleaned response
    st.text_area("Assistant:", cleaned_response, disabled=True)

