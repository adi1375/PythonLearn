# 2. Write a program that takes two numbers as input, performs all the basic arithmetic operations on them, and prints the results.

x = int(input("Enter the 1st integer: "))
y = int(input("Enter the 2nd integer: "))

print(
    f"Addition: x + y = {x+y}",
    f"Subtraction: x - y = {x-y}",
    f"Multiplication: x * y = {x*y}",
    f"Division: x / y = {x/y}",
    f"Modulus: x % y = {x%y}",
    sep="\n",
)
