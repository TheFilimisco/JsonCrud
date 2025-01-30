import json

def read_db(data_path,field):
    with open(data_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    items_dict = {item["id"] : item for item in data[field]}
    return items_dict

def read_db_list(data_path,field):
    with open(data_path, mode="r", encoding="utf-8") as file:
        data = json.load(file)
    return data[field]


def save_db(data_path, data):
    pass