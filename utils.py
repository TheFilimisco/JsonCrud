
def simplify(data, field, data_filer=None):
    # light version of products
    #data[field]

     #1. for iterator the list products
     #2. for each item
     #3. modifying item for get 5 values keys (give by data_filter)
        # keys put --> create a new dict with specific attributes
    items = []
    for item in data[field]:
        new_dict = {}
        print("launch item.items()")
        print(item.items())
        for key, value in item.items():
            if key in data_filer:
                new_dict[key] = value
        if new_dict:
            items.append(new_dict)
    new_data = {field:items}
    return new_data

def simplify_users(data, field, data_filter=None):
    items_user = []
    for item in data[field]:
        new_dict = {}
        for key, value in item.items():
            if key in data_filter:
                new_dict[key] = value
        if new_dict:
            items_user.append(new_dict)
    new_data = {field:items_user}
    return new_data



def simplify2(data, field, data_filter=None):
    for item in data[field]:
        keys = list(item.keys())
        for key in keys:
            if key not in data_filter:
                del item[key]

    return data
