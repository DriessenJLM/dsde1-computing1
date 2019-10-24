def repeat_at_index(the_list, index):
    the_list.insert(index,the_list[index])
    the_list.insert(index,the_list[index])
    return the_list
print(repeat_at_index([1,2,3,4,5],3))