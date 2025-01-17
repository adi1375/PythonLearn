# Exercise 4: Broadcasting
# Task: Given a 1D array array_1d = np.array([1, 1, 1]) and a 2D array array_2d = np.array([[2, 3, 4], [5, 6, 7]]):
# Add the 1D array to each row of the 2D array using broadcasting.
# Questions:
# What is the shape of the resulting array?
# How does broadcasting simplify operations like this?

import numpy as np

array_1d = np.array([1, 1, 1])
array_2d = np.array([[2, 3, 4], [5, 6, 7]])
array_broadcast = array_1d + array_2d
print(
    f"After adding the 1D array: \n{array_1d}\nand the 2D array: \n{array_2d}\nThe new broadcaated array is: \n{array_broadcast}"
)

print(
    "Broadcasting allows us to add arrays of different sizes by automatically increasing the size of the smaller array to match the bigger array."
)
