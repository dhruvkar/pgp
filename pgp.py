import gnupg
from config import *

gpg = gnupg.GPG(gnupghome=HOME)

file_to_encrypt = raw_input("Enter in full path of the file you'd like to encrypt")

def my_public_keys(key_file):
    key_data = open(key_file).read()
    


with open(file_to_encrypt, 'rb') as f:
    status = gpg.encrypt_file(f, recipients=[MY_EMAIL], output='my_encrypted_file.gpg')

