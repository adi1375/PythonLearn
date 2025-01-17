# Exercise 5: Transpose of a 2D Array
# Task: Take the following 2D array:
# array = np.array([[1, 2, 3],
#                   [4, 5, 6]])
# Questions:
# Find the transpose of this array.
# Compare the original and transposed arrays. How do their shapes differ?

import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Original array: \n{array}")

transposed_array = np.transpose(array)
print(f"Transposed array: \n{transposed_array}")

print(
    f"Shape of original array: {array.shape}\nShape of transposed array: {transposed_array.shape}"
)
