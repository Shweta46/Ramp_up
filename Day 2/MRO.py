class A:
    def method(self):
        print('A method')

class B:
    def method(self):
        print('B method')

class C(A):
    def method(self):
        print('C method')

class D(B, C):
    pass

d = D()
d.method()

# MRO:Method Resolution Order
# Determines which method implementation to use
# MRO for D = [D, B, C, A]