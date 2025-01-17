# Exercise 3: Summing Along Axes
# Task: Use the following array for this exercise:
# arr = np.array([[1, 2, 3],
#                 [4, 5, 6],
#                 [7, 8, 9]])
# Questions:
# Calculate the sum of elements along the rows.
# Calculate the sum of elements along the columns.
# What are the results, and what do they represent?


import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(f"2D Array: \n{array_2d}")
print(f"Sum of all elements along the rows: {np.sum(array_2d,axis=1)}")
print(f"Sum of all elements along the columns: {np.sum(array_2d,axis=0)}")
