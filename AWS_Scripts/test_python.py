import base64

# The plaintext file to be encrypted - REFERENCE A FILE
f = open("secret_4encryption.txt", "r")
secret = f.read()
secret_f = secret.encode('ascii')
secret_b = base64.b64encode(secret_f)
print(secret_b)