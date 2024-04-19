def square_root(d):
    return d ** 0.5
print(square_root(16))

def binary_to_decimal(d):
    c = [int(i) for i in str(d)]
    l = len(c)
    p = 0
    for i in range(l):
        p += c[i] * (2 ** i)
    return p
print(binary_to_decimal(1001))