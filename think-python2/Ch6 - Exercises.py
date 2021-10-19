# Exercise 6.1 - Draw a stack diagram for a function

# STACK DIAGRAM: see drawing

# Exercise 6.2 - write a function that evaluates the Ackermann function
# use "ack(3, 4)" which should be 125

def ack(m, n):
    if m == 0:
        return n+1
    if m > 0 and n == 0:
        return ack(m-1,1)
    if m > 0 and n > 0:
        return ack(m-1,ack(m,n-1))

print(ack(3,4))


# Exercise 6.3 - Palindrome checker
# See file "Ch6 - palindrome.py"


# Exercise 6.4 - "is a power of"

def is_power(a,b):
    """Determines if one number is a power of another number"""
    if a**1==b or a**0==1: #Get the trivial cases out of the way first
        return True
    return (a%b==0) and (is_power(a/b,b))

print("The answer to is_power is: "+str(is_power(1001,10)))


# Exercise 6.5 - Greatest Common Divisor

def gcd(a,b):
    if b == 0:
        return a
    r = a%b
    return gcd(b,r)

print(str(gcd(36,12)))
