import math

A = [[1,1,1,0,0,0], [0,1,0,0,0,0], [1,1,1,0,0,0], [0,0,2,4,4,0], [0,0,0,2,0,0], [0,0,1,2,4,0]]
# 8 used to be 0 - CHANGE LATER

def add_Hourglass(array, r, c):
    # adding the letters from the explanation
    a = array[r][c]
    b = array[r][c+1]
    c = array[r][c+2]
    d = array[r+1][c+1]
    e = array[r+2][c]
    f = array[r+2][c+1]
    g = array[r+2][c+2]

    sum = a+b+c+d+e+f+g

    return sum

if __name__ == '__main__':
    array = []

    for _ in range(6):
        array.append(list(map(int, input().rstrip().split())))
    all_hourglass_sums = []
    for row in range(len(array)-2):
        for col in range(len(array)-2):
            add_up = add_Hourglass(array,col,row)
            all_hourglass_sums.append(add_up)
    print(max(all_hourglass_sums))













def OLD_solution(A): # only partially finished
    hourglass_total = 0

    # find 1st hourglass: 1st 3 col in row

    # Instantiate variables to INCrement through all possible hourglasses
    row_inc = 0
    col_inc = 0

    row_count = 0
    col_count = 0
    for row in A:
        if row_count < (row_inc + 3): # if the row is within its 3 digits
            print('**row_count is '+str(row_count) + ', and row_inc is ' + str(row_inc))
            print('\t the difference between (row_inc + 3) and row_count is: ' + str((row_inc + 3) - row_count))
            
            for col in row:
                # print(col) this would print each number in the row
                # Indicate what to calculate in each ROW
                if ((row_inc + 3) - row_count) == 3: # if we are on the 1st row of the hourglass
                    print('hourglass row 1!')
                    hourglass_total += col
                elif ((row_inc + 3) - row_count) == 2: # if we are on the 2nd row of the hourglass
                    print('hourglass row 2!')
                    hourglass_total += col
                elif ((row_inc + 3) - row_count) == 1: # if we are on the 2nd row of the hourglass
                    print('hourglass row 3!')
                    hourglass_total += col
                
                # print(col, end= ' ')
            row_count += 1
        else:
            break
    # reserve this for SHIFTING the hourglass
    row_inc += 1

    return hourglass_total


    
