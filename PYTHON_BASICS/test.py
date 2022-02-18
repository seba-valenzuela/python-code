s = 'banana'
n = 10

fullString=''
i=0
# while i < n:
#     fullString + s[i%len(s)]
#     i+= 1

fullString += s[i%len(s)]
i += 1
fullString += s[i%len(s)]
i += 1
fullString += s[i%len(s)]
i += 1

print(fullString)
print()

print(n // len(s))