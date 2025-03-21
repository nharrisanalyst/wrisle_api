# testing command python3 -m pytest

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"endpoint": "Wrisle"}

def test_get_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"hello":"world"}