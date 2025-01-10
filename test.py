import  json

from setuptools.command.egg_info import write_file

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
    print(data["products"][0].keys())

info(data)

attributes = ["id","title","description","category","price"]
data_simp = simplify(data, "products", attributes)

info(data_simp)

with open("data/products_simplify.json", mode="w", encoding="utf-8") as write_file:
    json.dump(data_simp, write_file, indent=4)

