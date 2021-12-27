import boto3
import sys
import base64
# pip install cryptography
from cryptography.fernet import Fernet
# for pretty printing
from pprint import pprint

# create main method
def main(argv):

    # create a session to retrieve 'admin' credentials from ~/.aws/credentials
    # session is a class, you're creating a class called "session"
    session = boto3.Session(profile_name='admin')

    # create a client with KMS
    # client is a method, because you're acting on session
    kms = session.client('kms', region_name='us-east-1')

    # generate a temporary encryption/data key
    data_key = kms.generate_data_key(
        KeyId='arn:aws:kms:us-east-1:186570641799:key/e19aa50f-b781-4c9c-a739-61efd9b7982e',
        KeySpec='AES_256',
    )

    # Extract just the plaintext key (Note: it comes encoded in base64)
    plaintext_key = base64.b64encode(data_key['Plaintext'])

    # Extract just the Cyphertext Key (Note: it comes encoded in base64)
    cyphertext_key = data_key['CiphertextBlob']

    # Print the plaintext file to the console
    file = open("secret_4encryption.txt", "r")
    secret = file.read()
    print('\nThe plaintext, before encryption: \n')
    print(secret+'\n')

    # # plaintext_key decoded from base64
    # plaintext_key_base64 = base64.b64decode(plaintext_key)

    # # cyphertext_key decoded from base64
    # cyphertext_key_base64 = base64.b64decode(cyphertext_key)

    # Overwrite the old file with an encrypted version of the file
    plaintext_key_fernet = Fernet(plaintext_key)
    with open("secret_4encryption.txt", "w") as encrypted_secret:
        encrypted_secret.write(plaintext_key_fernet.encrypt(secret))

    # print the encrypted version of the file
    print('The encrypted plaintext: \n')
    print(encrypted_secret+'\n')

    # Discard the plaintext key
    plaintext_key = ''
    plaintext_key_fernet = ''

    # decrypt the cyphertext_key with KMS call
    response = kms.decrypt(CiphertextBlob=cyphertext_key)
    decrypted_ciphertext_key = base64.b64encode((response['Plaintext']))

    # use decrypted cyphertext key to decrypt encrypted message
    cyphertext_key_fernet = Fernet(decrypted_ciphertext_key)
    decrypted_file_contents = cyphertext_key_fernet.decrypt(encrypted_secret)

    # Write a new file, add contents, and print to console
    decrypted_file = open("decrypted_secret.rtf", "w")
    decrypted_file.write(decrypted_file_contents)
    print(decrypted_file.read())

    
    
    # Steps for Encrypt/Decrypt of a text file:
    # 1. Create a plaintext_secret.txt file and save its contents to 'secret' variable
    # 2. Decode 'plaintext_key' using base64, save result to 'plaintext_key_base64'
    # 3. Decode 'cyphertext_key' using base64, save result to 'cyphertext_key_base64'
    # 4. Use the 'plaintext_key_base64' to encrypt the secrets FILE (install/use openSSL) and save an ENCRYPTED file version
    # 5. Print contents of ENCRYPTED secrets file
    # 6. Delete (zero-out) the 'plaintext_key_base64', 'plaintext_key', and secrets file
    # 7. Call aws kms decrypt to decrypt the encrypted 'cyphertext_key_base64' and save that to 'decrypted_ciphertext_key'
    # 8. Decode 'decrypted_ciphertext_key' using base64, save it to 'plaintext_key_base64'
    # 9. Decrypt the ENCRYPTED secrets file using 'decrypted_ciphertext_key' and save to file secrets_decrypted.txt
    # 10. Print contents of secrets_decrypted.txt


# Execute this code only if you're running this program stand-alone,
# so don't run it if its being used as part of another program
if __name__ == "__main__":
    # Call the "main" function, pass all the command line arguments in order
    main(sys.argv[1:])
