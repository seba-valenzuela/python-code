def repeatedString(s, n):
    # Write your code here
    # 1. create the fullString
    fullString=''
    i=0
    while i <= n:
        fullString + s[i%len(s)]
        i+= 1
    print(fullString)
    
    # 2. iterate through the characters of fullString, counting every 'a'
    x=0
    count_a = 0
    while x < len(fullString):
        if fullString[x] == 'a':
            count_a+=1
            x+=1
    return count_a