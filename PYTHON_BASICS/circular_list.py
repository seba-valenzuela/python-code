# HackerRank question: Circular Printer
# Assuming the shortest direction from one letter to the next, and each step takes 1 second,
# How many seconds would it take to print out a word?

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# check distance between 2 letters in an array
# return the shorter distance
def check_distance(alpha,a,b):
    # keep track of shortest distance
    distanceLeft = 0
    distanceRight = 0
    # index of start and end letters
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
            while start_letter > (end_letter-26):
                start_letter -= 1 # step through letters to the LEFT
                distanceLeft += 1 # increment distance traveled
        # else, if the start letter is GREATER in index than the end letter
        else:
            while start_letter > end_letter:
                start_letter -= 1
                distanceLeft += 1
    print('The distance to the LEFT from '+ a +' to '+ b +' is: '+str(distanceLeft))


    # Count the distance towards the RIGHT of the array
    start_letter = alpha.index(a) # reset
    
    # if the 2 letters are the same
    if end_letter == start_letter:
        distanceRight = 0
    # else, go through letters and count the distance
    else:
        # if the start letter is GREATER in index than the end letter
        if start_letter > end_letter:
            # focus on getting to a negative number
            # while the start letter is greater than or equal to the negative value of the end letter
            while start_letter < (end_letter+26):
                start_letter += 1 # step through letters to the RIGHT
                distanceRight += 1 # increment distance traveled
        # else, if the start letter is LESS in index than the end letter
        else:
            while start_letter < end_letter:
                start_letter += 1
                distanceRight += 1
    print('The distance to the RIGHT is: '+ a +' to '+ b +' is: '+str(distanceRight))

    return min(distanceLeft, distanceRight)



def count_Seconds(alpha, input):
    # split; ['S', 'E', 'B', 'A']
    letter_list = list(input)
    total_seconds = 0

    for i in range(len(letter_list)-1):
        total_seconds += check_distance(alpha, letter_list[i], letter_list[i+1])
    return total_seconds


input = 'SEBA'
print(count_Seconds(alphabet, input))
    