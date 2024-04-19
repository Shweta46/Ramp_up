import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

zeros_arr = np.zeros((2, 3))
print(zeros_arr)

ones_arr = np.ones((2, 4))
print(ones_arr)

# Creating array within a range:
arr_range = np.arange(0, 10, 2)
print(arr_range)

# Create arrays with a specified number of evenly spaced values
arr_linspace = np.linspace(0,10,3)
print(arr_linspace)

# Create arrays with random values
rand_arr = np.random.rand(3, 2) # random values in [0, 1)
print(rand_arr)

randn_arr = np.random.randn(2, 2) # values taken from a normal distribution
print(randn_arr)

# Creating array from existing list
data = [1, 2]
arr = np.array(data)
print(type(arr))