import json


def test_create_user(client):
    data = {
        "first_name": "Kirill",
        "group": "4.105-1",
        "last_name": "Balaev",
        "patronymic": "Guramovich"
    }
    response = client.post("/api/users", json = data)
    print(response)
    assert response.status_code == 200
    assert response.json()["message"] == "User successfully created"
    assert response.json()["success"] == True