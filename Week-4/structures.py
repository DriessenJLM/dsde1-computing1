'''
structures.py

Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".
def first_and_last(the_list):
    terms = len(the_list)
    final = (terms-1)
    return the_list[0::final]
print(first_and_last([1, 2, 3, 4, 5]))



# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater then "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    if end > beginning or end > len(the_list) or beginning > len(the_list): 
        raise ValueError
    else:
        the_list.reverse()
        mylist = the_list[(-beginning): (-end)]
        return mylist
print(part_reverse([1, 2, 3, 4, 5], 4, 1)) #hint this is incomplete


# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    the_list.insert(index,the_list[index])
    the_list.insert(index,the_list[index])
    return the_list
print(repeat_at_index([1, 2, 3, 4, 5], 3))

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    import copy
    rev = copy.copy(word)
    words = word
    words = ''.join(reversed(word))
    if words == rev:
        return True
    else:
        return False
print(palindrome_word("racecar"))

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    import copy
    import string
    rev = copy.copy(sentence)
    rev = rev.casefold()
    s = rev
    s = s.replace(',', '')
    s = s.replace('.', '')
    s = s.replace('!', '')
    s = s.replace(' ', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    words = copy.copy(s)
    words = ''.join(reversed(s))
    print(words)
    if words == s:
        return True
    else:
        return False
print(palindrome_sentence("Mr. Owl ate my metal worm"))

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    first = sentence1[0]
    second = sentence1.capitalize()
    if second[0] != first:
        raise ValueError
    if sentence1[-1] == "!" or sentence1[-1] == "?" or sentence1[-1] == ".":
        pass
    else:
        raise ValueError
    third = sentence2[0]
    fourth = sentence2.capitalize()
    if fourth[0] != third:
        raise ValueError
    if sentence2[-1] == "!" or sentence2[-1] == "?" or sentence2[-1] == ".":
        return sentence1 + sentence2
    else:
        raise ValueError
print(concatenate_sentences("Hello!", "Goodbye!"))

# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    if key in dictionary:
        return True
    else:
        return False
print(index_exists({"name":"jasper", "sex":"male", "age":18}, "sex"))

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False
print(value_exists({"name":"jasper", "sex":"male", "age":18}, "male"))


# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    dictionary3 = dictionary1.copy()
    dictionary3.update(dictionary2)
    return dictionary3
print(merge_dictionaries({"name":"jasper", "sex":"male", "age":18}, {"make":"ford", "model":"Mustang"}))
