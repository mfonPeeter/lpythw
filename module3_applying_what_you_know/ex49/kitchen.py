from room import Room

class Kitchen(Room):

    def __init__(self):
        super().__init__('Kitchen')

    def enter(self): 
        print("Yo, you've entered the kitchen. You have two potions in front of you (Red and Blue). Drink one")
        
        choice = input('> ').lower()

        if choice == 'red':
            print("You get weaken, sleep and and wake up in the foyer")
            return 'foyer'
        elif choice == 'blue':
            print("You have strength and run out the exit")
            return 'exit'
        else: 
            print("You are taken back to the foyer")
            return 'foyer'