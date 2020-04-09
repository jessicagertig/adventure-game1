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

# Declare all the items
thing = {
'ruby': Item('Ruby', 'glittering deep red jewel'),
'dagger': Item('Dagger', 'razor sharp two sided dagger'),
'shovel': Item('Shovel', 'long handled rusty shovel'),
'dress': Item('Dress', 'fitted scarlet velvet gown trimmed with golden braid'),
'vest': Item('Vest', 'leather vest with lacings to put on over any clothing'),
'pants': Item('Pants', 'leather leggings which are strangely flexible'),
'shirt': Item('Shirt', 'dark gold silk button up shirt which seems impervious to flames'),
'lantern': Item('Lantern', 'metal lantern with a seeminly endless supply of fuel'),
'lighter': Item('Lighter', 'pure gold lighter with a rose pattern etched into the gold'),
'food': Item('Protein Bar', 'slightly unpleasant tasting edible bar that seems to provide all necessary nutrients'),
'stick': Item('Stick', 'a useless looking wooden stick'),
}

# Create Room Items
room['outside'].items = [thing['stick'], thing['lighter']]
room['foyer'].items = [thing['lantern'], thing['shovel']]
room['overlook'].items = [thing['ruby'], thing['dress'], thing['vest']]
room['narrow'].items = [thing['pants'], thing['dagger'], thing['shirt']]
room['treasure'].items = [thing['food']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
human = Player(room['outside'])
##BEGIN SETUP
human.name = input("Please enter your name: \n")
player = human.name.upper()

print("#############################################")
print(f"## Welcome to the Adventure Game {player}! ##")
print("#############################################\n")

game_running = True

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
while game_running == True:
    place = human.location.name.upper()
    print(f"{player} you are in the {place}.\n")
    print(f"{human.location.description}...\n")
    print("Your choices are: [n] North  [s] South  [w] West [e] East [q] Quit [l] Look  [i] Inventory")
    choice = input("Please make a selection to continue: ")
    print("  ")
    if choice == "n":
        if human.location.n_to is not None:
            human.location = human.location.n_to
        else:
            print("######################################")
            print("BUMP! Please choose another direction!")
            print("######################################\n")
    elif choice == "s":
        if human.location.s_to is not None:
            human.location = human.location.s_to
        else:
            print("######################################")
            print("BUMP! Please choose another direction!")
            print("######################################\n")
    elif choice == "e":
        if human.location.e_to is not None:
            human.location = human.location.e_to
        else:
            print("######################################")
            print("BUMP! Please choose another direction!")
            print("######################################\n")
    elif choice == "w":
        if human.location.w_to is not None:
            human.location = human.location.w_to
        else:
            print("######################################")
            print("BUMP! Please choose another direction!")
            print("######################################\n")
    elif choice == "l":
        if len(human.location.items) == 0:
            print("The room is empty.\n")
        elif len(human.location.items) > 0:
            print('In the room you find:')
            for i in human.location.items:
                print(f"Name: '{i.item_name}': {i.item_description}.\n")
            print(f"You may pick up an item (command [p]) and add it to your inventory or continue (command [c]).\n")
            option = input("Please select an option: ")
            if option == "c":
                pass
            elif option == "p":
                added_item = thing[input("Please type the item's name: ")]
                human.get_item(added_item)
                for e in human.inventory:
                    print(e.item_name)
            else:
                print("Please select a valid command.\n")
    elif choice == "i":
        if len(human.inventory) == 0:
            print("Your inventory is empty.\n")
    elif choice == "d":
        pass
    elif choice == "p":
        pass
    elif choice == "q":
        print("GOODBYE!!!\n")
        game_running = False
        break
    else:
        print("###################################") 
        print("PLEASE CHOOSE A VALID COMMAND BELOW.")
        print("###################################\n")


