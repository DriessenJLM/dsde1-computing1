def period(L,g):
    if g == 0:
        raise ValueError
    if isinstance(L,str) is True:
        raise TypeError
    if isinstance(g,str) is True:
        raise TypeError
    import math
    twop = 2*(math.pi)
    try:
        sqt = (math.sqrt(L/g))
        return twop * sqt
    except TypeError:
        print("your input has to be numerical")
    except ValueError:
        print("the value that you have entered breaks this function")
    except ZeroDivisionError:
        print("you cant divide by zero")
print(period("help",9))