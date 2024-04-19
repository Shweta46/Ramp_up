import numpy as np
# Boolean indexing

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
mask = arr > 3
print(mask)
print(arr[mask])

mask = (arr > 2) & (arr < 7)
print(mask)
filtered_arr = arr[mask]
print(filtered_arr)

# Fancy indexing: Like masking
arr = np.array([1, 2, 3, 4, 5])

indices = np.array([0, 2, 4]) # creating an array of indices
print(arr[indices])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
row_indices = np.array([0, 1, 2])
col_indices = np.array([0, 1, 2])
print(arr[row_indices, col_indices])
