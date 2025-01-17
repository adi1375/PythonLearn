# Exercise 8: Challenge: Combining Operations
# Task: Given the array arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]):
# Add 10 to the first column.
# Transpose the modified array.
# Calculate the sum of all elements in the transposed array.
# Questions:
# What is the final sum?
# Explain the steps and how each operation transforms the array.

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"Original arr: \n{arr}")

arr[:, 0] += 10
print(f"\nAdding 10 to the first column: \n{arr}")

transposed_arr = np.transpose(arr)
print(f"\nAfter transposing the array: \n{transposed_arr}")

sum_all_elements = np.sum(transposed_arr)
print(f"\nThe sum of all the elements in the transposed array: {sum_all_elements}")
