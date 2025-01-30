from crud import (read_all, read_item, create, delete, update, avg_price,count_category, avg_rating, max_stock, low_stock, reviews, reviews_rating, count_tags,
dates, id_with_title,title_start_letter,read_all_users,read_user,create_user,update_user,delete_user,get_user_role,get_color_hair,get_color_total_hair)



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

print(dates())

print(max_stock())
print(low_stock(2))
print(reviews("Liam Garcia"))
print(reviews_rating("Liam Garcia"))

print("Functions For Practice")
print(id_with_title())
print(title_start_letter("a"))

print(read_all_users())
print(read_item(2))
print(read_user(1))

new_user = {
      "firstName": "Steven",
      "lastName": "UwU",
}

new_update_user = {
        "id" : 31,
      "firstName": "Steven2",
      "lastName": "UwU2",
}

print(create_user(new_user))
print(update_user(new_update_user))
print(delete_user(31))

print("Delete 31")

for item in read_all_users():
    print(item)

print(get_user_role("moderator"))

print(get_color_hair("Gray"))
print(get_color_total_hair("Gray"))








