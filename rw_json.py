import json


def r_json():
    try:
        with open("./list.json", 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError as err:
        return "list.json NOT FOUND"


def w_json(data: dict):
    with open("./list.json", 'w', encoding='utf-8') as file:
        return json.dump(data, file, indent=4)
