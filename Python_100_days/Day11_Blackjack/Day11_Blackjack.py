import os
import random
def cls():
    os.system('cls' if os.name=="nt" else 'clear')

def draw_cards():
    cards_list = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards_list)   

def score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 21
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_final_score, computer_final_score):   
    if user_final_score == 21:
        return "You win with Blackjack!"
    elif computer_final_score == 21:
        return "Computer wins with Blackjack!"
    elif user_final_score > 21:
        return "You went over. You lose!"
    elif computer_final_score > 21:
        return "Computer went over. You win!"
    elif user_final_score == computer_final_score:
        return "Draw!"
    elif user_final_score > computer_final_score:
        return "You win!"
    else:
        return "You lose!"
    

def Blackjack():
    print("=====================")
    print("WELCOME TO BLACKJACK")
    print("=====================")
    user_cards =[]
    computer_cards=[]
    user_score=0
    computer_score=0
    repeat = True
    
    for _ in range(2):
        user_cards.append(draw_cards())
    computer_cards.append(draw_cards())    
    
    while   repeat:  
        user_score = score(user_cards)
        computer_score=score(computer_cards)
        
        print(f"Your cards are: {user_cards}, your current score: {user_score} ")
        print(f"Computer's 1st card: {computer_cards[0]}")
        
        if user_score >= 21:
            repeat = False 
        else: 
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                user_cards.append(draw_cards())
            else:
                repeat = False
                while computer_score!=21 and computer_score < 17:
                    computer_cards.append(draw_cards())
                    computer_score = score(computer_cards)

        
    print(f"Your final hand: {user_cards}, your final score: {user_score} ")
    print(f"Computer's final hand: {computer_cards}, computer's final score: {computer_score}")
    print(compare(user_score,computer_score))
    
    start_game()

def start_game():    
    start = input("Do you want to play Blackjack? Type 'y' or 'n': ")
    if start == "n":
        cls()
        print("Good Bye.")
    else:
        cls()
        Blackjack()

if __name__ == "__main__":       
    start_game()