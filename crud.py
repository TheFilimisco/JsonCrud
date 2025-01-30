from typing import List, Any

from database import read_db



#Read of Simplify products
DATA_PATH = "../data/products_simplify.json"
DATA = read_db(DATA_PATH,"products")

#Read of Products Original
DATA_PATH_ORIGINAL = "../data/products.json"
DATA_ORIGINAL = read_db(DATA_PATH_ORIGINAL, "products")



#Simplify Product
def read_all() -> list:
    return list(DATA.values())

def read_item(item_id: dict) -> dict:
    if item_id not in DATA:
        raise KeyError("id not found")
    return DATA[item_id]

def create(item: dict):
    #This Me
    #add_id ={"id": len(DATA.keys())+1}
    #add_id.update(item)
    #DATA[len(DATA.keys())+1] = add_id
    # Alberto did
    new_id = max(list(DATA.keys())) + 1
    item["id"] = len(DATA.keys()) + 1
    DATA[new_id] = item

def update(item):
    #This me
    id = item["id"]
    if id not in DATA:
        raise KeyError("id not found")
    else:
        #Print update Item
        DATA[id] = item
        return DATA[id]

def delete(id):
    #This Me
    return DATA.pop(id)
    #This alberto
    # del DATA[id]
    #return print("Successful")


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

# About the original Data

def count_tags() -> dict[str, int]:
    tag_counter = {}
    for item in DATA_ORIGINAL.values():
        for tag in item["tags"]:
            if tag in tag_counter:
                tag_counter[tag] +=1
            else:
                tag_counter[tag] =1
    return tag_counter

def avg_rating() -> list[float]:
    avgs = []
    for item in DATA_ORIGINAL.values():
        rating_avg = 0
        for review in item["reviews"]:
            rating_avg+= review["rating"]
        avgs.append(rating_avg/len(item["reviews"]))
    return avgs

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
    stocks = []
    attributes = ["title","description","category","price","stock"]
    for item in DATA_ORIGINAL.values():
        if item["stock"] < threshold:
            item_simp = {}
            for attribute in attributes:
                item_simp[attribute] = item[attribute]
            stocks.append(item_simp)
    return stocks

def reviews(reviewer_name: str) -> list[dict]:
    # return a list of reviews by reviewer
    revs = []
    for item in DATA_ORIGINAL.values():
        for review in item["reviews"]:
            if review["reviewerName"] == reviewer_name:
                revs.append(review)
    return revs

def reviews_rating(reviewer_name: str) -> float:
    # return avg review ratings
    avg = 0
    revs = reviews(reviewer_name)
    for rev in revs:
        avg += rev["rating"]
    return avg/len(revs)



