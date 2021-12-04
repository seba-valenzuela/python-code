# Examples of the String Method 'strip'

word = '    important   '

print()
print(word.strip())
print()

word = 'important'

print(word.strip('imanto')) # letters are eliminated from the outsides 
print()                     # until letters not specified are reached

print(word.replace('im','Tele'))
print()