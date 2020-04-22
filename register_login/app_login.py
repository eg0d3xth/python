import base64
import sys
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

login_prov = input('login: ')
login = login_prov.encode()

db_num = open('names.db', 'r')
lines = db_num.readlines()

db_pass = open('database.db', 'r')
lines_db = db_pass.readlines()

line_num = 0

for line in lines:
        if line != login_prov + '\n':
            line_num = line_num + 1
        elif line == login_prov + '\n':
            line_num = line_num + 1
            login_prov_line = line_num

line_checked = 0
try:
    for line in lines_db:
        line_checked = line_checked + 1
        if line_checked == login_prov_line:
            hash_ = line
except:
    print('user doesn\'t exists')
    input('press enter to exit')
    sys.exit()

hash_enc = hash_.encode()

password_prov = input('password: ')
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

try:
    hash_login = f.decrypt(hash_enc)
    hash_login_dec = hash_login.decode()
    print('Success!')
except:
    print('Wrong Password!')
    input('press enter to exit')
    sys.exit()
