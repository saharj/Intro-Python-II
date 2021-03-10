# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

        def _set_nick_name(name):
            if name == "Outside Cave Entrance":
                return "outside"
            elif name == "Foyer":
                return "foyer"
            elif name == "Grand Overlook":
                return "overlook"
            elif name == "Narrow Passage":
                return "narrow"
            else:
                return "treasure"

        self.nick_name = _set_nick_name(name)

    def add_item(self, item):
        self.items.append(item)

    def find_item(self, item):
        for i in self.items:
            if i.name == item:
                return i
            return False
