# src/generator.py

import requests
import json

# Ollama API configuration
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"  # or "zephyr" if installed

def format_prompt(context_chunks, question):
    """
    Formats the prompt by injecting context chunks and the user's question.
    """
    context_text = "\n\n".join(context_chunks)
    prompt = f"""You are an AI assistant. Answer the user's question truthfully using only the provided context.

Context:
{context_text}

Question: {question}
Answer:"""
    return prompt

def generate_response(question, context_chunks):
    """
    Calls Ollama API to generate a streamed response from the model.
    Yields each text token in real-time.
    """
    prompt = format_prompt(context_chunks, question)

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": True
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload, stream=True)
        for line in response.iter_lines():
            if line:
                try:
                    # Parse JSON from streamed line
                    data = json.loads(line.decode('utf-8'))
                    # Extract only the token text
                    if 'response' in data:
                        yield data['response']
                except json.JSONDecodeError:
                    continue
    except requests.exceptions.RequestException as e:
        yield f"[Error connecting to Ollama API: {e}]"
