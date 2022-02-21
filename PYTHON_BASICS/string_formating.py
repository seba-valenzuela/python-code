# New Line: \n
from traceback import print_tb


print("Hear \nme \nNOW!")
print()

# Tab indentation: \t
print("These \tare \twords.")
print()

# Ignore formatting: raw strings
print(r"There are 2 options: \n or \t")
print()

# Index of a string: strings can be treated like lists
name = "seba"
print(name[1])
print(len(name))
print()

# print every element in a list ON THE SAME LINE
list = [1, 2, 3, 4, 5, 6]

for i in list:
    print(i, end='') # use end='' to keep the printed item on the same line
print('\n')