# Task 2: Write a Python program that takes three integer inputs from the user and determines the largest number using nested if-else statements.

print("Enter 3 numbers:")
x = int(input())
y = int(input())
z = int(input())

if x > y and x > z:
    print(f"{x} is the greatest.")
elif y > z:
    print(f"{y} is the greatest.")
else:
    print(f"{z} is the greatest.")
