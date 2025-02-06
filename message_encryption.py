# This program encrypts and decrypts an input message using a key value

alphabet = "abcdefghijklmnopqrstuvwxyz"

message=input("Enter a message: ")

key = int(input("Enter a shift value: "))

#Encryption part
message=message.lower()
encrypted_message =""

for char in message:
    if char.isalpha():
        index = alphabet.find(char)
        new_index=(index+key) % 26
        char=alphabet[new_index]
    encrypted_message += char
print(encrypted_message)

#Decryption part

init_meesage=""  
    
for char in encrypted_message:
    if char.isalpha():
        index= alphabet.find(char)
        init_meesage += alphabet[index-key]
    else:
        init_meesage += char

print(init_meesage)

