import turtle
import math
seba = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length):
    angle = 360 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length =  2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(t, n, step_length, step_angle)
    
    # for i in range(n):
    #     t.fd(step_length)
    #     t.lt(step_angle)

def circle(t, r):
    arc(t, r, 360)

# square(seba, 350)

# polygon(seba, 13, 50)

circle(seba, 100)

