# PASSWORD GENERATION USING STRINGS
#####################################################
# import random
# letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
# numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+" ]
#
# print("Welcome to Python Password Generator")
# no_of_letters = int(input("How many letters you want in your password? "))
# no_of_numbers = int(input("How many numbers you want in your password?"))
# no_of_symbols = int(input("How many symbols you want in your password?"))
#
# password = ""
#
# for char in range(0, no_of_letters):
#     password += random.choice(letters)
# for char in range(0, no_of_numbers):
#     password += random.choice(numbers)
# for char in range(0, no_of_symbols):
#     password += random.choice(symbols)
#
# random.shuffle(password)
# print(f"Your generated password is\n{password}")
####################################################################################

# GENERATING A PASSWORD USING A LIST
import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+" ]

print("Welcome to Python Password Generator")
no_of_letters = int(input("How many letters you want in your password? "))
no_of_numbers = int(input("How many numbers you want in your password?"))
no_of_symbols = int(input("How many symbols you want in your password?"))

password = []

for char in range(0, no_of_letters):
    password.append(random.choice(letters))
for char in range(0, no_of_numbers):
    password.append(random.choice(numbers))
for char in range(0, no_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)
password = "".join(password)
print(f"Your generated password is\n{password}")
