class Animal():
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        print('Some generic animal sound.')

class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    def name_of(self):
        super().make_sound()
        print(self.name)

class Dog(Animal):
    def __init__(self, species, doggie, sound):
        super().__init__(species)
        self.doggie = doggie
        self.sound = sound

    def name_of_dog(self):
        print('Name of this doggie is' + self.doggie)

    def m1(self):
        super().make_sound()
        print('Sound is ' + self.sound)

generic_animal = Animal('Unknown')
my_cat = Cat('Felis catus', 'Whiskers')
my_dog = Dog('Dog', 'Polo', 'woof')

generic_animal.make_sound()
my_cat.name_of()
my_dog.name_of_dog()
my_dog.m1()