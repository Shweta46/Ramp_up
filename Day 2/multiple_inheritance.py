class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print('B method')

class C(A, B):
    def something(self):
        print('I have inherited both the classes above')

    def method(self):
        super().method()
        pass

c = C()
c.something()
c.method()