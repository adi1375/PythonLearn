import os
import random
def cls():
    os.system('cls' if os.name=="nt" else 'clear')


def choose_celebrity(celebrity):
    return random.choice(list(celebrity.keys()))

def compare_followers(celeb1,celeb2,choice,score):
    if choice == 'A' and celebrity[celeb1] > celebrity[celeb2]:
        return score + 1, celeb2
    elif choice == 'B' and celebrity[celeb1] < celebrity[celeb2]:
        return score + 1, celeb1
    else:
        return 0, celeb1

def higherLower():
    user_score = 0
    game_score = 0
    repeat = True

    contestant1 = choose_celebrity(celebrity)
    while repeat:
        contestant2 = choose_celebrity(celebrity)
        while contestant1 == contestant2:
            contestant2 = choose_celebrity(celebrity)

        print(f"Compare A: {contestant1}\n")
        print("vs\n")
        print(f"Against B: {contestant2}\n")
        choice = input("Who has more followers?Type 'A' or 'B': ").upper()
        user_score, contestant1 =compare_followers(contestant1,contestant2,choice,user_score)
        if user_score == 0:
            repeat = False
            cls()
            print(f"Sorry, that's wrong. Final score: {game_score}")
        else:
            cls()
            game_score=user_score
            print(f"You are right! Current score: {game_score}")


if __name__ == "__main__":
   
    cls()
    
    celebrity ={
    "Christiano Ronaldo" : 500000000,
    "Rihanna": 150000000,
    "Lionel Messi": 505000000,
    "Narendra Modi": 93000000,
    "Shakira": 92000000,
    "Selena Gomez": 422000000,
    "Camila Cabello": 64000000,
}
    
    higherLower()