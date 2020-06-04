from room import Room
from player import Player
from item import Item
# Declare Items

items = {
    "sword": Item("sword", "a rusty sword"),
    "coins": Item("coins", "a pile of coins"),
    "axe": Item("axe", "a mighty axe"),
    "necklace": Item("necklace", "very shiny and bright!")
}



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


# Add items to rooms
room['foyer'].items.append(items['sword'])
room['outside'].items.append(items['axe'])
room['narrow'].items.append(items['necklace'])
room['overlook'].items.append(items['coins'])


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Cole', room['outside'])

# Write a loop that:
#
while True:
    command = input("Where you going n, e, s, w? press 'f' to find, 'p' to pickup, 'd' to drop, 'i' for inventory and 'q' to quit: ")
    if command == "n":
        if player.current_room.n_to == None:
            print(" Can't go that way!")
            continue 
        player.current_room = player.current_room.n_to
    elif command == "e":
        if player.current_room.e_to == None:
            print(" Can't go that way!")
            continue
        player.current_room = player.current_room.e_to
    elif command == "s":
        if player.current_room.s_to == None:
            print(" Can't go that way!")
            continue
        player.current_room = player.current_room.s_to
    elif command == "w":
        if player.current_room.w_to == None:
            print(" Can't go that way!")
            continue
        player.current_room = player.current_room.w_to
    elif command == "f":
        player.current_room.print_items()     
    elif command == "i":
        player.inventory()
    elif command == "q":
        print("You Quit")
        break
    print(player.current_room)

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal command, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
