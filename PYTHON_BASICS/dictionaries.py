# Dictionaries consist of Key:Value pairs
data = {'age': '33', 'name': 'Seba', 'height': '69'}
print()

# Access just the Keys:
print(data.keys())
print()

# Print just the Keys:
print(*data.keys()) # <--- The magic asterix! *
print()

# Print just the Values:
print(*data.values()) # <--- The magic asterix! *
print()

# Lets test the integrity of keys when you remove an item...
list_of_names = {1:"jon", 2:"seba", 3:"carlos", 4:"jessica"}
print(list_of_names)
print()

# delete the 2nd item, which is key 2:
del list_of_names[2]
print(list_of_names)
print()

# try to access item with key 2:
print(list_of_names.get(2, "This is a custom error message!"))
print()

# check to see if a KEY exists in a DICTIONARY:
key = 1
if key in list_of_names.keys():
    print("This key is in data")
else:
    print("NO")

# (isinstance(key, int)) and 

# more complicated check...
if (key in list_of_names.keys()):
    print("This IS an int, and its a key in ther dictionary")
else:
    print("didn't work")

print()
print(list_of_names.keys())
print()