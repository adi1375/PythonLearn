import random

rps = ["Rock", "Paper", "Scissor"]
user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
computer_choice = random.randint(0, 2)
print(f"You chose: {rps[user_choice]}\n")
print(f"Computer chose: {rps[computer_choice]}\n")

if user_choice > 2 or user_choice < 0:
    print("Invalid input. You lose!")
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:
    print("You lose!")
elif user_choice > computer_choice:
    print("You win!")
elif computer_choice > user_choice:
    print("You lose!")
elif computer_choice == user_choice:
    print("It's a draw!")
