import requests

base_url = "https://reqres.in/api"

def test_register_successful():
    register_url = base_url + "/register"
    register_data = {"email": "eve.holt@reqres.in", "password": "pistol"}
    response = requests.post(register_url, data=register_data)
    assert response.status_code == 200


def test_login_successful():
    register_url = base_url + "/login"
    register_data = {"email": "eve.holt@reqres.in", "password": "cityslicka"}
    response = requests.post(register_url, data=register_data)
    assert response.status_code == 200


