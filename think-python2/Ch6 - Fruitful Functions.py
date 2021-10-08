# Fruitful Functions are functions which RETURN something (instead of, for example, just printing to the console)
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

# Functions can return Booleans too:

def true_orFalse(a,b):
    if a >= b:
        return True
    else:
        return False

def is_dividible(x,y):
    return x % y == 0

# Exercise:

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

# Use the built-in function "isinstance(n, int)" to check whether a variable is of a certain type or not

# 3 possibilities if a function is not working:
#   1. something is wrong with the arguments its getting (precondition violated)
#   2. something is wrong with the function (postcondition violated)
#   3. something is wrong with the return value or the way its being used

# "Dead Code" - part of a program that can never run, often because it appears after the return statement

# "Scaffolding" - code that is used during program development, but not intended to be part of the final program