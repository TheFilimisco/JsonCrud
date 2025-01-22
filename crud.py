from database import read_db

DATA_PATH = "../data/products_simplify.json"
DATA = read_db(DATA_PATH,"products")

def read_all():
    return list(DATA.values())

def read_item(item_id):
    #TODO:
    if item_id not in DATA:
        raise KeyError("id not found")
    return DATA[item_id]

def create(item):
    add_id ={"id":len(DATA.keys())+1}
    add_id.update(item)
    DATA[len(DATA.keys())+1] = add_id
    return DATA[len(DATA.keys())]
    # if item in DATA:
    #     raise KeyError("This item exist!")
    # else:
    #     return DATA[item]
    # item has no id
    # add new item
    #assign a id
    #DATA[new_id] item

def delete(id):
    DATA.pop(id)
    return print("Successful")

def update(item):
    id = item["id"]
    if id not in DATA:
        raise KeyError("id not found")
    DATA[id] = item
    return DATA[id]



