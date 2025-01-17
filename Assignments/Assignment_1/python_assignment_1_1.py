# 1. Create a program that asks the user for their name, age, and height, and then prints a message with this information.

name = input("Enter your name: ")
age = input("Enter your age: ")
height = input("Enter your height in cm: ")

print(f'Hello {name}! You are {age} year{('' if age == 1 else 's')} old and your height is {height} centimeters.')


