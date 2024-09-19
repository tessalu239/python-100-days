import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# # Easy version
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_easy=""
for time in range(1, nr_letters+1):
    password_easy+=random.choice(letters)
for time in range(1, nr_symbols+1):
    password_easy+=random.choice(symbols)
for time in range(1, nr_numbers+1):
    password_easy+=random.choice(numbers)

print(f"Easy version {password_easy}")

# Hard version

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_hard=[]
for time in range (1, nr_letters+1):
    password_hard.append(random.choice(letters))
for time in range (1, nr_symbols+1):
    password_hard.append(random.choice(symbols))
for time in range(1, nr_numbers+1):
    password_hard.append(random.choice(numbers))

final=""

# Using either random method .shuffle() or manually by loop number of time from 1 to length of password-> char === random choice of the password. add char to final. pop the char out using index password.pop(password.index(char))
# for time in range (1, len(password_hard)):
#     char=random.choice(password_hard)
#     final+=char
#     password_hard.pop(password_hard.index(char))
random.shuffle(password_hard)
for char in password_hard:
    final+=char
print(final)