class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("The sound that this animal makes.")
        pass

class Dog(Animal):
    def speak(self):
        return 'Woof' # overridden method
    def extend_(self):
        print('This is extended method i.e., a method not present in the parent class')

my_dog = Dog('Rob')

print(my_dog.speak())
print(my_dog.name)
my_dog.extend_()