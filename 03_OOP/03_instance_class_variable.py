class Dog:

    species = 'Canine'

    def __init__(self, name):
        self.name = name
        self.species='new Dog'

dog1 = Dog("Rockey")
print(dog1.species)
print(Dog.species)