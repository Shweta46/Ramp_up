sum_three = (lambda x, y, z: x+y+z)
print(sum_three(3, 4, 5))

concatenate = (lambda x, y: x+y)
print(concatenate('hello!', 'there'))

larger_one = (lambda x, y: x if x>y else y)
print(larger_one(9, 10))

repeat_me = (lambda x, y: x*3)
print(repeat_me('Me!', 3))

