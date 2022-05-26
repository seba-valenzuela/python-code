# Objective: Iterate through each type

# Set
my_set = {1, 2, 2, 3, 4, 4, 5}
for i in my_set:
    print(i)

print("...Next...")

# Tuple
my_tuple = (1, 2, 2, 3, 4, 4, 5)
for i in my_tuple:
    print(i)

print("...Next...")

# List
my_list = [1, 2, 2, 3, 4, 4, 5]
for i in my_list:
    print(i)

print("...Next...")

# Dictionary
my_dict = {"name":"Watson", "age":8, "color":"black & white"}
for key,value in my_dict.items():
    print("My {} is {}.".format(key,value))
print()