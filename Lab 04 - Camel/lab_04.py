# Welcome Screen
import random

def sum_two_numbers(value_1, value_2):
    result = (value_1 + value_2)
    return result

# Main Screen
def main():
    distance_of_natives = -20
    miles_traveled = 0
    thirst = 0
    camel_tiredness = 0
    drinks_in_canteen = 3

    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.\n")

# List of Choices
    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.\n")

        # Choice Input
        user_choice = input("What is your choice? ")
        print(user_choice)

        # Quit Choice
        if user_choice.upper() == "Q":
            done = True
            print("You have chosen to end your journey, you have died!")

        # Status Check Choice
        elif user_choice.upper() == "E":
            done = False
            print("Miles Traveled:", miles_traveled)
            print("Your drinks in canteen:", thirst)
            print("Your camel is at", camel_tiredness, "strength.")
            print("The natives are", miles_traveled - distance_of_natives, "miles behind you!\n")

        # Stop for the Night Choice
        elif user_choice.upper() == "D":
            done = False
            print("You have decided to rest for the night.")
            camel_tiredness = 0
            print("Your camel is happy and fully rested! It is now at", camel_tiredness)
            # Natives Closing in
            native_random = random.randint(7, 14)

            distance_of_natives = sum_two_numbers(distance_of_natives, native_random)

            print("The natives are now", miles_traveled - distance_of_natives, "miles behind you!\n")

        # Ahead Full Speed Choice
        elif user_choice.upper() == "C":
            done = False
            print("You decided to go full speed.")
            # Miles Traveled at Full Speed
            random_forward = random.randint(10, 20)
            miles_traveled = sum_two_numbers(random_forward, miles_traveled)
            print("You traveled", miles_traveled, "miles")
            # Thirst from Full Speed
            thirst += 1
            print("You are now at", thirst, "thirst!")
            random_tired = random.randint(1, 3)
            # Camel Tiredness from Full Speed
            camel_tiredness = sum_two_numbers(random_tired, camel_tiredness)
            print("Your camel is now", camel_tiredness, "tired")
            # Natives Closing in Full Speed
            native_random = random.randint(7, 14)
            distance_of_natives = sum_two_numbers(distance_of_natives, native_random)
            print("The natives are now", miles_traveled - distance_of_natives, "miles behind you!\n")

        # Ahead Moderate Speed Choice
        elif user_choice.upper() == "B":
            done = False
            print("You decided to go moderate speed.")
            # Miles Traveled
            random_forward = random.randint(5, 12)
            miles_traveled = sum_two_numbers(random_forward, miles_traveled)
            print("You traveled", miles_traveled, "miles")
            # Thirst
            thirst += 1
            print("You are now at", thirst, "thirst!")
            # Camel Tiredness
            camel_tiredness += 1
            print("Your camel is now", camel_tiredness, "tired")
            # Native Distance
            native_random = random.randint(7, 14)
            distance_of_natives = sum_two_numbers(distance_of_natives, native_random)
            print("The natives are now", miles_traveled - distance_of_natives, "miles behind you!\n")

        # Choice Drink from Your Canteen
        elif user_choice.upper() == "A":
            done = False
            print("You have decided to take a drink.")
            # Drink from Canteen with Error
            if drinks_in_canteen != 0:
                drinks_in_canteen -= 1
                thirst = 0
                print("You have", drinks_in_canteen, "drinks left!\n")
            else:
                print("You have no water to drink!\n")

        # Thirsty Warning
        if thirst > 4:
            print("You are thirsty\n")

        # Thirsty Death
        if thirst > 6:
            print("You died of thirst\n")
            done = True

        # Camel Tired Warning
        if camel_tiredness > 5 and done is False:
            print("Your camel is tired!\n")

        # Camel died
        if camel_tiredness > 8 and done is False:
            print("Your camel is dead!\n")
            done = True

        # Natives Catch up
        if miles_traveled <= distance_of_natives and done is False:
            print("Natives caught up, game over!\n")
            done = True

        # Natives Close
        if miles_traveled - distance_of_natives < 15 and done is False:
            print("Natives are getting close!\n")

        # Winning Screen End game
        if miles_traveled > 200 and done is False:
            print("You traveled", miles_traveled, "\nYOU WIN!!")
            done = True

        # Oasis Found By Chance
        if (user_choice.upper() == "B" or user_choice.upper() == "C") and done is False:
            if random.randrange(20) == 0:
                print("You found the oasis!")
                drinks_in_canteen = 3
                print("Canteen is now at", drinks_in_canteen)
                thirst = 0
                print("Thirst is at", thirst)
                camel_tiredness = 0
                print("Camel is at", camel_tiredness, "\n")


main()