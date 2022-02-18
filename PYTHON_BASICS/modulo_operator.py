# Modulo Operator returns the REMAINDER of a division problem!

# Example: I have 10 THINGS, I group them in groups of 3:
print(10 % 3) # My REMAINDER is 1
print()


# It allows you to iterate through a loop of ITEMS (numbers, chars in a string, etc.)

# 1. Working With INTEGERS:

# The number on the right stays constant while the others increment
# the number AFTER the % is the RANGE of the loop
# loop always starts at 0
# The HIGHEST number in this loop will be: RANGE-1

print(0 % 4) # 0
print(1 % 4) # 1
print(2 % 4) # 2
print(3 % 4) # 3
print(4 % 4) # 0
print(5 % 4) # 1
print(6 % 4) # 2
print(7 % 4) # 3
print()

# Lets try this the other way around...

# print(4 % 0) # 0 can't divide by 0
print(4 % 1) # 0
print(4 % 2) # 0
print(4 % 3) # 1
print(4 % 4) # 0
print(4 % 5) # 4
print(4 % 6) # 4
print(4 % 7) # 4
print(4 % 8) # 4
print(4 % 9) # 4
print(4 % 10) # 4
print(4 % 11) # 4
#wack

print()

# 2. Working with characters in a STRING:

# Since modulo includes '0' in it, this works nicely when refering to indices in a string...

i = 0
name = 'seba'
print(name[i%len(name)])
i += 1
print(name[i%len(name)])
i += 1
print(name[i%len(name)])
i += 1
print(name[i%len(name)])
i += 1
print(name[i%len(name)])
i += 1
print()

# ...OR indeces in an ARRAY, LIST:

x = 0
my_list = ['j', 'o', 's', 'e']
print(my_list[x%len(my_list)])
x += 1
print(my_list[x%len(my_list)])
x += 1
print(my_list[x%len(my_list)])
x += 1
print(my_list[x%len(my_list)])
x += 1
print(my_list[x%len(my_list)])
x += 1

print()

# Testing with 1 letter:

y = 0
name = 'c'
print(name[y%len(name)])
y += 1
print(y)
print(name[y%len(name)])
y += 1
print(y)
print(name[y%len(name)])
y += 1
print(y)
print(name[y%len(name)])