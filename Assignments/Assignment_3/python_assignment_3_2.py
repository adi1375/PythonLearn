# Exercise 2: Slicing and Indexing
# Task: Using the array from Exercise 1, slice out the following subarrays:
# A subarray containing the first row only.
# A subarray containing the last two elements of the second row.
# Questions:
# What does arr[0, 1:3] return?
# How would you modify the array to change the value of the element at position (1, 1) to 10?

import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array: \n{array_2d}")
print(f"Subarray containing the first row only: {array_2d[0,:]}")
print(f"Subarray containing the last two elements of the second row: {array_2d[1,1:3]}")
print(
    f"arr[0,1:3] returns: {array_2d[0,1:3]}\n The last two elements from the first row i.e 2 & 3."
)
array_2d[1, 1] = 10
print(f"The new modified array : \n{array_2d}")
