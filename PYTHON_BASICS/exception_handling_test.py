# create a custom exception class
class EndCurrentTask(Exception):
    pass

class main():
    
    while True:
        print()
        print("     Welcome to the input menu!")
        user_input = input("        Please input an integer: ")

        try:
            user_input = int(user_input)
        except TypeError:
            raise EndCurrentTask("Raising a Type Error")
        except ValueError:
            raise EndCurrentTask("Raising a Value Error")
        else:
            print(" Your number, plus 10, is:", str(user_input + 10))

if __name__ == '__main__':
    main()