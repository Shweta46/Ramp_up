from functools import reduce

# reduce(lambda arguments: expression, iterable)

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(product)

'''
When reduce() is called with lambda x, y: x * y and the list [1, 2, 3, 4, 5], here's how it works:

The lambda function lambda x, y: x * y takes two arguments x and y and returns their product. This function will be applied to pairs of elements in the list.

In the first step, reduce() passes the first two elements of the list to the lambda function: 1 and 2. The lambda function computes 1 * 2 = 2, and reduce() replaces 1 and 2 in the list with 2, so the list becomes [2, 3, 4, 5].
In the second step, reduce() passes the next element of the modified list (2) and the next element after it (3) to the lambda function. The lambda function computes 2 * 3 = 6, and reduce() replaces 2 and 3 in the list with 6, so the list becomes [6, 4, 5].
This process continues until all elements in the list have been processed. The final result is the product of all elements: 1 * 2 * 3 * 4 * 5 = 120.
'''

numbers = [3, 6, 8, 2, 4, 9, 1, 5]
maximum = reduce(lambda x, y: x if(x > y) else y, numbers)
print(maximum)

# Sort
# sorted(iterable, key=lambda x: sort_criteria)

data = [(1, 'Alice'), (3, 'Charlie'), (2, 'Bob')]
sorted_data = sorted(data, key=lambda x:x[1])
print(sorted_data)

# sort the function out based on their length
words = ['apple', 'banana', 'orange', 'kiwi']
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)
