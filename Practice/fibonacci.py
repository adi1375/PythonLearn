# FIBONACCI SERIES UPTO NTH TERM
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


num = int(input("Enter the number of terms for fibonacci series: "))

if num == 0:
    print("Incorrect input.")
else:
    for i in range(0, num):
        print(fibonacci(i), end=" ")
