# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.tools = []

    def setLocation(self, new_room):
        self.current_room = new_room

    def add_tool(self, item):
        self.tools.append(item)
