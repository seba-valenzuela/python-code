# Iteration: the ability to run a block of code repeatedly

# a note about ressigning variables - Example:

"""

a = 3
b = a   Here b is equal to 3
a = 5   Here a is reassigned to 5, but b is STILL assigned to 3!!

Instead of "b = a", use an Update, and first Initialize it:

b = 1
b = b + 2   This kind of update is called an Increment

"""

# Recreate print_n with a while loop

def print_n(s,n):
    while n > 0:
        print(s)
        n -= 1

print_n("hey",3)

# "stop when THIS happens" instead of "keep going UNTIL THAT happens"

while True:
    line = input("Type 'done' to end program: ")
    if line == 'done':
        break   # Think of "break" as breaking out of the current TAB
print(line)

