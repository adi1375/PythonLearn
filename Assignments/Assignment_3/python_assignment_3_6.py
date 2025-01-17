# Exercise 6: Exploring a 3D Array
# Task: Create a 3D array with shape (2, 2, 3) and the following values:
# [[[1, 2, 3],
#   [4, 5, 6]],

#  [[7, 8, 9],
#   [10, 11, 12]]]
# Questions:
# Access and print the second matrix in the array.
# Slice out the first row of every matrix.
# Perform a sum along the first axis and describe the result.

import numpy as np

array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(f"3D Array: \n{array_3d}")
print(f"\nThe second matrix in the array is: \n{array_3d[1,:,:]}")
print(f"\nThe first row of every matrix: \n{array_3d[:,0,:]}")
print(
    f"Sum along the first axis: \n{np.sum(array_3d,axis=1)}\nThis adds the columns of the respective inner matrices."
)
