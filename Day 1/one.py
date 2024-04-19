
def square():
    dict1 = {}
    for i in range(1, 6):
        dict1[i] = i**2
    return dict1

def square2():
    dict1 = {x: x**2 for x in range(1, 6)}
    return dict1
print(square2())

