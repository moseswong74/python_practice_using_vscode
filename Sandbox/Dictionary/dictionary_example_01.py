dictionary = {"a":1, "b":2}

def someFunction(a,b):
    print(a+b)
    return

# these do the same thing:
someFunction(**dictionary)
someFunction(a=1,b=2)