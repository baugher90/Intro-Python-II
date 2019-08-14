# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def__init__(self, name,current_room):
        self.name = name
        self.current_room = current_room

    def__str__(self):
        s = f'Player Name:{self.name}/n Current Location:{self.current_room}'
        return s
