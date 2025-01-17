# Exercise 1: Creating and Exploring Arrays
# Task: Create a 2D NumPy array with the following values:
# [[1, 2, 3],
#  [4, 5, 6]]
# Questions:
# What is the shape of the array?
# Access and print the element in the second row, third column.


import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array: \n{array_2d}")
print(f"The shape of the array is: {array_2d.shape}")
print(f"The element in the second row, third column is: {array_2d[1,2]}")
