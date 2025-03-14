from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
choice = screen.textinput(title="Make your bet", prompt="Which turtle will win? Enter a color: ").lower()
color = ["red","orange","yellow","green","blue","purple"]

turtles=[]
y_axis = -90
for i in range(6):
    turtles.append(Turtle("turtle"))
    turtles[i].color(color[i])
    turtles[i].penup()
    turtles[i].goto(x=-240,y=y_axis)
    y_axis+=40
    
race_start = False

if choice:
    race_start=True
 

while race_start:
   for turtle in turtles:
       if turtle.xcor() > 225:
           race_start=False
           winner_color = turtle.pencolor()
           if choice == winner_color:
               print(f"You win! The {winner_color} is the winner.")
           else:
               print(f"You lose! The {winner_color} is the winner.")
       turtle.forward(random.randint(1,10))







screen.exitonclick()