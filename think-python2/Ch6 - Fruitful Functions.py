# Fruitful Functions are functions which RETURN something.
# Think of a function that ends with a return statement:

def area(radius):
    a = math.pi * radius**2
    return a # THIS makes it fruitful

# example function

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1

print(compare(1,1))

# Incremental Development: work on a program in small bits, testing along the way. 
# Its helpful if you know the answer to the calculation you're making.