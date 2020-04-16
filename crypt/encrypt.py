import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys

x = 1

while x==1: 
    messege = input('\nencrypt: ')
    messege_encoded = messege.encode()

    password_provided = input('create password: ')
    password = password_provided.encode() 

    salt = b'\x94u\xd6\x9cZ\xd2\x87\xde\x98+I\xaa&}\x1a$'

    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))

    f = Fernet(key)
    encrypted = f.encrypt(messege_encoded)
    done = str(encrypted, 'utf-8')
    print('\nDone: ' + done + '\n')

    x = 2

    answer = None
    while answer not in('y', 'n'):
        answer = input('Continue (y/n): ')
        if answer == 'y':
            x = 1
        elif answer == 'n':
            sys.exit()
        else:
            print('type y for yes or n for no\n')