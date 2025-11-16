from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_home_payload():
    response = client.get("/")
    body = response.json()
    assert "message" in body
    assert "DevOps CI/CD" in body["message"]


def test_health_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

