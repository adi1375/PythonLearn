print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.")
choice = input(
    f"You're at a crossroad, where do you want to go? Type 'Left' or 'Rgiht'.\n"
).lower()

if choice == "left":
    choice = input(
        f"You've  come to a lake. There is an island in the middle of the lake. Type 'Wait' to wait for a boat. Type 'Swim' to swim across.\n"
    ).lower()
    if choice == "wait":
        choice = input(
            f"You arrive at the island unharmed. There are three doors, 'Red', 'Blue' and 'Yellow'. which one do you choose?\n"
        ).lower()
        if choice == "yellow":
            print("You found the treaseure. You win!")
        else:
            print("You chose the wrong door. Game Over.")
    else:
        print("You got attacked by a trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")
