done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True

    if not done:
        attack = input("Does your elf attack the dragon? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True

    if not done:
        attack = input("Does your elf attempt to steal the gold? ")
        if attack == "y":
            print("Bad choice, you died.")
            done = True