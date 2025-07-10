# app.py

import streamlit as st
from src.retriever import get_top_k_chunks
from src.generator import generate_response

st.set_page_config(page_title="Fine-Tuned RAG Chatbot with Streaming Responses - Amlgo Labs", layout="wide")

# Sidebar Info Panel
with st.sidebar:
    st.header("Chatbot Configuration")
    st.markdown("**Model in Use:** TinyLlama via Ollama")
    st.markdown(f"**Chunks Indexed:** ~{len(get_top_k_chunks('test', k=100))}")
    if st.button(" Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# 🧠 Header
st.title("Legal Document Chatbot - Amlgo Labs")
st.write("Please ask your legal document-related questions.")

# Session state for chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 🔧 Formatting: paragraph + bullet mix

def format_response(text: str) -> str:
    import re
    paragraphs = text.split('\n')
    formatted = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        # If sentence seems like a list or instruction, convert to bullet
        if any(kw in p.lower() for kw in ["such as", "include", "for example", "may", "should", "can"]):
            bullets = re.split(r'(?<!\w)\s*[\u2022*-]\s*', p)
            for b in bullets:
                b = b.strip("-• ").strip()
                if len(b.split()) > 3:
                    formatted.append(f"- {b}")
        else:
            formatted.append(p)
    return "\n\n".join(formatted)

# Chat input
query = st.chat_input("Ask your question...")

if query:
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        response_area = st.empty()
        full_response = ""

        with st.spinner("🤖 Thinking, please wait..."):
            context_chunks = get_top_k_chunks(query, k=100)

            for token in generate_response(query, context_chunks):
                full_response += token
                response_area.markdown(full_response + "▌")

        # Format response (paragraph + bullets)
        formatted_response = format_response(full_response)
        response_area.markdown(formatted_response)

    st.session_state.messages.append({"role": "assistant", "content": formatted_response})

    # Source context display
    with st.expander("📖 Source Chunks Used"):
        for i, chunk in enumerate(context_chunks, 1):
            st.markdown(f"**Chunk {i}:** {chunk[:500]}{'...' if len(chunk) > 500 else ''}")



