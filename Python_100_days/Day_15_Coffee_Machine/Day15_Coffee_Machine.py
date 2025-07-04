import os
def cls():
    os.system("cls" if os.name=="nt" else "clear")

def displayReport():
    print(f"Water: {resources["water"]}ml")
    print(f"Milk: {resources["milk"]}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: Rs. {money}")


def ask_for_money():
    rupee = float(input("Please enter ruppee coins: "))
    paise = float(input("Please enter 50 paise coins: "))
    return  rupee + paise/2
    
def calculateResources(item):
    for k in item:
        resources[k]-=item[k]
        
def makeDrink(order,item):
    order_price = MENU[order]["cost"]
    print(f"It costs Rs. {order_price}")
    drink_served = False
    while not drink_served:
        money_received = ask_for_money()
        if money_received > order_price:
            drink_served = True
            change = money_received-order_price
            calculateResources(item)
            print(f"Here is your {order}. Enjoy!")
            print(f"Here's your your change of Rs. {round(change,2)}")
            return order_price
        elif money_received < order_price:
            print("Sorry that's not enough. Money refunded.")
        else:
            drink_served = True
            calculateResources(item)
            print(f"Here is your {order}. Enjoy!")
            return order_price
    
   
def serveDrink(order):
    item = MENU[order]["ingredients"]
    for k in item:
        if item[k]>resources[k]:
            print(f"Sorry, there is not enough {k}.")
            return 0.00
    return makeDrink(order,item)

MENU ={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.50,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.50,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.00
    },
}

resources ={
    "water":500,
    "milk":300,
    "coffee":100,
}

money = 0.00
repeat = True
while repeat:
    choice = input("What would you like to order? (espresso/latte/cappuccino) ").lower()
    if choice =="report":
        displayReport()
    elif choice == "off":
        cls()
        repeat = False
        print("Good Bye.")
    else:
        money += serveDrink(choice)