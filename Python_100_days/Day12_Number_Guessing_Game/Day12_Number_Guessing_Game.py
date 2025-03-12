import random
import os
def cls():
    os.system('cls' if os.name=="nt" else 'clear')


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        return  10
    else:
        return  5

def guess_num(guess, num, attempts):
        if guess > num:
            print("Too high.")
            return attempts-1
        elif guess < num:
            print("Too low.")
            return attempts-1
        elif guess == num:
            print(f"You got it! The number was {num}.")

def number_guessing():
    repeat = True
    while repeat:
        cls()
        print("=====================================")
        print("Welcome to The NUMBER GUESSING GAME!")
        print("=====================================")
        print("I am thinking of a number between 1 and 100")
        num = random.randint(1,100)
        attempts = set_difficulty()
        
        
        guess = 0
        while guess!=num:
            print(f"You have {attempts} attempts remaining.")
            guess = int(input("Make a guess: "))
            attempts = guess_num(guess,num,attempts)
            
            if attempts == 0:
                print("You've run out of attempts, you lose!")
                break
            elif guess != num:
                print("Guess again.")
        
        choice=input("Do you want to play again? Type 'y' or 'n': ")
        if choice == "n":
            repeat = False
            cls()
            
if __name__ == "__main__":
    number_guessing()