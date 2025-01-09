import  json

with open("data/frieda.json", mode="r", encoding="utf-8") as file:
    data = json.load(file)

print(data["name"])
print(type(data))

print(data["hobbies"][1])

#Acces to Json
print(data["friends"][1]["hobbies"][0])

