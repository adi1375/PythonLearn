# Task 7: Write a Python program that finds and prints the largest element in an array list.

from array import *
import numpy as np

integer_array = array("i", [])

n = int(input("Enter number of elements: "))

print(f"Enter {n} numbers:")
for i in range(n):
    integer_array.append(int(input()))

integer_array = np.array(integer_array)
print(f"The current array is: {integer_array}")

max = integer_array[0]

for i in range(n):
    if max < integer_array[i]:
        max = integer_array[i]

print(f"The largest element is {max}.")
