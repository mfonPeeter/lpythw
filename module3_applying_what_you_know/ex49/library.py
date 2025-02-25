from room import Room

class Library(Room): 

    def __init__(self):
        super().__init__('Library')

    def enter(self): 
        print("Yo, you've entered the library. The guardian comes out and you are asked a riddle to determine if you go proceed to the next room or not.")
        
        ans = input('What goes up, but never comes down? ').strip().lower()

        if ans == 'age': 
            print('Correct!')
            return 'exit'
        else: 
            print('Wrong! You will be sent back to the foyer. Ah ah ah')
            return 'foyer'