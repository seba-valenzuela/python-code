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