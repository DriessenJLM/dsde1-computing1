def merge_dictionaries(dictionary1, dictionary2):
    dictionary3 = dictionary1.copy()
    dictionary3.update(dictionary2)
    return dictionary3
print(merge_dictionaries({"name":"jasper", "sex":"male", "age":18},{"make":"ford", "model":"Mustang"}))