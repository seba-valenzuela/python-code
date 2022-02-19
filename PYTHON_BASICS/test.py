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
print()

one = 'one, '
two = 'two, '
three = 'THREE!'

print(one + two + three)
print(one.join(two))
print()

team_side = 1
team = 'barcelona'
year = 2013
url = 'https://jsonmock.hackerrank.com/api/football_matches?team' + str(team_side) + '=' + str(team) + '&year=' + str(year)
print(url)
print()

print(url + '&page=2')
