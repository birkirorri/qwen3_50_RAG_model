# Local RAG Model

A simple local RAG chatbot that answers questions about Markdown files in `docs/`. It uses [Ollama](https://ollama.com) to run the models, so everything stays on your machine.

## Setup

Requires [Ollama](https://ollama.com) and [uv](https://docs.astral.sh/uv/).

```bash
ollama pull nomic-embed-text
ollama pull qwen3:4b-instruct
```

## Usage

Make sure Ollama is running, then start the chatbot:

```bash
uv run rag.py
```

Ask questions about the documents in `docs/`. The sample `docs/handbook.md` is a fictional employee handbook.