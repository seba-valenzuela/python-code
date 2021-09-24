# Floor Division and Modulus
minutes = 135
hours = minutes // 60
print(hours,"\n")

remainder = minutes % 60 #the Modulus operator returns the remainder
print(remainder,"\n")         #you can also use the % operator to see if a number is dividible by another

x = 5
y = 6


# Boolean Expressions
print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y,"\n")

# Logical Operators

a = 1
b = 2
c = 3
d = 6

outcome1 = (c%2 == 0) or (d%2 == 0)
print(outcome1,"\n")

outcome2 = (b%2 == 0) and (d%2 == 0)
print(outcome2,"\n")

outcome3 = not (a>b)
print(outcome3,"\n")

# Conditional Execution

if a > 0:
    print("'a' is greater than zero","\n")
    pass    # Think of "pass" as a placeholder - it does nothing

# Alternative Execution

if a > 0:
    print("First conditional statement","\n")
else:
    print("Else statement executed","\n")

# Chained Conditionals

if a < 0:
    print("First Conditional")
elif b < 0:
    print("Second Conditional")
else:
    print("Third Conditional","\n")

# Nested Conditionals

if a == b:
    print("'a' is equal to 'b'")
else:           # Avoid Nested Cond. when possible - they are difficult to read!
    if a+b == 4:
        print("these two vars = 4")
    else:
        print("these two vars do NOT equal 4","\n")

                # Instead, use Logical Operators (and, or, not) - easier to read

# Recursion - "When a function calls ITSELF"

def countdown(n):
    if n <= 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)
countdown(5)
print()

s = "Hello"

def do_2(t, n):
    if n <= 0:
        exit
    else:
        t(n)

do_2(countdown(3), 2)
