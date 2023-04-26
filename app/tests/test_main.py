from fastapi.testclient import TestClient
from fastapi import status

from app.main import app

client = TestClient(app)


def test_root():
    resp = client.get("/")
    assert resp
    assert resp.status_code == status.HTTP_200_OK


def test_health():
    resp = client.get("/health")
    assert resp
    assert resp.status_code == status.HTTP_200_OK
