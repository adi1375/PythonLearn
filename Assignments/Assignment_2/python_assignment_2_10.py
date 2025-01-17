# Task 10: Write a Python program that checks whether a number is prime or not using a loop and conditional statements.

num = int(input("Enter a positive integer: "))

count = 0
if num == 1:
    print(f"{num} is neither prime nor composite.")
else:
    for i in range(2, num + 1):
        if num % i == 0:
            count += 1
    if count == 1:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
