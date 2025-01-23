
import  json

from utils import simplify

with open("../data/product.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)
dict = {"name":"Steven",
        "age":19}
d = {}

d["id"] = 1

print(d)
print(dict["name"])

#Value defect if you need
print(dict.get("email",0))
print(data["dimensions"]["width"])

