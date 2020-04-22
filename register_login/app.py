import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

x=0
while x==0:
    login_prov = input('create login: ')
    login = login_prov.encode()
    
    check = open('names.db', 'r')
    lines = check.readlines()
    check.close()
    for line in lines:
        if line == login_prov + '\n':
            print('user allready exists')
            x=0
        else:
            x=1

password_prov = input('create password: ')
password = password_prov.encode()

salt = "YOUR SALT HERE"
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)

key = base64.urlsafe_b64encode(kdf.derive(password))

f = Fernet(key)

hash_login = f.encrypt(login)
hash_login_dec = hash_login.decode()

fl = open('database.db', 'a')
fl.write(hash_login_dec + '\n')
fl.close()

fl_name = open('names.db', 'a')
fl_name.write(login_prov + '\n')
fl_name.close()
