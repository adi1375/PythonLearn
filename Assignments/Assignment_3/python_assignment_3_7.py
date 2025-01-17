# Exercise 7: Manipulating Array Elements
# Task: Given the array arr = np.array([[3, 5, 7], [1, 9, 2], [8, 6, 4]]):
# Multiply every element in the array by 2.
# Subtract 5 from every element in the array.
# Questions:
# What is the resulting array after each operation?
# How does NumPy handle operations applied to the entire array?

import numpy as np

arr = np.array([[3, 5, 7], [1, 9, 2], [8, 6, 4]])
print(f"Original array : \n{arr}")

array_mul = arr * 2
print(f"\nArray after multiplying by 2: \n{array_mul}")

array_sub = array_mul - 5
print(f"\nArray after subtracting by 5: \n{array_sub}")

print(
    "\nNumpy uses broadcasting to perform required mathematical operations on every element when using scalar values."
)
