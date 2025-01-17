# F[N] FIBONACCI NUMBER
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))

print(f"F[{num}]: {fibonacci(num)}")
