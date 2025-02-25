import random

def Person_new(name, age, eyes, hit_point, job): 
    person = {
        "name": name,
        "age": age,
        "eyes": eyes,
        "hit_point": hit_point,
        "job": job
    }

    def talk(words):
        print(f"I am {person['name']} and {words}")

    
    def hit(target):
        print(target)
        damage = random.randint(5, 15) # Random damage
        print(f"{person['name']} hits {target['name']} for {damage} damage!")
        target['hit_point'] -= damage
        if target['hit_point'] <= 0:
            print(f"{target['name']} has been defeated!")
        else: 
            print(f"{target['name']} now has {target['hit_point']} hit points.")
        

    person['talk'] = talk
    person['hit'] = hit

    return person

becky = Person_new("Becky", 39, "green", 20, "boxer")
benny = Person_new('Benny', 23, "blue", 50, "baby")
alice = Person_new("Alice", 28, "brown", 30, "ninja")

# becky['talk']('I am talking here!')
# benny['talk']("I am talking too jhoor!")

def fight_club(people):
    while len(people) > 1:  # Continue until only one person is left
        attacker = random.choice(people)  # Random attacker
        defender = random.choice([person for person in people if person != attacker])  # Random defender
        
        print(attacker)
        attacker['hit'](defender)  # Make the attacker hit the defender
        
        # If defender is defeated, remove them from the fight
        if defender['hit_point'] <= 0:
            people.remove(defender)
            print(f"{defender['name']} is out of the fight!\n")
        else:
            print(f"{attacker['name']} and {defender['name']} continue fighting!\n")
        
        # If only one person is left, they win
        if len(people) == 1:
            print(f"{people[0]['name']} is the winner of the fight club!\n")
            break

people = [becky, benny, alice]
fight_club(people)