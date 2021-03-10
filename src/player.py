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

    def has_item(self, item):
        for i in self.tools:
            if i.name == item:
                return i
            return False

    def remove_tool(self, item):
        self.tools.remove(item)
