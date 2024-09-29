from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all_users():
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json() == [
        {"name": "Myroslav", "age": 13, "work": "student"},
        {"name": "name", "age": 14, "work": "nothing"}
    ]

def test_add_user():
    new_user = {"name": "some", "age": 22, "work": "some"}
    response = client.post("/users/add", params=new_user)
    assert response.status_code == 201
    assert response.json() == new_user

def test_add_user_exist():
    response = client.post("/users/add", params={"name": "Myroslav", "age": 13, "work": "student"})
    assert response.status_code == 400
    assert response.json()

def test_get_user_by_id():
    response = client.get("/users/0")
    assert response.status_code == 200
    assert response.json() == {"name": "Myroslav", "age": 13, "work": "student"}

def test_get_user_by_id_error():
    response = client.get("/users/10")
    assert response.status_code == 400
    assert response.json()

def test_delete_user():
    response = client.delete("/users/delete", params={"name": "name"})
    assert response.status_code == 204

def test_delete_user_error():
    response = client.delete("/users/delete", params={"name": "Unknown"})
    assert response.status_code == 400
    assert response.json()

 