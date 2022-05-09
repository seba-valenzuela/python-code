from secrets_manager_class import secrets_manager

secretsDict = {}
counter = 0
master_pass = "MASTER1"

while True:
    print()
    print("   Welcome to the Secrets Manager App!")
    print("   Options:")
    print("      'n' - Create a New secret")
    print("      'p' - Change the Password of a secret")
    print("      'u' - Change the Username of a secret")
    print("      'a' - View the Age of a secret in seconds")
    print("      'v' - View the Username/Password of a secret")
    print("      'q' - Quit")
    print()

    action = input("What would you like to do? ")
    action = action.lower() # force lowercase
    action = action[0] # select only the 1st character
    print()

    # If the user selected anything other than 'n' and there isn't any data in secretsDict...
    if not (action == 'n') and not secretsDict:
        print("   Please add something to the list by choosing 'n'")
        print()

    if action == 'n':
        print("** Create a New Secret **")
        user = input("Enter a Username for this secret: ")
        passwd = input("Enter a Password for this secret: ")
        secret0 = secrets_manager(user, passwd)
        secretsDict[counter] = secret0
        print("Your new secret has been stored. Keep this info for your records:")
        print("   Ref. Number:", counter)
        print("   User:", user)
        print("   Password:", passwd)
        print()