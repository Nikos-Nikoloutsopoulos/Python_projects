# This program encrypts and decrypts an input message using the Caesar Cipher method

"""
The Caesar Cipher is one of the simplest and oldest methods of encrypting messages,
named after Julius Caesar, who reportedly used it to protect his military communications. 
This technique involves shifting the letters of the alphabet by a fixed number of places.
For example, with a shift of three, the letter ‘A’ becomes ‘D’, ‘B’ becomes ‘E’, and so on. 
Despite its simplicity, the Caesar Cipher formed the groundwork for modern cryptographic techniques. 
In this article, we’ll explore how the Caesar Cipher works, its significance, 
and its impact on the development of cryptography with its advantages and disadvantages.

"""
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

