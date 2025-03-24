def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a positive integer: "))

print(f"The factorial of {n} is {factorial(n)}.")
