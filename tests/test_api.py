import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.database import get_db
from app.models import Trigger

client = TestClient(app)


# Test: Create a new trigger
def test_create_trigger():
    response = client.post(
        "/api/triggers/",
        json={
            "name": "Test Trigger",
            "trigger_type": "scheduled",
            "schedule_time": "2024-12-14T10:00:00",
            "interval_seconds": 600,
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Trigger"
    assert data["trigger_type"] == "scheduled"


# Test: Get all triggers
def test_get_all_triggers():
    response = client.get("/api/triggers/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)


# Test: Update a trigger
def test_update_trigger():
    response = client.put(
        "/api/triggers/1",
        json={
            "name": "Updated Trigger",
            "trigger_type": "api",
            "api_payload": {"key": "value"},
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Trigger"


# Test: Delete a trigger
def test_delete_trigger():
    response = client.delete("/api/triggers/1")
    assert response.status_code == 204


# Test: Log an event
def test_log_event():
    response = client.post(
        "/api/events/log",
        json={"trigger_id": 1, "event_type": "manual", "payload": {"key": "test"}},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["event_type"] == "manual"
