'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>
def welcome_message(user_name = None, place = None):
    if user_name == None and place == None  :
        return "Hello and welcome"
    if user_name and place != None:
        return ("Hello, "+ user_name+ ', and welcome to '+place)
    elif user_name != None:
        return("Hello, " + user_name + ", and welcome")
    elif place != None:
        return("Hello and welcome to " + place)

    


# Create a function called list_average()
# without using any libraries to do the maths for you 
# (the point of this exercise is to practice interacting 
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list
def list_average(listy, avg_type = None):
    if avg_type == None:
        if len(listy) == 0:
            raise ZeroDivisionError
        else:
            return int(sum(listy)/len(listy))
    elif avg_type == "mode":
        mode1 = max(set(listy), key = listy.count)
        return mode1
    elif avg_type == "mean":
        mean1 = int(sum(listy)/len(listy))
        return mean1
    elif avg_type == "median":
        listy.sort()
        median1 = listy
        lenmed = int((len(median1))/2)
        return listy[lenmed]
print(list_average([1,2,3,4,5,6,7]))
