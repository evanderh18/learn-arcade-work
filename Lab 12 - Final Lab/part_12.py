import random
import math

class Room:
    def __init__(self, description: str = "", north: int = 0, east: int = 0, south: int = 0, west: int = 0):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west

class Item:
    def __init__(self, description: str = "", room_num: int = "", name: str = ""):
        self.description: str = description
        self.room_num: int = room_num
        self.name: str = name

def main():
    room_list = []
    item_list = []
    item_list.append(Item("There is a invisibility potion here", random.randint(0, 7), "Potion"))
    item_list.append(Item("A Key that gives you access to another room", random.randint(0, 7), "Key"))
    item_list.append(Item("You found sage", random.randint(0, 7), "Sage"))
    item_list.append(Item("You found a match", random.randint(0, 7), "Match"))

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
        print("\n" + room_list[current_room].description)
        for f in item_list:
            if f.room_num == current_room:
                print(f.description)
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
                    f.room_num = random.randint(0, 7)
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
            current_room = next_room


main()
