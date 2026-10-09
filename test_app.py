
import pytest
from app import app, tasks


@pytest.fixture(autouse=True)
def reset_tasks():
    tasks.clear()
    yield
    tasks.clear()


@pytest.fixture
def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_home(client):
    assert client.get("/").status_code == 200


def test_add_task(client):
    response = client.post(
        "/tasks", json={"title": "Study Agile"}
    )
    assert response.status_code == 201
    assert response.json["title"] == "Study Agile"


def test_reject_empty_task(client):
    response = client.post("/tasks", json={"title": " "})
    assert response.status_code == 400


def test_complete_task(client):
    response = client.post(
        "/tasks", json={"title": "Write tests"}
    )
    task_id = response.json["id"]

    response = client.post(f"/tasks/{task_id}/complete")
    assert response.status_code == 200
    assert response.json["done"] is True


def test_delete_task(client):
    response = client.post(
        "/tasks", json={"title": "Temporary"}
    )
    task_id = response.json["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert client.get("/tasks").json == []


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"
