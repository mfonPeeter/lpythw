from room import Room

class Foyer(Room):

    def __init__(self,):
        super().__init__('Foyer')
    
    def enter(self):
        print("""
        Welcome to the foyer where you make a decision on how you want the game to start.
        You have two doors you can walk into. Either you enter the Library or the Kitchen. 
        Pick wisely!
        """)

        choice = input("> ").lower()
        if choice == 'library':
            return 'library'
        elif choice == 'kitchen':
            return 'kitchen'
        else: 
            print('Wrong choice! You will be returned to the foyer')
            return 'foyer'
    