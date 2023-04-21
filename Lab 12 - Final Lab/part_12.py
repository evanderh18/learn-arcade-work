import random
from room import Room
from item import Item
from ghost import Ghost

import math
ROOM_MIN = 2
ROOM_MAX = 9

def move_ghosts(ghost_list):
    for f in ghost_list:
        next_room_num = random.randint(ROOM_MIN, ROOM_MAX)
        while next_room_num == f.room_num:
            next_room_num = random.randint(ROOM_MIN, ROOM_MAX)
        f.room_num = next_room_num
#Override to make sure ghost does not appear in the same room again when using sage
def move_ghosts_sage(ghost_list, current_room):
    for f in ghost_list:
        next_room_num = random.randint(ROOM_MIN, ROOM_MAX)
        while next_room_num == f.room_num or next_room_num == current_room:
            next_room_num = random.randint(ROOM_MIN, ROOM_MAX)
        f.room_num = next_room_num

def main():
    room_list = []
    item_list = []
    ghost_list = []

    lives = 3
    potion_countdown = 0

#Intro Screen
    input("---Welcome to the Haunted Mansion---\nYour objective is to find your way out hahaha!\nFind a key to open "
          "up the door to the main exit\n***In order to move around rooms, command your desired direction***\n***To view "
          "inventory type command \"INVENTORY\"***\n***To quit game type command \"QUIT\"***\n---PRESS ENTER KEY TO "
          "CONTINUE---")
#Spawn Ghost
    ghost_list.append(Ghost(random.randint(ROOM_MIN, ROOM_MAX)))
    ghost_list.append(Ghost(random.randint(ROOM_MIN, ROOM_MAX)))
    ghost_list.append(Ghost(random.randint(ROOM_MIN, ROOM_MAX)))
#Spawn Items
    item_list.append(Item("There is a invisibility potion here\nPick up using command GET POTION", random.randint(ROOM_MIN, ROOM_MAX), "Potion"))
    item_list.append(Item("A Key that gives you access to leave the mansion!\nPick up using command GET KEY", random.randint(ROOM_MIN, ROOM_MAX), "Key"))
    item_list.append(Item("You found sage\nPick up using command GET SAGE", random.randint(ROOM_MIN, ROOM_MAX), "Sage"))
#Rooms
    room = Room("You are in a bedroom that has two small beds.\nThere is a door to your North and East.", 3, 1, None,
                None)
    room_list.append(room)

    room = Room("You are in the South Hall which has old furniture.\nThere is the main door! Escape using command \"USE KEY\" if found.\nThere is a door to your North, East, and West.", 4,
                2, None, 0)
    room_list.append(room)

    room = Room("You are in the Dining Room, the table seems to be set for six. Maybe room for one more?\nThere is a door to your North and "
                "West.", 5, None, None, 1)
    room_list.append(room)

    room = Room("You are in the Master Bedroom, the furniture seems to be too fancy.\nThere is a door "
                "to your North, East and South.", 6, 4, 0, None)
    room_list.append(room)

    room = Room("You are in the North Hall, it is filled with modern furniture, that has collected dust.\nThere is a door to your North, East, "
                "South, and West.", 7, 5, 1, 3)
    room_list.append(room)

    room = Room("You are in the Kitchen, looks like someone is cooking a meal, smells good! Not sure who it is for.\n"
                "There is a door to your South and West.", 8, None, 2, 4)
    room_list.append(room)

    room = Room("You are in the Master Bathroom, looks like whoever was here left in a hurry.\nThere is only a door to your South.", None, None, 3, None)
    room_list.append(room)

    room = Room("You made it to the Balcony, pretty view! Too high to jump.\nYou only have a door to your South.", None, None, 4, None)
    room_list.append(room)

    room = Room("You are in the pantry, stocked with rotten food.\nYou only have a door to your South.", None, None, 5, None)
    room_list.append(room)

    current_room = 0
    next_room = 0

    done = False
    #Travel rooms
    while not done:
        caught_by_ghost = False
        print("\n" + room_list[current_room].description)
        for f in item_list:
            if f.room_num == current_room:
                print(f.description)
        #If no potion check if caught by ghost
        if potion_countdown == 0:
            for f in ghost_list:
                if f.room_num == current_room:
                    print("Zoinks! A ghost has shown itself!\nSave yourself with sage if you have one\nUse"
                      " command \"USE Sage\"")
                    caught_by_ghost = True
                    break
        #Commands
        user_input = input("What is your action? ")
        command_words = user_input.split(" ")
        if command_words[0].upper() == "N" or command_words[0].upper() == "NORTH":
            next_room = room_list[current_room].north
        elif command_words[0].upper() == "E" or command_words[0].upper() == "EAST":
            next_room = room_list[current_room].east
        elif command_words[0].upper() == "S" or command_words[0].upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif command_words[0].upper() == "W" or command_words[0].upper() == "WEST":
            next_room = room_list[current_room].west
        #Get Command, Pick up Item
        elif command_words[0].upper() == "GET":
            found_item = False
            for f in item_list:
                if f.name.upper() == command_words[1].upper():
                    found_item = True
                    f.room_num = -1
                    break
            if found_item == False:
                print("Error item is not found or does not exist")
        #Check Inventory
        elif command_words[0].upper() == "INVENTORY":
            for f in item_list:
                if f.room_num == -1:
                    print(f.name)
        #Use Command
        elif command_words[0].upper() == "USE":
            found_item = False
            for f in item_list:
                if f.name.upper() == command_words[1].upper() and f.room_num == -1:
                    found_item = True
                    if command_words[1].upper() == "POTION":
                        potion_countdown = 2
                        print("Potion used\nYou are now hidden from the ghost for 2 rounds")
                    elif command_words[1].upper() == "KEY":
                        if current_room == 1:
                            print("You can open the door with the key!\nYou can now leave!\nYou Won!")
                            done = True
                        if current_room != 1:
                            print("You cannot use key here")
                            break
                    elif command_words[1].upper() == "SAGE":
                        if caught_by_ghost == True:
                            caught_by_ghost = False
                            move_ghosts_sage(ghost_list, current_room)
                            print("The ghost fled!")
                    f.room_num = random.randint(ROOM_MIN, ROOM_MAX)
            if found_item == False:
                print("Item does not exist in inventory")
        #Quit Game Command
        elif command_words[0].upper() == "Q" or command_words[0].upper() == "QUIT":
            done = True
            print("\nYou left the house\nGame Over")
            continue
        #Unknown Command
        else:
            print("Unknown Command")
            next_room = None
            continue
        #If no Room
        if next_room is None:
            print("There is no room here!")
        #Hit from Ghost
        elif next_room != current_room:
            if caught_by_ghost == True:
                print("The ghost took one of your lives. Lives remaining:")
                lives -= 1
                print(lives)
            if lives == 0:
                print("Game Over\nThe ghost killed ya!")
                done = True
                break
        #Drop potion count if active
            if potion_countdown > 0:
                potion_countdown -= 1

            current_room = next_room
            move_ghosts(ghost_list)


main()
