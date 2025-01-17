# Task 6: Write a Python program to reverse the elements of a array list without using the built-in reverse() function. Use a loop to achieve this.

from array import *
import numpy as np

integer_array = array("i", [])

n = int(input("Enter number of elements: "))

print(f"Enter {n} numbers:")
for i in range(n):
    integer_array.append(int(input()))

integer_array = np.array(integer_array)
print(f"The current array is: {integer_array}")

reversed_array = integer_array[::-1]

print(f"The reversed array is: {reversed_array}")
