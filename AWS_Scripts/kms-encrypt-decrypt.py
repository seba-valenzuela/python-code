import boto3
import sys
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

    # Extract just the plaintext key
    plaintext_key = data_key['Plaintext']

    # Extract just the Cyphertext Key
    cyphertext_key = data_key['CiphertextBlob']

    # The plaintext file to be encrypted - REFERENCE A FILE
    secret = ''

    # plaintext_key decoded to base64
    plaintext_key_base64 = ''

    # cyphertext_key decoded to base64
    cyphertext_key_base64 = ''

    # decrypted cyphertext_key
    decrypted_ciphertext_key = ''

    print('\nThe plaintext, before encryption: \n')
    print(secret+'\n')
    print('The encrypted plaintext: \n')
    
    # TO DO:
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
