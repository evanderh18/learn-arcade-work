# Welcome Screen
import random

miles_traveled = 0
thirst = 0
camel_tiredness = 0
distance_of_natives = -20
def main():
    print("Welcome to Camel!")
    print("You have stolen a camel to make your way across the great Mobi desert.")
    print("The natives want their camel back and are chasing you down! Survive your")
    print("desert trek and out run the natives.")

    done = False
    while not done:
        print("A. Drink from your canteen.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit.")

        user_choice = input("What is your choice? ")
        print(user_choice)

        if user_choice.upper() == "Q":
            done = True
            print("You have chosen to end your journey, you died!")

        elif user_choice.upper() == "E":
            done = False
            print("Miles Traveled:", miles_traveled)
            print("Your drinks in canteen:", thirst)
            print("Your camel is at", camel_tiredness, "strength.")
            print("The natives are", distance_of_natives, "behind you!")

        elif user_choice.upper() == "D":
            done = False
            print("You have decided to rest for the night")
            #camel_tiredness = 0
            print("Your camel is happy and fully rested!")

            native_random = random.randrange(7, 14)

            def sum_two_numbers(distance_of_natives, native_random):
                result = (distance_of_natives + native_random)
                return result
            print("The natives are now", sum_two_numbers(distance_of_natives, native_random), "behind you!")




main()