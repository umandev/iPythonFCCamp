import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

usr_pwd = input("Enter your password :")
pwd = usr_pwd.encode()

mysalt = b'M\xb5Q\x8f\x14\x02s\xef+\x97\x91\xf7\xd2a\xce'

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256,
    length=32,
    salt=mysalt,
    iterations=100000,
    backend=default_backend()

)

key = base64.urlsafe_b64decode(kdf.derive(pwd))

print(key)



