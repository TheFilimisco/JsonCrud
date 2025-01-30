from typing import List, Any

from database import read_db


DATA_PATH = "../data/products_simplify.json"
DATA = read_db(DATA_PATH,"products")

DATA_PATH_ORIGINAL = "../data/products.json"
DATA_ORIGINAL = read_db(DATA_PATH_ORIGINAL, "products")


def read_all() -> list:
    return list(DATA.values())

def read_item(item_id: dict) -> dict:
    if item_id not in DATA:
        raise KeyError("id not found")
    return DATA[item_id]

def create(item: dict):
    add_id ={"id": len(DATA.keys())+1}
    # new_id = max(list(DATA.keys())) + 1
    add_id.update(item)
    # item["id"] = len(DATA.keys())+1
    DATA[len(DATA.keys())+1] = add_id

    # DATA[new_id] = item

    # save
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
    # del DATA[id]
    return print("Successful")

def update(item):
    id = item["id"]
    if id not in DATA:
        raise KeyError("id not found")
    DATA[id] = item
    return DATA[id]

def avg_price():
    accum = 0
    counter = 0
    for value in DATA.values():
        counter+=1
        accum+=value["price"]
    return accum/counter

def count_category(category:str):
    counter = 0
    for item in DATA.values():
        if category == item["category"]:
            counter+=1
    return counter

# Sobre el original

def avg_rating():
    # counter = 0
    # accum = 0
    # for item in DATA_ORIGINAL.values():
    #     accum+=item["rating"]
    #     counter+=1
    # return accum/counter
    pass

def max_stock() -> tuple[int,int]:
    ident = -1
    new_max_stock = float("-inf")
    for item in DATA_ORIGINAL.values():
        if item["stock"] > new_max_stock:
            new_max_stock = item["stock"]
            ident = item["id"]
    return ident,new_max_stock


def low_stock(threshold: int) -> list[dict]:
    # items_simpl when stock <= threshold
    # return title, description, category, price, stock
    pass

def reviews(reviewer_name: str) -> list[dict]:
    # return a list of reviews by reviewer
    pass

def reviews_rating(reviewer_name: str) -> float:
    # return avg review ratings
    pass



