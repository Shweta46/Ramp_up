
def sum_of_digits_in_a_number(d):
    n = str(d)
    l = []
    for i in n:
        l.append(i)
    print(l)
    p = 0
    for i in l:
        p += int(i)
        print(p)
    return p

print(sum_of_digits_in_a_number(12))