from operator import index

# Python doesn't have arrays, they instead have lists (same thing)

# Iterate through a list, as a loop

music = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

starting_index = music.index('C')
# print(starting_index)

print()
for i in range(8):
    print(music[starting_index], end='')
    starting_index -= 1
print('\n\n')

# current_note = music[music.index('C')-1]
# print(current_note)
# current_note = music[music.index(current_note)-1]
# print(current_note)

print()


# BELOW: loop that uses INDEXES

def print_scale(list, target):

    target_index = list.index(target)
    current_index = target_index

    count_LEFT = 0
    # read to the LEFT
    while current_index <= target_index:
        print(list[current_index], end='')
        current_index -= 1
        count_LEFT += 1
        if abs(current_index) == target_index: # this is the issue: abs(current_index) isn't the same letter as target_index
            break
    
    return print('\n'+str(count_LEFT))

print_scale(music, 'C')
print()

    # read to the RIGHT



# BELOW: loop that uses LETTERS

# def print_scale_descending(list, target):

#     # count the number of moves
#     num_moves = 0

#     # Set current note to the the note after root
#     current_note = list[list.index(target)-1] # returns 'B', the note before C

#     # instantiate an array with the initial note
#     scale_array = [target]

#     # loop through array, adding notes to list
#     while current_note != target:
#         scale_array.append(current_note)
#         current_note = list[list.index(current_note)-1]
#         num_moves += 1
#     scale_array.append(current_note)
#     num_moves += 1
    
#     for i in scale_array:
#         print(i, end='')
    
#     return print('\n'+str(num_moves))

# print_scale_descending(music, 'C')

