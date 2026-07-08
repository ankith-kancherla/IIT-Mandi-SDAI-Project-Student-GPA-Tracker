import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_add_student():
    response = client.post("/students", json={
        "name": "Rahul Sharma",
        "subject": "Mathematics",
        "grades": [85, 90, 78, 92]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Rahul Sharma"
    assert data["gpa"] == 86.25

def test_get_all_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_student_by_id():
    # First add a student
    client.post("/students", json={
        "name": "Priya Singh",
        "subject": "Physics",
        "grades": [70, 80, 90]
    })
    response = client.get("/students/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Rahul Sharma"

def test_get_student_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404

def test_delete_student():
    # Add a student first
    post_res = client.post("/students", json={
        "name": "Test Student",
        "subject": "Chemistry",
        "grades": [60, 70]
    })
    student_id = post_res.json()["id"]
    delete_res = client.delete(f"/students/{student_id}")
    assert delete_res.status_code == 200
    assert "deleted successfully" in delete_res.json()["message"]