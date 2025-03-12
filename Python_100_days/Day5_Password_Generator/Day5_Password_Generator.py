import random

print("Welcome to the Password Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))

letters_list = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols_list = ["!", "#", "$", "%", "(", ")", "*", "+"]

# easy
# password = ""

# for i in range(letters):
#     password += random.choice(letters_list)
# for i in range(numbers):
#     password += random.choice(numbers_list)
# for i in range(symbols):
#     password += random.choice(symbols_list)

# print(password)

# hard
password_list = []

for i in range(letters):
    password_list += random.choice(letters_list)
for i in range(numbers):
    password_list += random.choice(numbers_list)
for i in range(symbols):
    password_list += random.choice(symbols_list)

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i
print(password)
