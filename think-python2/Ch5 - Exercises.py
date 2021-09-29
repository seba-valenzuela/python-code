import time

# Exercise 5.1 - Display Time

time_now = time.time() # time since Jan 1, 1970 in SECONDS
seconds_per_hour = 60*60
seconds_per_day = 60*60*24
days = time_now // seconds_per_day

hours = time_now / seconds_per_hour

current_hour = (hours % 12) - 4
current_min = (time_now / 60) % 60
current_sec = (time_now % 60)

print("The current time is " + str(int(current_hour)) + ":" + str(int(current_min)) + ":" + str(int(current_sec)) + " P.M.")
print("There have been "+ str(int(days)) +" days since the epoch (Jan 1, 1970)")

# Exercise 5.2 - Check Fermat's Theorem
# It says that there are no positive integers a, b, and c such that
# a^n + b^n = c^n, for any values of n greater than 2

print("\n------------------------------------------\n")

def check_fermat (a, b, c, n):
    if (n > 2) and (a^n + b^n == c^n):
        print("\nHoly smokes, Fermat was wrong!\n")
    else:
        print("\nNo, that doesn't work\n")

def user_prompt():
    print("The equation is: a^n + b^n = c^n")
    a = input("Provide a value for a: ")
    b = input("Provide a value for b: ")
    c = input("Provide a value for c: ")
    n = input("Provide a value for n: ")
    check_fermat(int(a), int(b), int(c), int(n))

user_prompt()

# Exercise 5.3 - Test for Triangle

print("\n------------------------------------------\n")