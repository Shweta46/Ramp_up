import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Logical operations
add_ = arr1 + arr2
print(add_)

mul_ = arr1 * arr2
print(mul_)

two = arr1*2
print(two)

result = arr1 | arr2
print(result)

result = ~arr1
print(result)

# Array functions
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([1, 2, 4, 4])
compare_results = arr1 == arr2
any_result = np.any(compare_results)
print(any_result)

all_result = np.all(compare_results)
print(all_result)

result = arr1 ^ arr2
print(result)

# Math functions:
arr = np.array([1, 4, 9, 16, 25])
sqrt_arr = np.sqrt(arr)
print(sqrt_arr)

exp_arr = np.exp(arr)
print(exp_arr)

log_arr = np.log(arr)
print(log_arr)

log10_arr = np.log10(arr)
print(log10_arr)

sin_arr = np.sin(arr)
print(sin_arr)

arctan_arr = np.arctan(arr)
print(arctan_arr)

# Numpy constants:
pi_value = np.pi
print(pi_value)

e_value = np.e
print(e_value)

infinity_value = np.inf
print(infinity_value)

nan_value = np.nan
print(nan_value)

# Statistical functions

mean = np.mean(arr)
print(mean)

median = np.median(arr)
print(median)

std_dev = np.std(arr)
print(std_dev)

variance = np.var(arr)
print(variance)

# String functions
arr = np.array(['Hello', 'World', 'NumPy'])
capitalized = np.char.capitalize(arr)
print(capitalized)

joined = np.char.join('-', arr)
print(joined)

replaced = np.char.replace(arr, 'o', 'O')
print(replaced)

add_a_character = np.char.add(arr, '!p')
print(add_a_character)

split = np.char.split(arr, 'o')
print(split)

lowercase = np.char.lower(arr)
print(lowercase)


