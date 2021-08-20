def ask_for_int():
    loop = 1
    while loop == 1:
        try:
            user_int = int(input('Enter an integer: '))
        except:
            print('Not an integer.\n')
        else:
            loop = 0
    return user_int

def factorial(n):
    if n == 1:
        return 1
    elif n <= 0:
        return 0
    else:
        return (n*factorial(n-1))

def main():
    loop = 1
    while loop == 1:
        input_num = ask_for_int()
        print("%s is %d" % (input_num, factorial(input_num)))
        response = None
        while response not in ('y', 'n'):
            response = input('Do you want to loop again? ').lower()
        if response == 'y':
            loop = 1
        elif response == 'n':
            loop = 0
            print('Good bye.')
main()
