import  json

from utils import simplify

with open("data/products.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

#print(data["name"])
#print(type(data))
#print(data["hobbies"][1])
#Acces to Json
#print(data["friends"][1]["hobbies"][0])

def info(data):
    print(type(data))
    print(data)
    print(len(data))
    print(len(data["products"]))
    print(len(data["products"][0]))
    print(data.keys())

info(data)

data_simp = simplify(data, None, None)

info(data_simp)

