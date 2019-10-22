'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
   print(a+1)
print(inc(2))


# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    return(a+1)    # hint this is incomplete
print(inc_return(2))


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    return(a+b)
print(sum(2,5))


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    return inc_return(sum(a,b))
print(sum_inc(2,5))



# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    if a % 2 == 0:
        return 'truth'
    else:
        return "false"
print(is_even(4))


# create for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    # hint: you can add strings together 
    # in order to concatenate them
    s=str()
    for XXX in range(repeat): #this is where you tell it to do it a set number of times this is through the range function
        s += phrase #this is where it keeps adding ho to the previoulst empty s variable which then starts to fill
    print(s)
print(string_repeat("ho",3))

