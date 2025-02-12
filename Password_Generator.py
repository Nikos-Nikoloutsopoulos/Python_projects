import random
import string

min_length =12
max_length =20

password_lenght= random.randint(min_length, max_length)

password=""

for char in range(password_lenght):
    password+=random.choice(string.ascii_letters)

print(f"The created password is: {password}")