from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_get_existing_equipment():
    response = client.get("/equipment/P01/status")

    assert response.status_code == 200

    data = response.json()

    assert data["equipment_id"] == "P01"
    assert data["fault_code"] == "E17"


def test_unknown_equipment():
    response = client.get("/equipment/UNKNOWN/status")

    assert response.status_code == 404