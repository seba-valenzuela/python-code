# Imagine a circle of the Alphabet
# you want to count the number of moves (step-wise) from one letter to the next

list = [1, 2, 3, 4, 5]

# Start from 1st number, count to a certain number
# return the number of moves
def count_NOloop(end):

    count = 0
    for item in list:
        if item == end:
            break
        else:
            count += 1
    return print('\ntotal moves: ' + str(count) + '\n')

count_NOloop(3)
