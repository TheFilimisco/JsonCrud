from typing import List, Any

from database import read_db

#Read of Simplify products
DATA_PATH = "../data/products_simplify.json"
DATA = read_db(DATA_PATH,"products")

#Read of Products Original
DATA_PATH_ORIGINAL = "../data/products.json"
DATA_ORIGINAL = read_db(DATA_PATH_ORIGINAL, "products")

#Read of Users
DATA_PATH_USERS = "../data/users.json"
DATA_USERS = read_db(DATA_PATH_USERS, "users")



#Simplify Product
def read_all() -> list:
    return list(DATA.values())

def read_item(item_id: int) -> dict:
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

def dates() -> list[str]:
    list_date = []
    for item in DATA_ORIGINAL.values():
        for rev in item["reviews"]:
            list_date.append(rev["date"])
    return list_date

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


def id_with_title() -> dict[str,str]:
    dict_title = {}
    for item in DATA_ORIGINAL.values():
        dict_title[item["id"]] = item["title"]
    return dict_title


def title_start_letter( letter: str) -> list[str]:
    list_title = []
    for item in DATA_ORIGINAL.values():
        if item["title"][0] == letter.upper():
            list_title.append(item["title"])
    return list_title


# Test Crud Users
def read_all_users() -> list:
    return list(DATA_USERS.values())

def read_user(id : int) -> dict:
    if id not in DATA_USERS:
        raise KeyError("Dont found")
    return DATA_USERS[id]

def create_user(item:dict):
    new_id = max(list(DATA_USERS.keys()))+1
    item["id"] = new_id
    DATA_USERS[new_id] = item
    return DATA_USERS[new_id]

def update_user(item:dict):
    id = item["id"]
    if id not in DATA_USERS:
        raise KeyError("This item dont  exist")
    else:
        DATA_USERS[id] = item
    return DATA_USERS[id]

def delete_user(id:int):
    return DATA_USERS.pop(id)


def get_user_role(role :str) -> list:
    list_role = []
    for item in DATA_USERS.values():
        if item["role"] == role:
            list_role.append(item["firstName"])
    return list_role

def get_color_hair(color_hair : str) -> list:
    list_color_hair = []
    for item in DATA_USERS.values():
        if item["hair"]["color"] == color_hair:
            list_color_hair.append(item["firstName"])
    return list_color_hair

def get_color_total_hair(color_hair : str) -> [str,int]:
    accum = 0
    for item in DATA_USERS.values():
        if item["hair"]["color"] == color_hair:
            accum+=1
    return color_hair,accum

