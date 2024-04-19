import numpy as np

arr = np.array([[1, 3, 4], [1,2,3], [4, 67, 8]])
print(arr.shape)

arr1 = np.zeros(5)
print(arr1)

arr2 = np.array([[1, 2, 3], [1, 2, 4]])
print(arr2.shape)

arr = np.array([1, 2, 3, 4], dtype='int64')
print(arr.dtype)

# Array attributes:
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('Shape', arr.shape)
print('Size', arr.size)
print('Data type', arr.dtype)
print('Dimension of the array:', arr.ndim)
print('Size of each element of array:', arr.itemsize)
print(arr.strides)
print(arr.base)
print(arr.flags)
print(arr.itemsize)
print("Array's own memory location:", arr.__array_interface__['data'][0])

