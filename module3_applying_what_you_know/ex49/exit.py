from sys import exit
from room import Room

class Exit(Room): 
    
    def __init__(self):
        super().__init__('Exit')

    def enter(self):
        print("You've successfully reached the exit. Enjoy the exit! Have lot of fun!")
        exit(0)