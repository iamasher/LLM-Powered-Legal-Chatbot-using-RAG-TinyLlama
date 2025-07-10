# Fine-Tuned RAG Chatbot with Streaming Responses – Amlgo Labs

This project is a Retrieval-Augmented Generation (RAG) chatbot that allows users to ask questions about legal documents (like Terms & Conditions, Privacy Policies) and receive factual, grounded answers using an open-source LLM.

It integrates semantic search (via FAISS + MiniLM embeddings) and a lightweight local LLM (TinyLlama via Ollama) into a real-time, streaming chatbot interface built with Streamlit.

---

## Features

- RAG Pipeline: Retriever + Generator with document grounding
- Fast, streamed responses using `TinyLlama`
- Streamlit-based chatbot UI
- FAISS vector database for similarity search
- Mixed output format: paragraphs + bullet points
- Legal context from 10,500+ word document
- Chat reset button & source transparency

---

## Setup Instructions

### 🔹 1. Clone the Repo

```bash
git clone https://github.com/iamasher/amlgo-rag-chatbot.git
cd amlgo-rag-chatbot
```

### 🔹 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 🔹 3. Install Ollama & Pull TinyLlama

[Download Ollama](https://ollama.com/download) for your OS, then run:

```bash
ollama pull tinyllama
```

### 🔹 4. Run the Model Server

```bash
ollama run tinyllama
```

### 🔹 5. Launch the Chatbot

```bash
streamlit run app.py
```

---

##  Demo

![Demo](https://github.com/iamasher/amlgo-rag-chatbot/raw/main/Demo.gif)

> _(Includes streamed response, user query, and source chunks used)_

---

## Sample Questions + Answers

Q1: What happens if the user violates the terms?  
 A:

- Account may be suspended
- Listings removed
- Legal action taken as per the user agreement

Q2: Can the company change the terms at any time?  
 A: Yes, the document explicitly states the company reserves the right to amend terms unilaterally.

Q3: Are bots allowed to access the service?  
 A: No, the agreement clearly prohibits automated tools and scraping.


---

## Model & Tools

- **LLM:** `TinyLlama` (1.1B parameters) via [Ollama](https://ollama.com)
- **Embeddings:** `all-MiniLM-L6-v2` from Sentence-Transformers
- **Vector DB:** FAISS (Facebook AI Similarity Search)
- **Frontend:** Streamlit (with token-by-token streaming)

---

## Updated Streamlit Features

- Input field for user queries
- Real-time streaming response with "Thinking..."
- Source chunks in expandable section
- Sidebar includes:
  - Model in use
  - Number of indexed chunks
  - Reset/Clear Chat functionality
- Sticky footer: _Developed by – Md Asher_

---

## Project Structure

```
├── data/             # Cleaned legal document
├── chunks/           # Text chunks for retrieval
├── vectordb/         # FAISS index
├── src/              # Generator & retriever logic
│   ├── generator.py
│   └── retriever.py
├── app.py            # Streamlit UI with streaming + formatting
├── requirements.txt
├── README.md
├── demo/             # demo GIF
└── report.pdf       
```

---

## Developed by

**Md Asher**  
 iamasher786@gmail.com  
 [github.com/iamasher](https://github.com/iamasher)

---

## License

This project is intended for evaluation by Amlgo Labs and for educational use only. Not licensed for commercial use.
