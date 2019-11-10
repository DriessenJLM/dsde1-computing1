def start_to_lower(string, x):
    new_string = string[0:x]
    newbe = new_string.casefold()
    final = string.replace(new_string,newbe)
    return final
print(start_to_lower("HELLO World", 5))