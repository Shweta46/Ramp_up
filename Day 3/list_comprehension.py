numbers = [(1, 2), (2, 1), (23, 23)]
numbers.sort(key=lambda x: x[1])
print(numbers)

n = [1, 2, 4, 5]
v = list(map(lambda x: x*2, n))
print(v)

lis = [i for i in range(1, 21) if i%2 == 0]
print(lis)

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_numbers = [x for x in list1 if x in list2]
print(common_numbers)

list2d = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
list1d = []
one_d = [j for i in list2d for j in i]
print(one_d)

s = "Hello world, how are you?"
first_word = [i[0] for i in s.split(' ')]
print(first_word)

tup = [(i, i**2) for i in range(1, 6)]
print(tup)

