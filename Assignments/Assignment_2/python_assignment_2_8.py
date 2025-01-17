# Task 8: Write a Python program that calculates the factorial of a given number using a for loop.
num = int(input("Enter a positive number: "))

factorial_num = 1

for i in range(1, num + 1):
    factorial_num *= i

print(f"The factorial of {num} is {factorial_num}.")
