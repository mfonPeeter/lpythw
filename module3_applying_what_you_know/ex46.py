# Animal is-a object
class Animal: 
    pass

# Dos is-a Animal
class Dog(Animal): 

    def __init__(self, name):
        # Dog has-a name
        self.name = name
        # Dog has-many tricks
        self.tricks = []

# Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        # Cat has-a name
        self.name = name

# Person is-a object
class Person:
    
    def __init__(self, name):
        # Person has-a name
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

        # Person has-many belongings (dictionary: item -> value)
        self.belongings = {}
    
# Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        # Calls the __init__() method of Person
        super(Employee, self).__init__(name)
        # python 3
        # super().__init__(name)
        # Employee has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

# Salmon is-a Fish
class Salmon(Fish):
    pass

# Halibut is-a Fish
class Halibut(Fish):
    pass

# rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a which is a Cat
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet which is a Dog
frank.pet = rover

# flipper is-a Fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()