import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print('Element at (1, 2):', arr[1, 2])

# Array slicing
print('First row:', arr[0, :])

# array[row_start:row_stop:row_step, col_start:col_stop:col_step]
print('Second column:', arr[:, 1])

# Another way of indexing
index = np.array([1, 2])
print('Index:', arr[index])

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
index = np.array([2, 1])
print('Index:', arr[index])

print(arr[:, -1])

# Mask: making array out of elements which are greater than 3
mask = arr > 3
print(arr[mask])

# Replacing even numbers of the array with 0
mask = arr % 2 == 0
print(mask)
arr[mask] = 0
print(arr)

total_sum = np.sum(arr)
print('Sum of all elements:', total_sum)

row_sums = np.sum(arr, axis=1)
print(row_sums)

column_sums = np.sum(arr, axis=0)
print(column_sums)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

product_ = np.prod(arr, axis=1)
print(product_)

# Reshaping of array

arr2d = arr.reshape(1, 9)
print(arr2d)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
arr2 = arr.reshape(2, 4, 2)
print(arr2)