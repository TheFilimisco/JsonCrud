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
    # item has no id
    # add new item
    #assign a id
    #DATA[new_id] item


    pass
def delete(id):
    pass
def update(item):
    pass



