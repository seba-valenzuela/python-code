
# 's' is the original string, 'n' is the number of chars in the final product
def repeatedString(s, n):
    # Write your code here
    # 1. create the fullString
    fullString=''
    # 1a. Count the number of times you iterate through the full string, then add that to fullString:
    fullString += (s*(n // len(s)))

    # 1b. If there is a remainder, Add the remaining letters to fullString
    if (n % len(s)) != 0: # if there IS a remainder, add it
        modulo = n % len(s)
        print(modulo)
        fullString += s[:(n % len(s))] # add (remainder amount) of chars from the beginning of the string to fullString
    
    # OLD solution: this would give a memory error when n = a HUGE number
    # i=0
    # if len(s) == 1:
    #     fullString += (s * n)
    # else:
    #     while i < n:
    #         fullString += s[i%len(s)] # If you don't use the "=", you won't ASSIGN anything to the variable
    #         i+= 1

    print(fullString)
    print(len(fullString))
    
    # 2. iterate through the characters of fullString, counting every 'a'
    
    count_a = fullString.count('a') # easier way of doing the below
    # x=0
    # while x < len(fullString):
    #     if fullString[x] == 'a':
    #         print('found an a')
    #         count_a+=1
    #     x+=1 # Watch out: this "while INCREMENTOR" needs to be OUTSIDE the if statement

    return count_a

my_string = 'banana'
num = 10

print(repeatedString(my_string, num))

one_char = 'a'
bigNum = 1000000000000

# print(repeatedString(one_char, bigNum))
