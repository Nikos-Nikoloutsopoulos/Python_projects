alphabet = "abcdefghijklmnopqrstuvwxyz"

message=input("Enter a message: ")

key = int(input("Enter a shift value: "))

message=message.lower()
new_message =""

for char in message:
    if char.isalpha():
        index = alphabet.find(char)
        new_index=(index+key) % 26
        char=alphabet[new_index]
    new_message += char
print(new_message)


init_meesage=""  
    
for char in new_message:
    if char.isalpha():
        index= alphabet.find(char)
        init_meesage += alphabet[index-key]
    else:
        init_meesage += char

print(init_meesage)

