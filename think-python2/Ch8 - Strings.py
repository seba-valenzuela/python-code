# Chapter 8 - Strings

# remember that computer scientists count from 0
# so the word 'word' has characters from 0 to 3

# To access a string's character, use brackets

word = 'word'
character = word[0] #this is the letter 'w'
print(character)

# to access letters from the end, use NEGATIVE INDICES

character = word[-1] # this is the letter 'd'
print(character)
print()

# Here are 3 ways of printing the same char:
print(word[0])
print(word[-4])
print(word[-len(word)])
print()

# A TRAVERSAL is a pattern when you process each character one at a time

# Exercise in section 8.3 - display string chars backwards

word = 'backwards'
index = -len(word)

while index < 0:
    print(word[-index-1])
    index = index + 1

print()
# You can print letters of a word with a For Loop:

for chars in word:
    print(chars)

print()
# Exercise in section 8.3 - fix For Loop

prefixes = 'JKLMNOPQ'
suffix = 'ack'

for letter in prefixes:
    if letter == 'O' or letter == 'Q':
        print(letter+'uack')
    else:
        print(letter+suffix)

print()

# A segment of a string is called a SLICE
print(word[0:4]) # this prints the first 4 letters of backwards. Note the 4 at the end!
print(word[:4]) # this prints the first 4 letters from the BEGINNING
print(word[2:]) # this prints from the END, OMITTING the first 2 letters
print(word[:]) # this prints the whole word

# Strings are IMMUTABLE - meaning you can't change alter them
# word[0] = 'T' <-- Error!
# but you can replace a string variable with another value
# or create a new variable with parts of the old:

new_word = 'Squid' + word[4:] # take everything BUT omit the 1st letter, add 'T' in front
print(new_word)
print()

# 8.6 Exercise - add 'index' to 'find' parameters

def find(word, letter, index):
    i = index   # Specifying the index at which the program starts looking
    while i < len(word):    # So if you start at index 2 for the word 'star',
        if word[i] == letter:   # the program will only search the letters 'a' and 'r'.
            return i
        i = i + 1
    return -1

print(find('can','a',2))
print()

# 8.7 Exercises

# this counts the number of times a letter appears
def count(word,letter):
    count = 0
    for letter in word:
        if letter == 'a':
            count+= 1
    return count

print(count('banana','a'))
print()

# This counts the number of times a letter appears starting at a certain index
def count2(word, letter, index):
    find(word, letter, index)


# 8.8 String Methods

word = 'word'
print(word)
print(word.upper())
print()

name = 'barbara'    # 'find' method is flawed
print(name.find('ar'))  # here it returns 1
print()

banana = 'banana'
print(banana.find('na')) # here it returns 2
print() # So maybe it looks for CONSECUTIVE results
# find can also take arguments that indicate where to start and stop (index)

# 8.9 - the 'in' operator

def in_both(word1, word2): # this compares the 1st word ONTO the 2nd
    for letter in word1:
        if letter in word2:
            print(letter)

in_both('carlos','sebastian')
print()

# 8.10 - String Comparison

# An example of how Python puts Capital letters before lowercase
if 'Cucumber' < banana:
    print('The word, ' + banana + ', comes after Cucumber.')
    print()

# 8.11 - Fix this function

def is_reverse(word1,word2):
    if len(word1) != len(word2):
        return False
    
    i = 0
    j = len(word2) - 1 # correction 1: the reverse index is length - 1

    while j >= 0: # correction 2: if J never equals 0, it will never get to the 1st letter
        print(i,j)
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

is_reverse('stop','pots')
print()