from cryptography.fernet import Fernet

fkey = input("Enter your key:")
# key = fkey.read()
cipher = Fernet(fkey)

with open('secrets.pw','rb') as df:
    encrypted_data = df.read()

decrypted_file = cipher.decrypt(encrypted_data)

with open('secrets.pw','wb') as df:
    df.write(decrypted_file)