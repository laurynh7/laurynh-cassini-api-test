import requests

from test_support import read_json, assert_with_message, check_resource

base_url = "https://reqres.in/api"


def test_register_successful():
    register_url = base_url + "/register"
    login_information = read_json("tests/test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['register'])
    try:
        assert response.status_code == 200
    except AssertionError:
        error_output = response.json()
        raise AssertionError(f'Error occurred: {error_output["error"]}')


def test_login_successful():
    register_url = base_url + "/login"
    login_information = read_json("tests/test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['login'])
    try:
        assert response.status_code == 200
    except AssertionError:
        error_output = response.json()
        raise AssertionError(f'Error occurred: {error_output["error"]}')


def test_list_resource():
    list_resource_url = base_url + "/unknown"
    expected_resource = read_json("tests/test_data/expected_resource.json")
    categories_to_check = ['name', 'year', 'color', 'pantone_value']

    response = requests.get(list_resource_url)
    assert response.status_code == 200
    response_json = response.json()

    resource_list = response_json['data']
    resource_found = False
    for resource in resource_list:
        if resource['id'] == expected_resource['id']:
            resource_found = True
            assert_with_message(len(resource), len(expected_resource), 'length')
            check_resource(resource, expected_resource, categories_to_check)

    assert resource_found, f"No resource found with id of {expected_resource['id']}"
