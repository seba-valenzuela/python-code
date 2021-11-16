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

# LEFT OFF ON 8.6 - PDF page 96