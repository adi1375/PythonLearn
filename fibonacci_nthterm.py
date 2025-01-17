# NTH TERM FIBONACCI NUMBER
def fibonacci(n):
    if n == 0:
        print("Incorrect input.")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter a number: "))

print(f"{num}th fibonacci term: {fibonacci(num)}")
