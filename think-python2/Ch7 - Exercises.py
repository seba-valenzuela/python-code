# Exercise 7.1 - Given a number, return an estimate of the square root

import sys

def start_here():

    input_data = []
    print()
    user_input = input("Input an integer to find the square root: ")

    while user_input != "exit":
        input_data.append(user_input)
        user_input = input("Input another integer, or type 'exit': ")
        

    print(input_data) # scaffolding for testing

    # print menu
    print ("{:<4} {:<14} {:<14} {:<14}".format('a','mysqrt(a)','math.sqrt(a)','diff'))
    print ("{:<4} {:<14} {:<14} {:<14}".format('-','---------','------------','----'))

# Provide a parameter, "a", and return the square root of "a"
def my_sqrt(a):

    # data to be printed goes here
    data = []

    x = 0 # dummy variable

    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y-x) < sys.float_info.epsilon: # epsilon is 0.0000001
            break   # if the difference between y and x is less than epsilon, break
        x = y

start_here()