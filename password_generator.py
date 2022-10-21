import string

import random


# You can add "string.punctuation" in characters for a stronger password:
characters = string.ascii_letters + string.digits


password = ""
password_length = random.randint(30, 30)    # The password length can be change the default is 30 length


for x in range(password_length):
    char = random.choice(characters)
    password = password + char

print(f"Your newly generated password is:        {password}")
