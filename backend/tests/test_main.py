from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    """Test that GET /api/health returns HTTP 200 and the expected status payload."""
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "message": "AI Engineering Work Documentation Assistant API is running",
    }


def test_unknown_route_returns_404():
    """Test that requesting an undefined route returns HTTP 404 Not Found."""
    response = client.get("/api/unknown-route")
    assert response.status_code == 404
