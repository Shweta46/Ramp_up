import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
result = np.dot(a, b)
print(result)

# Matrix decomposition:
u, s, v = np.linalg.svd(a)
print(u)

t = np.transpose(a)
print(t)

eignenvalues, eigenvectors = np.linalg.eig(a)
print(eigenvectors)
print(eignenvalues)

inverse_a = np.linalg.inv(a)
print(inverse_a)

# NUMPY HISTOGRAM

import matplotlib.pyplot as plt

data = np.random.randn(1000)
plt.hist(data, bins=10)
