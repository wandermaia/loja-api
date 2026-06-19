# app/main.py 
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI(title="Loja API")

Instrumentator().instrument(app).expose(app)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/produtos")
def listar_produtos():
    return [
        {"id": 1, "nome": "Teclado Mecânico", "preco": 350.00},
        {"id": 2, "nome": "Monitor 27\"", "preco": 1800.00},
    ]
