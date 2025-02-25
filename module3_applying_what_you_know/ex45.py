import random

class Person(object):

    def __init__(self, name, age, eyes, hit_point, job):
        self.name = name
        self.age = age
        self.eyes = eyes
        self.hit_point = hit_point
        self.job = job
    
    def talk(self, words):
        print(f"I am {self.name} and {words}")

    def hit(self, target):
        damage = random.randint(5, 15)
        print(f"{self.name} hits {target.name} for {damage} damage!")
        target.hit_point -= damage
        if target.hit_point <= 0:
            print(f"{target.name} has been defeated!")
        else: 
            print(f"{target.name} now has {target.hit_point} hit points.")


becky = Person("Becky", 39, "green", 20, "boxer")
benny = Person('Benny', 23, "blue", 50, "baby")
alice = Person("Alice", 28, "brown", 30, "ninja")

def fight_club(people):
    while len(people) > 1: 
        attacker = random.choice(people)
        defender = random.choice([person for person in people if person != attacker])

        attacker.hit(defender)

        if defender.hit_point <= 0:
            people.remove(defender)
            print(f"{defender.name} is out of the fight!\n")
        else: 
            print(f"{attacker.name} and {defender.name} continue fighting!\n")
        
        if len(people) == 1:
            print(f"{people[0].name} is the winner of the fight club!\n")
            break
    
people = [becky, benny, alice]
fight_club(people)

# Create 1,000 people and store them in a list
# people = [Person(f"Person{i}", i % 100 + 1, "blue") for i in range(1000)]
# people = []
# for i in range(1000):
#     people.append(Person(f"Person{i}", i, "blue"))
# for person in people[:5]:
#     print(person.name)

# print(becky.__dict__)

# the class that becky comes from
# print(becky.__class__) 

# the contents of that class
# print(becky.__class__.__dict__)

# a list of strings for everything
# print(dir(becky))

# these two do the same thing
# print(becky.talk)
# print(getattr(becky, 'talk'))

# this is the class's vesion of talk
# print(becky.__class__.__dict__['talk'])

# becky.talk("I am talking here")
