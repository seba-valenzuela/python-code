# Exercise 3.1
def right_justify(input):
    length = len(input)
    spaces = 70 - (length)
    print((" "*spaces)+input)
right_justify('seba')

# Exercise 3.2
def do_twice(func, arg):
    func(arg)
    func(arg)

def print_twice(arg):
    print(arg)
    print(arg)

def do_four(func, arg):
    do_twice(func, arg)
    do_twice(func, arg)



do_twice(print, 'spam') # 'print' gets converted into a function, with 'spam' as the arg

print()

do_four(print, 'spam') # this passes function and arg to print_twice, TWICE!


# Exercise 3.3
def make_row(arg, num):
    print('+' + ((arg + '+') * num))

def make_columns(num):
    print('|' + ((' ' * len(row) + '|') * num) )

row = " - - - - "

# Set the desired number of rows & columns:
num_row_col = 5


def make_grid_section():    
    make_row(row, num_row_col)
    make_columns(num_row_col)
    make_columns(num_row_col)
    make_columns(num_row_col)
    make_columns(num_row_col)

for x in range(num_row_col):
    make_grid_section()

make_row(row, num_row_col)