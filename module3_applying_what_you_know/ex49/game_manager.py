from kitchen import Kitchen
from foyer import Foyer
from library import Library
from exit import Exit

class GameManager(object):
    
    def __init__(self):
        self.rooms = {
            'foyer': Foyer(),
            'library': Library(),
            'kitchen': Kitchen(),
            'exit': Exit(),
        }
        self.current_room = 'foyer'

    def play(self): 
        while self.current_room:
            room = self.rooms[self.current_room]
            self.current_room = room.enter()
            