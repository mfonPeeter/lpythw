from sys import exit 
from random import randint
from ex47_dialogue import DIALOGUE

class Scene(object): 

    def enter(self):
        print("This scene is not yet confirmed.")
        print("Subclass it and implement enter().")
        exit(1)

class Engine(object):
    def __init__(self, scene_map):
        self.scence_map = scene_map

    def play(self):
        current_scene = self.scence_map.opening_scene()
        last_scene = self.scence_map.next_scene('finished')

        while current_scene != last_scene: 
            next_scene_name = current_scene.enter()
            current_scene = self.scence_map.next_scene(next_scene_name)

            current_scene.enter()

class Death(Scene):

    quips = [
        "You died. You kinda suck at this.",
        "Your Mom would be proud...if she were smarter.",
        "Such a luser.",
        "I have a small puppy that's better at this.",
        "You're worse than your Dad's jokes."
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips) - 1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print(DIALOGUE["CentralCorridor_enter"])

        action = input("> ")

        if action == "shoot!":
            print(DIALOGUE["CentralCorridor_shoot"])
            return 'death'

        elif action == "dodge!":
            print(DIALOGUE["CentralCorridor_dodge"])
            return 'death'
        
        elif action == "tell a joke":
            print(DIALOGUE["CentralCorridor_joke"])
            return 'laser_weapon_armory'
        
        else: 
            print("DOES NOT COMPUTE!")
            return 'central_corridor'
        
class LaserWeaponArmory(Scene):
    
    def enter(self):
        print(DIALOGUE["LaserWeaponArmory_enter"])

        code = f"{randint(1, 9)}{randint(1, 9)}{randint(1, 9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print('BZZZZEDDD!')
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code: 
            print(DIALOGUE["LaserWeaponArmory_guess"])
            return 'the_bridge'
        else: 
            print(DIALOGUE["LaserWeaponArmory_fail"])
            return 'death'
        
class TheBridge(Scene):

    def enter(self): 
        print(DIALOGUE["TheBridge_enter"])

        action = input("> ")

        if action == "throw the bomb":
            print(DIALOGUE["TheBridge_throw_bomb"])
            return 'death'
        
        elif action == "slowly place the bomb":
            print(DIALOGUE["TheBridge_place_bomb"])
            return 'escape_pod'
    
        else: 
            print('DOES NOT COMPUTE!')
            return "the_bridge"
        
class EsacapePod(Scene):

    def enter(self):
        print(DIALOGUE["EscapePod_enter"])

        good_pod = randint(1, 5)
        guess = input("[pod #]> ")

        if int(guess) != good_pod:
            print(DIALOGUE["EscapePod_death"]).format(guess=guess)
            return 'death'
        else: 
            print(DIALOGUE["EscapePod_escape"]).format(guess=guess)
            return 'finished'
        
class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'
    
class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EsacapePod(),
        'death': Death(),
        'finished': Finished(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()