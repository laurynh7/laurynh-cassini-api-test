import requests

from test_support import read_json, assert_with_message

base_url = "https://reqres.in/api"


def test_register_successful():
    register_url = base_url + "/register"
    login_information = read_json("test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['register'])
    try:
        assert response.status_code == 200
    except AssertionError:
        error_output = response.json()
        raise AssertionError(f'Error occurred: {error_output["error"]}')


def test_login_successful():
    register_url = base_url + "/login"
    login_information = read_json("test_data/happy_path_data.json")
    response = requests.post(register_url, data=login_information['login'])
    try:
        assert response.status_code == 200
    except AssertionError:
        error_output = response.json()
        raise AssertionError(f'Error occurred: {error_output["error"]}')


# Test list<resource> for id "4" and corresponding values
def test_list_resource():
    list_resource_url = base_url + "/unknown"
    response = requests.get(list_resource_url)
    assert response.status_code == 200
    response_json = response.json()

    resource_list = response_json['data']
    resource_found = False
    for resource in resource_list:
        if resource['id'] == 4:
            resource_found = True
            assert_with_message(len(resource), 4, 'length')
            assert_with_message(resource['name'], 'tigerlily', 'name')
            assert_with_message(resource['year'], 2004, 'year')
            assert_with_message(resource['color'], '#E2583E', 'color')
            assert_with_message(resource['pantone_value'], '17-1456', 'pantone_value')

    assert resource_found, "No resource found with 'id' of 4"







