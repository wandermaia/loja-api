# tests/unit/test_health.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_retorna_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_produtos_retorna_lista():
    response = client.get("/produtos")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_categorias_retorna_lista():
    response = client.get("/categorias")
    assert response.status_code == 200
    assert "Periféricos" in response.json()
