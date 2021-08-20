print("type 2 words and an int: ")
user_input = input()
split = user_input.split()

print("the number of values = " + str(len(split)))

if split[0].isdigit() == False:
    print("1st word is a string")
else:
    print("1st Didn't work\n")

if split[1].isdigit() == False:
    print("2nd word is a string")
else:
    print("2nd Didn't work\n")

if split[2].isdigit() == True:
    print("3rd word is a int")
else:
    print("3rd Didn't work\n")
