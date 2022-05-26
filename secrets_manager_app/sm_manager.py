from sm_accounts import *

# This is an Object Manager Object
class Manager():
    def __init__(self):
        self.secretsDict = {}
        self.counter = 0
        self.master_pass = "MASTER1" # new feature to be added later
    
    def newSecret(self):
        print("   ** Create a New Secret **")
        user = input("Enter a Username for this secret: ")
        passwd = input("Enter a Password for this secret: ")
        secret0 = secrets_manager(user, passwd)
        self.secretsDict[self.counter] = secret0
        print()
        print("Your new secret has been stored. Keep this info for your records:")
        print("   Ref. Number:", self.counter)
        print("   User:", user)
        print("   Password:", passwd)
        print()
        self.counter += 1

    def viewSecret(self):
        while True:
            print("   ** View a Secret **")
            # The INPUT has to be an integer! Otherwise the if conditions won't work
            ref = int(input("Enter the Ref. Number of the Secret: "))
            # if input is an integer and its a key that exists in secretsDict...
            if (isinstance(ref, int)) and (ref in self.secretsDict.keys()):
                object = self.secretsDict[ref]
                object.view(ref)
                break
            else:
                print("Please enter a valid integer that refers to an existing secret.")
                print()

    def changePassword(self):
        while True:
            print("   ** Change the Password of the Secret **")
            ref2 = int(input("Enter the Ref. Number of the Secret: "))
            # if input is an integer and its a key that exists in secretsDict...
            if (isinstance(ref2, int)) and (ref2 in self.secretsDict.keys()):
                new_pass = input("Enter your new password: ")
                object = self.secretsDict[ref2]
                object.set_Passwd(new_pass)
                break
            elif ref2 not in self.secretsDict.keys():
                print("Please enter a valid integer that refers to an existing secret.")
                print()

    def changeUser(self):
        while True:
            print("   ** Change the Username of a secret **")
            ref3 = int(input("Enter the Ref. Number of the Secret: "))
            # if input is an integer and its a key that exists in secretsDict...
            if (isinstance(ref3, int)) and (ref3 in self.secretsDict.keys()):
                new_user = input("Enter your new username: ")
                object = self.secretsDict[ref3]
                object.set_User(new_user)
                break
            else:
                print("Please enter a valid integer that refers to an existing secret.")
                print()

    def viewAge(self):
        while True:
            print("   ** View the Age of a Secret in seconds **")
            ref4 = int(input("Enter the Ref. Number of the Secret: "))
            # if input is an integer and its a key that exists in secretsDict...
            if (isinstance(ref4, int)) and (ref4 in self.secretsDict.keys()):
                object = self.secretsDict[ref4]
                print("This password is", object.get_Age(), "seconds old.")
                break
            else:
                print("Please enter a valid integer that refers to an existing secret.")
                print()
    
    def delSecret(self):
        while True:
            print("   ** Delete a Secret **")
            ref4 = int(input("Enter the Ref. Number of the Secret: "))
            # if input is an integer and its a key that exists in secretsDict...
            if (isinstance(ref4, int)) and (ref4 in self.secretsDict.keys()):
                object = self.secretsDict[ref4]
                print("This secret with username '" + object.user + "' has been deleted.")
                del self.secretsDict[ref4]
                break
            else:
                print("Please enter a valid integer that refers to an existing secret.")
                print()