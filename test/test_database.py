import json

from database import read_db

DATA_PATH = "../data/products_simplify.json"
data = read_db(DATA_PATH,"products")

print(json.dumps(data,indent=4))
print(data)
print(len(data))
print(type(data))
