from secrets_manager_class import secrets_manager

secretsDict = {}
counter = 0
master_pass = "MASTER1"

while True:
    print()
    print("   Welcome to the Secrets Manager App!")
    print("   Options:")
    print("      'n' - Create a New secret") # THIS WORKS
    print("      'p' - Change the Password of a secret")
    print("      'u' - Change the Username of a secret")
    print("      'a' - View the Age of a secret in seconds") # FIX BUGS
    print("      'v' - View the Username/Password of a secret") # THIS WORKS
    print("      'q' - Quit") # FIX BUGS
    print()

    action = input("   What would you like to do? ")
    action = action.lower() # force lowercase
    action = action[0] # select only the 1st character
    print()

    # If you type 'q', break out of the While loop
    if action == 'q':
                print("** Exiting Secrets Manager App **")
                print()
                break

    # If the user selected anything other than 'n' and there isn't any data in secretsDict...
    if not (action == 'n') and not secretsDict:
        print("   There are currently no secrets stored.")
        print("   Please add a secret by choosing 'n'")
        print()

    else:
        if action == 'n':  # DONE
            print("   ** Create a New Secret **")
            user = input("Enter a Username for this secret: ")
            passwd = input("Enter a Password for this secret: ")
            secret0 = secrets_manager(user, passwd)
            secretsDict[counter] = secret0
            print()
            print("Your new secret has been stored. Keep this info for your records:")
            print("   Ref. Number:", counter)
            print("   User:", user)
            print("   Password:", passwd)
            print()
            counter += 1

        elif action == 'v':  # DONE
            while True:
                print("   ** View a Secret **")
                # The INPUT has to be an integer! Otherwise the if conditions won't work
                ref = int(input("Enter the Ref. Number of the Secret: "))
                # if input is an integer and its a key that exists in secretsDict...
                if (isinstance(ref, int)) and (ref in secretsDict.keys()):
                    object = secretsDict[ref]
                    object.view(ref)
                    break
                else:
                    print("Please enter a valid integer that refers to an existing secret.")
                    print()

        elif action == 'p': # DONE
            while True:
                print("   ** Change the Password of the Secret **")
                ref2 = int(input("Enter the Ref. Number of the Secret: "))
                # if input is an integer and its a key that exists in secretsDict...
                if (isinstance(ref2, int)) and (ref2 in secretsDict.keys()):
                    new_pass = input("Enter your new password: ")
                    object2 = secretsDict[ref2]
                    object2.set_Passwd(new_pass)
                    break
                elif ref2 not in secretsDict.keys():
                    print("Please enter a valid integer that refers to an existing secret.")
                    print()

        elif action == 'u':  # DONE
            while True:
                print("   ** Change the Username of a secret **")
                ref3 = int(input("Enter the Ref. Number of the Secret: "))
                # if input is an integer and its a key that exists in secretsDict...
                if (isinstance(ref3, int)) and (ref3 in secretsDict.keys()):
                    new_user = input("Enter your new username: ")
                    object3 = secretsDict[ref3]
                    object3.set_User(new_user)
                    break
                else:
                    print("Please enter a valid integer that refers to an existing secret.")
                    print()

        elif action == 'a':  # DONE
            while True:
                print("   ** View the Age of a Secret in seconds **")
                ref4 = int(input("Enter the Ref. Number of the Secret: "))
                # if input is an integer and its a key that exists in secretsDict...
                if (isinstance(ref4, int)) and (ref4 in secretsDict.keys()):
                    object4 = secretsDict[ref4]
                    print("This password is", object4.get_Age(), "seconds old.")
                    break
                else:
                    print("Please enter a valid integer that refers to an existing secret.")
                    print()


        
        