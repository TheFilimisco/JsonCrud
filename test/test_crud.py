from crud import read_all, read_item, create, delete, update, avg_price,count_category

# print(read_all())
# print(read_item(1))

new_product = {
    "title": "Nuevo Item",
    "description": "New description",
    "category" : "beauty",
    "price": 20
}

update_product = {
    "id" : 35,
    "title": "Nuevo Item",
    "description": "New description",
    "category" : "beauty",
    "price": 20
}

# print(create(new_product))
# print(create(new_product))
# print(read_all())
# delete(31)
# print(read_all())
# print(update(update_product))
# print(read_all())

print(avg_price())

print(count_category("beauty"))


