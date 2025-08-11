#EXERCISES
"""Q1 Create two dimensional 3×3 array and perform ndim, shape, slicing operation on it."""

import numpy as np
arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f"Dimensions: {arr.ndim}")
print(f"Shape: {arr.shape}")
print("Slicing")
print(f"first element of first row: {arr[0,0]}")
print(f"second and third element of second row: {arr[1,1:3]}")
print(f"first two elements of first and third row: {arr[[0,0,2,2],[0,1,0,1]].reshape(2,2)}")

"""Q2 Create one dimensional array and perform ndim, shape, reshape operation on it."""

import numpy as np
arr=np.array([1,2,3,4,5,6,7,8,9])
print(f"Dimension: {arr.ndim}")
print(f"Shape: {arr.shape}")
reshaped_array=arr.reshape(3,3)
print(f"Original array: {arr}")
print(f"Reshaped array: {reshaped_array}")