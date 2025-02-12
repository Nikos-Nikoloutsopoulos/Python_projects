import random
import string

min_length =12
max_length =20
# Randomly check the password length
password_lenght= random.randint(min_length, max_length)

password=""
#According to length add characters to password
for char in range(password_lenght):
    password+=random.choice(string.ascii_letters)

#print the generated password
print(f"The created password is: {password}")