import os
def cls():
    os.system('cls' if os.name=="nt" else 'clear')

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    return a / b

calculate ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

def calculator():
    cls()
    print("Welcome to The Calculator")
    repeat = True
    a=float(input("What is the first number? "))
    while repeat:
        for i in calculate:
            print(i)
            
        operation = input("Pick an operation: ")

        b=float(input("What is the second number? "))

        result=calculate[operation](a,b)
        print(f"{a} {operation} {b} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result} or type 'n' to start a new calculation: ")

        if choice == "y":
            a = result
        else:
            repeat = False
            cls()
            calculator()
        

calculator()