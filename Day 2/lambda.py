square = (lambda x: x**2)
print(square(2))

even_or_not = (lambda x: x%2 == 0 )
print(even_or_not(2))

sum_of_list = (lambda *x: sum(x))
print(sum_of_list(1, 2, 3))

# Using map with  lambda function:
# map(lambda arguments: expression, iterable)

numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x**2, numbers))
print(square)

c_to_f = list(map(lambda c: c * (9/5) + 32, numbers))
print(c_to_f)


