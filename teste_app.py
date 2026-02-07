import pytest
import requests

# CRUD

BASE_URL = "http://127.0.0.1:5000"
snack = []
    
def test_create_snack():
    new_snack_data = {
            "id": "new_id",
            "name": "new_name",
            "description": "new_description",
            "date": "new_date",
            "time": "new_time",
            "in_diet": "new_in_diet"
        }
    
    response = requests.post(f"{BASE_URL}/snack", json=new_snack_data)
    assert response.status_code == 201

def test_get_snacks():
    response = requests.get(f"{BASE_URL}/snack")
    assert response.status_code == 200

def test_get_snack():
    if snack:
        snack_id = snack[0]
        response = requests.get(f"{BASE_URL}/snack/{snack_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert snack_id == response_json["id"]

def test_update_snack():
    if snack:
        snack_id = snack[0]
        payload = {
            "id": "new_id",
            "name": "new_name",
            "description": "new_description",
            "date": "new_date",
            "time": "new_time",
            "in_diet": "new_in_diet"
        }
        response = requests.put(f"{BASE_URL}/snack/{snack_id}", json=payload)
        assert response.status_code == 200
        response_json = response.json()


def test_delete_task():
    if snack:
        snack_id = snack[0]
        response = requests.delete(f"{BASE_URL}/snack/{snack_id}")
        response.status_code == 200

        response = requests.delete(f"{BASE_URL}/tasks/{snack_id}")
        assert response.status_code == 404
            