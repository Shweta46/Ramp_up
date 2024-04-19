import numpy as np

# Broadcasting
a = np.array([1, 2, 3])
b = 2
c = a + b
print(c)

matrix = np.array([[1, 2, 3], [4, 5, 6]])
row_vector = np.array([1, 2, 3])
result = matrix + row_vector
print(result)

# matrix operations

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = a - b
print(result)

result = np.dot(a, b)
print(result)

result = np.divide(a, b)
print(result)

# Set operations
a = np.array([1, 2, 3, 4, 5])
b = np.array([3, 4, 5, 6, 7])

# intersection of two matrices
result = np.intersect1d(a, b)
print(result)

# union of the arrays
result = np.union1d(a, b)
print(result)

# difference
result = np.setdiff1d(a, b)
print(result)

# Numpy Vectorization:
# It is different from broadcasting as in broadcasting, the dimensions of the arrays is different

result = a * b
print(result)

# addition

result = a+b
print(result)

result = a/b
print(result)

result = a**2
print(result)
try:
    with open('this.txt', 'r') as file:
        a = file.read()
        if a is '':
            raise ValueError("The file is empty")
except ValueError as e:
    print("Error:", e)
