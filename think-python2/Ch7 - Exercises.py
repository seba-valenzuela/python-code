# Exercise 7.1 - Given a number, return an estimate of the square root

import sys
import math

def collect_input():

    input_data = []
    print()
    user_input = input("Input an integer to find the square root, or type 'exit': ")

    while user_input != "exit":
        input_data.append(user_input)
        user_input = input("Input additional integer, or type 'exit': ")
        

    # print(input_data) # scaffolding for testing

    # print menu
    print()
    print ("{:<4} {:<14} {:<14} {:<14}".format('a','mysqrt(a)','math.sqrt(a)','diff'))
    print ("{:<4} {:<14} {:<14} {:<14}".format('-','---------','------------','----'))

    return input_data


# Provide a parameter, "a", and return the square root of "a"
def my_sqrt(a):

    # FIX THIS: input of "1" gives error: "ZeroDivisionError: float division by zero"...
    # line 34, in my_sqrt
    #   y = (x + a/x) / 2

    # The initial guess for the square root will be HALF of 'a' (rounded down)
    x = int(a/2)

    while True:
        y = (x + a/x) / 2
        if abs(y-x) < sys.float_info.epsilon: # epsilon is 0.0000001
            return x   # if the difference between y and x is less than epsilon, return x
        x = y

# collect_input()


def test_square_root():
    
    # data to be printed goes here
    data = collect_input()

    # Using a FOR LOOP, extract elements of the data list one at a time to perform operations
    for element in data:
        
        # instantiate variable holders
        mysqrt_value = my_sqrt(float(element))
        mathSqrt_value = math.sqrt(float(element))

        # Move this to AFTER the calculations
        diff = mysqrt_value - mathSqrt_value

        # FIRST: print the 'a' value
        # SECOND: print mysqrt(a) value
        # THIRD: print math.sqrt(a) value
        # FOURTH: print the difference between the previous 2
        print ("{:<4} {:<14} {:<14} {:<14}".format(float(element),round(mysqrt_value,11),round(mathSqrt_value,11),diff))

    # scaffolding - REMOVE later
    return data

print(test_square_root())