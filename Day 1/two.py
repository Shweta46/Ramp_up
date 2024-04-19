
def least_common_mulitple(n1, n2):
    l = []
    for i in range(1, max(n1, n2) + 1):
        if(n1 % i == 0) and (n2 % i==0):
            l.append(i)
    c = 1
    for i in l:
        c *= i
    return c

print(least_common_mulitple(2, 4))

