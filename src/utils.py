import json


def file_read():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data_json = file.read()
        data = json.loads(data_json)
    return data


operations = file_read()
print(operations[1])
