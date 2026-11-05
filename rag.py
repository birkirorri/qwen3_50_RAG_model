import requests
import numpy as np
from pathlib import Path


OLLAMA = "http://localhost:11434"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "qwen3:4b-instruct"

# Function send a request to the embedding model
def embed(texts):
    r = requests.post(f"{OLLAMA}/api/embed", json={"model": EMBED_MODEL, "input": texts})
    return np.array(r.json()["embeddings"])

# Function to send a request to the chat model (LLM model, qwen3:4b-instruct)
def ask_llm(prompt):
    r = requests.post(f"{OLLAMA}/api/chat", json={
        "model": CHAT_MODEL, "stream":False, 
        "messages": [{"role": "user", "content": prompt}],
    })
    return r.json()["message"]["content"]

#print(ask_llm("What is the capital of France?"))

#print(embed("What is the capital of France?"))

# Step 1: Split the documents into chunks so we can search them

chunks = [] # Empty list to store the chunks
for file in Path("docs").glob("*.md"): # Loop through all the files in the docs directory
    chunks += [p.strip() for p in file.read_text(encoding="utf-8").split("\n\n") if p.strip()] # Split the text into chunks

# Step 2: Turning text into vectors so we can search the chunks

chunk_vectors = embed(chunks)
print(f"Indexed {len(chunk_vectors)} chunks\n")

# compute the similarity between the question and the chunks
# Finding the distances between the question and the chunks
def retrieve(question, k=3): # k = number of chunks to retrieve
    q = embed([question])[0]
    scores = chunk_vectors @ q / (np.linalg.norm(chunk_vectors, axis=1) * np.linalg.norm(q)) # cosine similarity
    return [chunks[i] for i in np.argsort(scores)[::-1][:k]] 

while True:
    question = input("Question: ")
    context = "\n\n".join(retrieve(question))
    #print(context)
    prompt = f"""Answer the question using ONLY the context below. 
    If the answer is not in the context, say "I don't know".

Context:
{context}

Question: {question}"""
    print("\n" + ask_llm(prompt) + "\n")
