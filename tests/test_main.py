from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, CI world!"}


def test_square():
    response = client.get("/square/4")
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 4
    assert data["square"] == 16