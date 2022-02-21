alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

char_index = 2

positive = alphabet[char_index]
print(positive)

negative = alphabet[char_index-26]
print(negative)

print(alphabet[-24])
print()

letter_list = ['S', 'E', 'B', 'A']

length = len(letter_list)

for i in range(length-1):
    print(i, end='')
    print(i+1)

print()