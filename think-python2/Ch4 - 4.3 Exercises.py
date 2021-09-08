import turtle
import math
seba = turtle.Turtle()

def square(t, length):
    for i in range(4):
        seba.fd(length)
        seba.lt(90)

def polygon(t, length, n):
    for i in range(n):
        seba.fd(length)
        seba.lt(360/n)

def circle(t, r):
    circumference =  2 * math.pi * r
    n = int(circumference / 3) + 3
    length = circumference / n
    polygon(t, length, n)

def polyline(t, r, angle):
    arc_length =  2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

# square(seba, 350)

# polygon(seba, 50, 13)

# circle(seba, 100)

