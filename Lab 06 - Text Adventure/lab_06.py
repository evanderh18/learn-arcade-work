class Room:
    def __init__(self, description: str = "", north: int = 0, east: int = 0, south: int = 0, west: int = 0):
        self.description: str = description
        self.north: int = north
        self.east: int = east
        self.south: int = south
        self.west: int = west


def main():
    room_list = []
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
        user_input = input("What direction do you want to go? ")
        if user_input.upper() == "N" or user_input.upper() == "NORTH":
            next_room = room_list[current_room].north
        elif user_input.upper() == "E" or user_input.upper() == "EAST":
            next_room = room_list[current_room].east
        elif user_input.upper() == "S" or user_input.upper() == "SOUTH":
            next_room = room_list[current_room].south
        elif user_input.upper() == "W" or user_input.upper() == "WEST":
            next_room = room_list[current_room].west
        elif user_input.upper() == "Q" or user_input.upper() == "QUIT":
            done = True
            print("\nYou left the house\nGame Over")
            continue
        else:
            print("Unknown direction")
            next_room = None
            continue

        if next_room is None:
            print("There is no room here!")
        else:
            current_room = next_room


main()