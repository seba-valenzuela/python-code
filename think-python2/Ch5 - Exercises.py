import time
import turtle

print("\n------------------------------------------\n")

# Exercise 5.1 - Display Time

time_now = time.time() # time since Jan 1, 1970 in SECONDS
seconds_per_hour = 60*60
seconds_per_day = 60*60*24
days = time_now // seconds_per_day

hours = time_now / seconds_per_hour

current_hour = (hours % 12) - 4
current_min = (time_now / 60) % 60
current_sec = (time_now % 60)

print("The current time is " + str(int(current_hour)) + ":" + str(int(current_min)) + ":" + str(int(current_sec)) + " P.M.")
print("There have been "+ str(int(days)) +" days since the epoch (Jan 1, 1970)")

print("\n------------------------------------------\n")

# Exercise 5.2 - Check Fermat's Theorem
# It says that there are no positive integers a, b, and c such that
# a^n + b^n = c^n, for any values of n greater than 2


def check_fermat (a, b, c, n):
    if (n > 2) and (a^n + b^n == c^n):
        print("\nHoly smokes, Fermat was wrong!\n")
    else:
        print("\nNo, that doesn't work\n")

def user_prompt():
    print("The equation is: a^n + b^n = c^n")
    a = input("Provide a value for a: ")
    b = input("Provide a value for b: ")
    c = input("Provide a value for c: ")
    n = input("Provide a value for n: ")
    check_fermat(int(a), int(b), int(c), int(n))

# user_prompt()

print("\n------------------------------------------\n")

# Exercise 5.3 - Test for Triangle

def is_triangle(a, b, c):
    if a > (b+c):
        print("No.")
    elif b > (c+a):
        print("No.")
    elif c > (a+b):
        print("No.")
    else:
        print("Yes!")

def check_triangle():
    a = input("Input length of triangle side 1: ")
    b = input("Input length of triangle side 2: ")
    c = input("Input length of triangle side 3: ")
    print("Calculating whether or not these sides can form a triangle... ")
    is_triangle(int(a), int(b), int(c))

# check_triangle()

print("\n------------------------------------------\n")

# Exercise 5.4 - Draw a Stack Diagram that shows the state of the program when it prints the result:

"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
"""

# STACK DIAGRAM:

"""
__main__ : 
recurse : n = 3, s = 0
recurse : n = 2, s = 2
recurse : n = 1, s = 4
recurse : n = 0, s = 5
"""

# If you called recurse(-1,0), n would continue to decrease negatively 
# and eventually display a Runtime error due to recursion

# Docstring (add this inside a function)
""" In order to use this recurse(n,s) properly, 
only use positive integers for n """

print("\n------------------------------------------\n") 


# Exercise 5.5

t = turtle.Turtle()

def koch(t, n):
    """Draws a koch curve with length n."""
    if n < 10:
        t.fd(n)
        return
    m = n/3
    koch(t, m)
    t.lt(60)
    koch(t, m)
    t.rt(120)
    koch(t, m)
    t.lt(60)
    koch(t, m)

def snowflake(t, n):
    """Draws a snowflake (a triangle with a Koch curve for each side)."""
    for i in range(3):
        koch(t, n)
        t.rt(120)

# koch(t, 100)

snowflake(t, 50)