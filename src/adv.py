from room import Room
from player import Player
import sys
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

#[OV] [TR]
# |     |
#[FO]-[NA]
# |
#[OT]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
newPlayer= Player('myname','outside',['item1','item2'])
print(newPlayer)

# Write a loop that:
running=True
while(running):
#
# * Prints the current room name
    current_location=newPlayer.get_location
    print(current_location)
# * Prints the current description (the textwrap module might be useful here).
    print(room[f"{current_location}"].get_description)
# * Waits for user input and decides what to do.
    input = input("what action would you like to take? : ")
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
    if(input=="q"):
        print("Goodbye!")
        sys.exit(1)
# If the user enters "q", quit the game.




#stuff from class
# #define a store using OOP principals

# class Store:
#     def __init__(self, name, departments):
#         self.name=name
#         #departments will be a list strings that we need to make departments
#         self.departments= self.init_departments(departments)

#     def __str__(self):
#         #will print out the name of the store
#         #as well as any departments that the store has (stores can have more than 1 dept)
#         output= f"{self.name} \n"
#         for dept in self.departments:
#             output += "  id: " + str(dept.get_id()) + ", name: " + dept.get_name() + "\n"
#         return output
#     def init_departments(self, departments):
#         #normal version
#         # instances = []
#         # for index, dept in enumerate(departments):
#         #     instances.append(Department(index+1, dept))
#         # return instances
#         #list comprehension
#         return [Department(index+1 , dept) for index, dept in enumerate(departments)]

# #not having it inherit since it didn't make sense to our instructor, make sure to think through if something is distinct
# class Department:
#     def __init__(self, id, name):
#         self.id=id
#         self.name=name
#     def __str__(self):
#         return f"Department {self.id}: {self.name}"
#     def get_id(self):
#         return self.id

#     def get_name(self):
#         return self.name

# departments=[
#     "running",
#     "fishing",
#     "baseball",
#     "basketball"
#     ]
# # Department(4, "basketball") used to have the departments structured like this
# my_store = Store("The Dugout", departments)
# print(my_store)

# selection = input("select the department number: ")
# print(f"you selected Department {selection}, {my_store.departments[int(selection)-1].get_name()}")

#a couple things that we can think about fixing
#there's no way to access departments easily outside of our store class
#fixed sorta, but we need to not pull from the input array as the source of truth
#fixed to taking just from my_store and callind get name for the dept

#streamline adding departments to our store
#adding a method on the store class that will taking a list of strings and make them departments