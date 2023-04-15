import random
import math
ROOM_MIN = 1
ROOM_MAX = 7


class Room:
    def __init__(self, description: str = "", north: int = 0, east: int = 0, south: int = 0, west: int = 0):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west

class Item:
    def __init__(self, description: str = "", room_num: int = 0, name: str = ""):
        self.description: str = description
        self.room_num: int = room_num
        self.name: str = name

class Ghost:
    def __init__(self, room_num: int = 1):
        self.room_num: int = room_num

def main():
    room_list = []
    item_list = []
    ghost_list = []

    lives = 3

    input("---Welcome to the Haunted Mansion---\nYour objective is to find your way out hahaha!\nFind a key to open "
          "up the door to the main exit\n---PRESS ANY KEY TO CONTINUE---")

    ghost_list.append(Ghost(random.randint(ROOM_MIN, ROOM_MAX)))

    item_list.append(Item("There is a invisibility potion here", random.randint(ROOM_MIN, ROOM_MAX), "Potion"))
    item_list.append(Item("A Key that gives you access to another room", random.randint(ROOM_MIN, ROOM_MAX), "Key"))
    item_list.append(Item("You found sage", random.randint(ROOM_MIN, ROOM_MAX), "Sage"))
    item_list.append(Item("You found a match", random.randint(ROOM_MIN, ROOM_MAX), "Match"))

    room = Room("You are in a bedroom that has two small beds.\nThere is a door to your North and East.", 3, 1, None,
                None)
    room_list.append(room)
    room = Room("You are in the South Hall which has old furniture.\nThere is a door to your North, East, and West.", 4,
                2, None, 0)
    room_list.append(room)
    room = Room("You are in the Dining Room, the table seems to be set for six.\nThere is a door to your North and "
                "West.", 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in the Master Bedroom, the furniture seems to be too fancy.\nThere is a door "
                "to your East and South.", None, 4, 0, None)
    room_list.append(room)
    room = Room("You are in the North Hall, it is filled with modern furniture.\nThere is a door to your North, East, "
                "South, and West.", 6, 5, 1, 3)
    room_list.append(room)
    room = Room("You are in the Kitchen, looks like someone is cooking a meal, smells good!\nIf you do not want any "
                "food, there is a door to your South and West.", None, None, 2, 4)
    room_list.append(room)
    room = Room("You made it to the Balcony, pretty view!\nYou only have a door to your South.", None, None, 4, None)
    room_list.append(room)

    current_room = 0
    next_room = None

    done = False
    while not done:
        caught_by_ghost = False
        print("\n" + room_list[current_room].description)
        for f in item_list:
            if f.room_num == current_room:
                print(f.description)
        for f in ghost_list:
            if f.room_num == current_room:
                print("Zoinks! A ghost has shown itself!\nSave yourself with sage and a match if you have one\nUse"
                      "command\"USE Sage\"")
                caught_by_ghost = True
                break
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
        elif command_words[0].upper() == "GET":
            found_item = False
            for f in item_list:
                if f.name.upper() == command_words[1].upper():
                    found_item = True
                    f.room_num = -1
                    break
            if found_item == False:
                print("Error item is not found or does not exist")
        elif command_words[0].upper() == "INVENTORY":
            for f in item_list:
                if f.room_num == -1:
                    print(f.name)
        elif command_words[0].upper() == "USE":
            for f in item_list:
                if f.name.upper() == command_words[1].upper():
                    f.room_num = random.randint(ROOM_MIN, ROOM_MAX)
        elif command_words[0].upper() == "Q" or command_words[0].upper() == "QUIT":
            done = True
            print("\nYou left the house\nGame Over")
            continue
        else:
            print("Unknown Command")
            next_room = None
            continue

        if next_room is None:
            print("There is no room here!")
        else:
            if caught_by_ghost == True:
                print("The ghost took one of your lives")
                lives -= 1
                print(lives)
            current_room = next_room
            for f in ghost_list:
                f.room_num = random.randint(ROOM_MIN, ROOM_MAX)


main()
