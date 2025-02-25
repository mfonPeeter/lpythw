class Room(object):

    def __init__(self, room_name):
        self.room_name = room_name
    
    def enter(self):
       print("Each room will have a different enter approach")