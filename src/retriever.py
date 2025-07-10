# src/retriever.py

import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

# Load vector DB and metadata once
INDEX_PATH = "vectordb/index.faiss"
CHUNKS_PATH = "vectordb/chunks.json"
EMBED_MODEL = "all-MiniLM-L6-v2"

# Load sentence transformer model
model = SentenceTransformer(EMBED_MODEL)

# Load FAISS index
index = faiss.read_index(INDEX_PATH)

# Load text chunks (used as context)
with open(CHUNKS_PATH, 'r', encoding='utf-8') as f:
    chunks = json.load(f)


def get_top_k_chunks(query, k=4):
    """
    Given a query, return top-k relevant text chunks using FAISS.
    """
    # Step 1: Convert query to embedding
    query_embedding = model.encode([query])
    
    # Step 2: Search FAISS index
    distances, indices = index.search(np.array(query_embedding), k)
    
    # Step 3: Get top-k matching chunks
    top_chunks = [chunks[i] for i in indices[0]]
    
    return top_chunks
