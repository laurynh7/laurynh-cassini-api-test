import requests
import json

base_url = "https://reqres.in/api"

def read_json(file_path):
    try:
        data = json.load(open(file_path))
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except json.decoder.JSONDecodeError:
        raise Exception("File must be in valid JSON format and must not be empty")
    else:
        return data

def test_register_successful():
    register_url = base_url + "/register"
    login_information = read_json("test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['register'])
    assert response.status_code == 200


def test_login_successful():
    register_url = base_url + "/login"
    login_information = read_json("test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['login'])
    assert response.status_code == 200

