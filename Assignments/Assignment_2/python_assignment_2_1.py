# Task 1: Write a Python program that takes an integer input from the user and checks whether the number is even or odd using an if-else statement.

num = int(input("Enter a number:"))

if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

print(f'\n{num} is {('even.' if num % 2 == 0 else 'odd.')}')
