import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys

password_provided = input('password: ')
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

hash_ = input('decrypt: ')
hash_bytes = hash_.encode()

try:
    f = Fernet(key)
    decrypted = f.decrypt(hash_bytes)
except:
    print('wrong password!')
    input('press enter to exit ')
    sys.exit()

print(decrypted)

input('press enter to exit ')
sys.exit()