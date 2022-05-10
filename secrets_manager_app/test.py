from secrets_manager_class import secrets_manager

secretsDict = {}
counter = 0

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

while True:
    print("   ** Change the Password of the Secret **")
    ref2 = input("Enter the Ref. Number of the Secret: ")
    # if input is an integer and its a key that exists in secretsDict...
    print()
    print(ref2)
    print(type(ref2))
    print(secretsDict.keys())
    print()
    if True:
        new_pass = input("Enter your new password: ")
        object2 = secretsDict[ref2]
        object2.set_Passwd(new_pass)
        break
    elif ref2 not in secretsDict:
        print("Please enter a valid integer that refers to an existing secret.")
        print()
    else:
        print("neither of the first 2 conditions work")