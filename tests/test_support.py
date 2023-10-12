import json


def read_json(file_path):
    try:
        data = json.load(open(file_path))
    except FileNotFoundError:
        raise Exception(f"File not found: {file_path}")
    except json.decoder.JSONDecodeError:
        raise Exception("File must be in valid JSON format and must not be empty")
    else:
        return data


def assert_with_message(actual, expected, value_name):
    assert expected == actual, f"Expected resource {value_name} to equal: {expected}, but it was: {actual}"


def check_resource(actual, expected, categories):
    for category in categories:
        assert_with_message(expected[category], actual[category], category)
