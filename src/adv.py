from os import system, name
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

# create items
items = {
    'flashlight': Item('flashlight','small flashlight'),
    'dagger': Item('dagger', 'Small dull dagger'),
}
# add items to rooms
room['foyer'].add_item(items['flashlight'])
room['foyer'].add_item(items['dagger'])
room['overlook'].add_item(items['dagger'])
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
if __name__ == "__main__":
    def clear():
        if name == 'nt':
            _ = system('cls')
        else:
            _ = system('clear')

# Make a new player object that is currently in the 'outside' room.
    player = Player("sam",room['outside'])
    playing = True

    while(playing):
        
        print(f'{player.name} is in the {player.current_room.name}')
        print(f'{player.current_room.description}')
        if len(player.current_room.items) >= 1:
            if len(player.current_room.items) == 1:  
                print(f'You see something {player.current_room.items[0].description }')
            else:
                print('You see some items...')
                for i in player.current_room.items:
                    print(i.description)
        user_input = input()
        if(user_input == 'q' or user_input == 'quit'):
            print('Are you sure you want to quit Game')
            user_input = input()
            if user_input == 'y' or user_input == 'yes':
                playing = False
                exit()
            elif user_input == 'n' or user_input =='no':
                pass
        elif user_input == 'n' or user_input == 'north':
            if player.current_room.n_to != None:
                player.current_room = player.current_room.n_to
            else:
                pass
        elif user_input == 'e' or user_input == 'east':
                if player.current_room.e_to != None:
                    player.current_room = player.current_room.e_to
                else:
                    pass
        elif user_input == 's' or user_input == 'south':
            if player.current_room.s_to != None:
                player.current_room = player.current_room.s_to
            else:
                pass
        elif user_input == 'w' or user_input == 'west':
             if player.current_room.w_to != None:
                player.current_room = player.current_room.w_to
             else:
                pass
        elif( len(user_input.split()) > 1):
            temp = user_input.split()
            if temp[0] == 'take':
                player.add_item(temp[1])
                print(player.inventory)
                print(f'You picked up {temp[1]}')
                player.current_room.remove_item(temp[1])
            if temp[0] == 'drop':
                if player.get_item(temp[1]):
                    player.current_room.add_item(player.get_item(temp[1]))
                    player.drop_item(temp[1])
                    print(player.inventory)
                    print(f'You droped {temp[1]}')
                else:
                    print(f'You dont have a {temp[1]} to drop')
                
                
        else:
            print('Movement is not allowed')

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
