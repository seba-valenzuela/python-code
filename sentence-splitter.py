# import sys
#
# print(sys.argv[0]) # this prints the filename
# print(sys.argv[1]) # this prints the 1st argument

# for arg in sys.argv:
#     print(arg)

# print("\n <-- is there a space here?")
# input = input("\nType something: ")
#
# if 'view by' in input:
#     print("\nyeah this works.")
#     last_word = input.split() #this splits up the input into a list of words
#     print("and heres the last word you typed: ")
#     print(last_word[-1]) #this means get the last element of this list
# else:
#     "\nthis doesn't work"

exit = 0

while exit == 0: # while the user doesn't exit the program...
    print("\n Enter a command: \n")
    user_input = input()
    split = user_input.split() # this splits up the input into a list of words
    if user_input.lower() == 'exit':
        exit = 1
    elif user_input.lower() == 'view':
        print("\n**DISPLAYS THE AMOUNTS**")
    elif 'view by' in user_input.lower(): # if the string 'view by' can be found in the input...
        last_word = split[-1] # this means get the last element of this list
        print("\n**DISPLAYS THE AMOUNT BY: " + last_word.lower())
    elif len(split) == 3 and type(split[0]) == 'str' and type(split[1]) == 'str' and type(split[2]) == 'int': # if the input is formatted correctly...
        print("\n**SENDS THIS TO LOG: '{}', '{}', {}".format(split[0].lower(),split[1].lower(),split[2].lower()))
    else:
        print("^^check your syntax and try again^^")
print("\nYou've exited the program\n")
