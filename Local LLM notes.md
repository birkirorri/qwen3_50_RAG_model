
Enviorment used: Ollama

To install a model: 
- ollama pull nomic-embed-text
- ollama pull qwen3:4b-instruct

To run a model: 
- ollama run qwen3:4b-instruct

To see the list of models: 
- `ollama list`


## Working in python: 

- Worked in cursor
- Installed UV 

Til að runna eih: 

`uv run rag.py`



Gerði: 
`uv init .`
og síðan: 
`uv add requests numpy`



Vectors: 

Take our chunks and turn them into vectors which allows us to search the text for similarity which will then allow us to pass relevant chunks into the prompt. 
