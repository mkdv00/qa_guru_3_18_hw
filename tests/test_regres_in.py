import requests
from pytest_voluptuous import S

from config import settings
from schemas.user_schemas import new_user_schema, user_update_schema, user_login_schema


def test_create_user():
    payload = {
        "name": "test_kudaev",
        "job": "qa"
    }

    response = requests.post(url=f"{settings.regress_in_base_url}/api/users", data=payload)

    assert response.status_code == 201, f"Incorrect status code: {response.status_code}"
    assert response.json()["name"] == "test_kudaev", f"Incorrect name: {response.json()['name']}"
    assert response.json()["job"] == "qa", f"Incorrect job: {response.json()['job']}"
    assert response.json() == S(new_user_schema)


def test_update_user():
    payload = {
        "name": "test_kudaev_updated",
        "job": "zion resident"
    }

    response = requests.put(url=f"{settings.regress_in_base_url}/api/users/2", data=payload)

    assert response.status_code == 200, f"Incorrect status code: {response.status_code}"
    assert response.json()["name"] == "test_kudaev_updated", f"Incorrect name: {response.json()['name']}"
    assert response.json()["job"] == "zion resident", f"Incorrect job: {response.json()['job']}"
    assert response.json() == S(user_update_schema)


def test_register_user_unsuccessful():
    payload = {
        "email": "test@example.com"
    }

    response = requests.post(url=f"{settings.regress_in_base_url}/api/register", data=payload)

    assert response.status_code == 400, f"Incorrect status code: {response.status_code}"
    assert response.json()["error"] == "Missing password", f"Incorrect error: {response.json()['error']}"


def test_login_user():
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url=f"{settings.regress_in_base_url}/api/login", data=payload)

    assert response.status_code == 200, f"Incorrect status code: {response.status_code}"
    assert len(response.json()['token']) == 17, f"Error in the token: {response.json()['token']}"
    assert response.json() == S(user_login_schema)


def test_delete_user():
    response = requests.delete(url=f"{settings.regress_in_base_url}/api/users/2")

    assert response.status_code == 204, f"Incorrect status code: {response.status_code}"
