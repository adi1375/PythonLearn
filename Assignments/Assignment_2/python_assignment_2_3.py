# Task 3: Write a Python program that calculates the sum of all numbers in an array list using a for loop.

from array import *

integer_array = array("i", [])

n = int(input("Enter number of elements: "))

print(f"Enter {n} numbers:")
for i in range(n):
    integer_array.append(int(input()))

sum = 0

for i in range(len(integer_array)):
    sum = sum + integer_array[i]

print(f"The sum of the numbers is {sum}")
