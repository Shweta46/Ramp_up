# my_list = [expression for item in iterable if condition]

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)
