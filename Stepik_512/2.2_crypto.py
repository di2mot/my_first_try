
from simplecrypt import decrypt, DecryptionException


with open("encrypted.bin", "rb") as inp:
    encrypted_file = inp.read()

with open("passwords.txt", "r") as pw:
    for password in pw:
        try:
            dt_text = decrypt(password.strip(), encrypted_file).decode('utf8')
            print(dt_text)
            break
        except DecryptionException:
            print("Wrong password: {}".format(password))
