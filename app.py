import streamlit as st
from retriever import load_data, create_index, retrieve_answer
from generator import generate_response
import asyncio
import sys






# Fix event loop issue on Windows
if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

# Disable Streamlit file watcher for Torch
import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "True"



# Load and preprocess data
questions, answers = load_data('data/covid.json')
index, _ = create_index(questions)

# Streamlit UI
st.title("COVID-19 FAQ RAG Chatbot")

# User input
query = st.text_input("Ask a question about COVID-19:")

if st.button("Get Answer"):
    if query:
        print(query)
        retrieved_question, retrieved_answer = retrieve_answer(query, questions, answers, index)
        st.subheader("Retrieved Answer:")
        st.write(retrieved_answer)
        
        # Generate a better response using LLM
        generated_response = generate_response(retrieved_answer)
        st.subheader("Generated Response:")
        st.write(generated_response)
    else:
        st.warning("Please enter a question.")

# Display some sample questions
st.sidebar.title("Sample Questions")
st.sidebar.write("1. What are the symptoms of COVID-19?")
st.sidebar.write("2. How does COVID-19 spread?")
st.sidebar.write("3. What are the treatments available for COVID-19?")
