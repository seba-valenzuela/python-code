# this will print 0 through 4:
for i in range(5):
    print(i)

print()

# this will print 1 though 4:
for i in range(1, 5):
    print(i)

print()

# this will print the numbers in a single line
array = []
for i in range(5):
    array.append(i)
print('Here is your array, with range(5): ')
print(*array) # <-- single line!

print()

# Single line for loop
new_array = []
print(new_array.append(i) for i in range(3))
