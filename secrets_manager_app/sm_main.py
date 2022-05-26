from sm_manager import *

# Create an Object Manager Object
oManager = Manager()

while True:
    print()
    print("   Welcome to the Secrets Manager App!")
    print("   Options:")
    print("      'n' - Create a New secret")
    print("      'p' - Change the Password of a secret")
    print("      'u' - Change the Username of a secret")
    print("      'a' - View the Age of a secret in seconds")
    print("      'v' - View the Username/Password of a secret")
    print("      'd' - Delete a Secret")
    print("      'q' - Quit")
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
    if not (action == 'n') and not oManager.secretsDict:
        print("   There are currently no secrets stored.")
        print("   Please add a secret by choosing 'n'")
        print()

    else:
        if action == 'n':  # Create a New Secret
            oManager.newSecret()

        elif action == 'v':  # View a Secret
            oManager.viewSecret()

        elif action == 'p': # Change the Password of the Secret
            oManager.changePassword()

        elif action == 'u':  # Change the Username of a secret
            oManager.changeUser()

        elif action == 'a':  # View the Age of a Secret in seconds
            oManager.viewAge()
        
        elif action == 'd': # Delete a Secret
            oManager.delSecret()


        
        