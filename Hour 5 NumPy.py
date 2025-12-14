import numpy as np

# Creating arrays
arr = np.array([1, 2, 3, 4, 5])
matrix = np.array([[1, 2], [3, 4]])

# Array operations
print(arr.shape)      # (5,) - dimensions
print(arr.mean())     # Average
print(arr.max())      # Maximum value

# Indexing & Slicing
print(arr[0])         # First element
print(arr[1:4])       # Elements 1 to 3