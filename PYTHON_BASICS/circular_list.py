# Imagine a circle of the Alphabet
# you want to count the number of moves (step-wise) from one letter to the next

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

input = 'SEBA'

# check distance between 2 letters in an array
def check_distance(alpha,a,b):
    # keep track of shortest distance
    distanceLeft = 0
    distanceRight = 0
    # index of letters
    start_letter = alpha.index(a)
    end_letter = alpha.index(b)

    # Count the distance towards the LEFT of the array

    # if the 2 letters are the same
    if end_letter == start_letter:
        distanceLeft = 0
    # else, go through letters and count the distance
    else:
        # if the start letter is LOWER in index than the end letter
        if start_letter < end_letter:
            # focus on getting to a negative number
            # while the start letter is greater than or equal to the negative value of the end letter
            while start_letter >= (end_letter-26):
                start_letter -= 1 # step through letters to the LEFT
                distanceLeft += 1 # increment distance traveled
        # else, if the start letter is GREATER in index than the end letter
        else:
            while start_letter >= end_letter:
                start_letter -= 1
                distanceLeft += 1
    print('The distance to the LEFT is: '+str(distanceLeft))


    # Count the distance towards the RIGHT of the array

    # if the 2 letters are the same
    if end_letter == start_letter:
        distanceRight = 0
    # else, go through letters and count the distance
    else:
        # if the start letter is GREATER in index than the end letter
        if start_letter > end_letter:
            # focus on getting to a negative number
            # while the start letter is greater than or equal to the negative value of the end letter
            while start_letter <= (end_letter+26):
                start_letter += 1 # step through letters to the RIGHT
                distanceRight += 1 # increment distance traveled
        # else, if the start letter is LESS in index than the end letter
        else:
            while start_letter <= end_letter:
                start_letter += 1
                distanceRight += 1
    print('The distance to the RIGHT is: '+str(distanceRight))

check_distance(alphabet,'C','D')


def count_Seconds(alpha, input):
    # split; ['S', 'E', 'B', 'A']
    letters = list(input)
    


    

# Start from 1st number, count to a certain number
# return the number of moves
# def count_NOloop(end):

#     count = 0
#     for item in list:
#         if item == end:
#             break
#         else:
#             count += 1
#     return print('\ntotal moves: ' + str(count) + '\n')

# count_NOloop(3)
