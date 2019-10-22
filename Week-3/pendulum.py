def period(L,g):
    try:
        import math
        twop = 2*(math.pi)
        sqt = (math.sqrt(L/g))
        return twop * sqt
    except TypeError:
        print("your input has to be numerical")
    except ValueError:
        print("the value that you have entered breaks this function")
    except ZeroDivisionError:
        print("you cant divide by zero")
print(period(2,9))