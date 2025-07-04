import os
def cls():
    os.system('cls' if os.name=="nt" else 'clear')

def highest_bidder(bidders):
    # max = 0
    # for key, val in bidders.items():
    #     if val > max:
    #         max = val
    #         winner = key
    winner = max(bidders, key=bidders.get)
    print(f"The winner is {winner} with a bid of ${bidders[winner]}.")
    

print("Weclome to The Secret Auction Program")
bidders ={}
repeat = True
while repeat:
    str = input("What is your name?: ")
    bid =int(input("What's your bid?: $"))
    bidders[str] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    
    if choice == "yes":
        cls()
    else:
        repeat = False
        cls()
        highest_bidder(bidders)

