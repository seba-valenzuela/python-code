def jumpingOnClouds(c):
    # Write your code here
   
    index_of_lastSpace = (len(c) - 1)
    placeholder = 0
    num_of_moves = 0
    # ** We always want to advance MORE, but if not, we will advance LESS **
    while placeholder < index_of_lastSpace:
        if (placeholder+2) < (len(c)) and c[placeholder+2] == 0:
            placeholder+= 2
            num_of_moves+= 1
        else:
            placeholder+= 1
            num_of_moves+= 1
    return num_of_moves