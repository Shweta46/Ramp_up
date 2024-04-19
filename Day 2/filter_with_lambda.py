
'''
Filter function with lambda:
It returns an iterator that contains only the elements for which the function returns True.
filter(lambda arguments: expression, iterable)
'''
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

names = ['Alice', 'Bob', 'Anna', 'Michael', 'Alex']
start_with_a = list(filter(lambda x: x[0] == 'A', names))
print(start_with_a)