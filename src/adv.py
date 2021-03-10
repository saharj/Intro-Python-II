from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

bucket = Item("bucket", "this is a bucket")
broom = Item("broom", "this is a broom")
rope = Item("rope", "this is a rope")
key = Item("key", "This key can open any door")
treasure = Item("treasure", "What can it be?")
# print(bucket.name)

room['outside'].add_item(bucket)
room['foyer'].add_item(broom)
room['foyer'].add_item(rope)
room['narrow'].add_item(key)
room['treasure'].add_item(treasure)

# print(room['outside'].items[0].name)

#
# Main
#
print("")
print("WHERE IS THE TREASURE?")
print("")
# Make a new player object that is currently in the 'outside' room.

player = Player("outside")

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# TODO: Remove the line below
current = "outside"
choice = ""

while choice != "q":

    command = choice.split()

    if len(command) <= 1:
        if choice == "s":
            if hasattr(room[current], "s_to"):
                current = room[current].s_to.nick_name
                player.setLocation(current)
            else:
                print(f"There is no door to the {choice} side.")
                print("Try another direction.  Select q to exit.")
        elif choice == "n":
            if hasattr(room[current], "n_to"):
                current = room[current].n_to.nick_name
                player.setLocation(current)
            else:
                print(f"There is no door to the {choice} side.")
                print("Try another direction.  Select q to exit.")
        elif choice == "e":
            if hasattr(room[current], "e_to"):
                current = room[current].e_to.nick_name
                player.setLocation(current)
            else:
                print(f"There is no door to the {choice} side.")
                print("Try another direction.  Select q to exit.")
        elif choice == "w":
            if hasattr(room[current], "w_to"):
                current = room[current].w_to.nick_name
                player.setLocation(current)
            else:
                print(f"There is no door to the {choice} side.")
                print("Try another direction.  Select q to exit.")
        else:
            print(f"There is no door to the {choice} side.")
            print("Try another direction.  Select q to exit.")
    else:
        if command[0] == 'get' or command[0] == 'take':
            # print(command)
            item = room[player.current_room].find_item(command[1])
            if item != False:
                player.add_tool(item)
                item.on_take(item.name)
                room[player.current_room].remove_item(item)
                # print(player.tools[0].name)
                # print(room.items[0].name)
            else:
                print("{command[1]} doesn't exist in this room.")

    print("------------------------------------")
    print("* You are now in " + room[player.current_room].name + ": " +
          room[player.current_room].description + "\n")
    choice = input("Take something or go to a different room: ")
    print("")
    print("")
