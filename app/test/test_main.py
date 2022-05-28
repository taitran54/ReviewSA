from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == { "Message" : "This is a main route" }