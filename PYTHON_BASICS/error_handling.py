# IndexError: list index out of range

# Lets pretend this list could be of varying lengths
my_list = [0, 1, 0, 0, 1, 0]

def calculator(c):
    indexOf_lastItem = len(c)-1
    index = 0
    count = 0 # count the number of moves
    while index < indexOf_lastItem: # while the current index is less than the index of the last item
        if index+2 < indexOf_lastItem and c[index+2] == 0:
            index+=2
            count+=1
        elif index+1 < indexOf_lastItem and c[index+1] == 0:
            index+=1
            count+=1
    return count

print(len(my_list))
print(calculator(my_list))