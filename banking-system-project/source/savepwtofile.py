from cryptography.fernet import Fernet

fkey = input("Please input your key: ")
# key = fkey.read()
cipher = Fernet(fkey)

filename = 'secrets.pw'

with open(filename,'rb')as f:
    e_file = f.read()

encrypted_file = cipher.encrypt(e_file)

with open(filename + "encrypted",'wb') as ef:
    ef.write(encrypted_file)