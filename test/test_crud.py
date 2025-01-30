from crud import read_all, read_item, create, delete, update, avg_price,count_category, avg_rating, max_stock, low_stock, reviews, reviews_rating, count_tags

# print(read_all())
# print(read_item(1))

new_product = {
    "title": "Nuevo Item",
    "description": "New description",
    "category" : "beauty",
    "price": 20
}

update_product = {
    "id" : 29,
    "title": "Nuevo Item",
    "description": "New description",
    "category" : "beauty",
    "price": 20
}


print(read_all())

print(create(new_product))

print(read_all())


print(update(update_product))
print(read_all())

print(delete(30))

print(read_all())

print(avg_price())
print(count_category("beauty"))


# Functions Original Products
print("Functions Original Products")
print(count_tags())
print(avg_rating())
print(max_stock())
print(low_stock(2))
print(reviews("Liam Garcia"))
print(reviews_rating("Liam Garcia"))


