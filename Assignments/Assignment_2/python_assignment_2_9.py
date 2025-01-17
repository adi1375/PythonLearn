# Task 9: Write a Python program that counts the number of times a particular element occurs in an array list using a loop.

from array import *

integer_array = array("i", [])

n = int(input("Enter number of elements: "))

print(f"Enter {n} numbers:")
for i in range(n):
    integer_array.append(int(input()))

x = int(input("Enter the number to be searched: "))

count = 0
for i in range(n):
    if x == integer_array[i]:
        count += 1

print(f"{x} occurs {count} times.")
