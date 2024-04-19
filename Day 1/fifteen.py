
def prime_or_not(d):
    l = int(d**0.5)
    print(l)
    i = 1
    for i in range(2, l+ 1):
        if d % i == 0:
            print('No, its not prime')
            return 0
    print('Yes, it is prime')
    return 1

print(prime_or_not(2))
