from turtle import Turtle,Screen
import random

tim = Turtle()
screen = Screen()
screen.colormode(255)
tim.shape("turtle")
tim.color("red")

"""Draw a square"""
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

"""Draw a dashed line"""
# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

"""Assings a random color to turtle"""
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    
    tim.color(r,g,b)
    
"""Draws different shapes with random colors"""
# for side in range(3,11):
#     # tim.color(random.choice(color))
#     random_color()
#     for _ in range(side):
#         angle = 360 / side
#         tim.right(angle)
#         tim.forward(100)
    
# directions = [0, 90, 180, 270]

"""Random Walk implementation"""
# for _ in range(100):
#     tim.speed(0)
#     tim.pensize(10)
#     random_color()
#     tim.setheading(random.randrange(0,271,90))
#     tim.forward(20)
    
"""Draw a Spirograph"""
for angle in range(0,361,5):
    tim.speed(0)
    random_color()
    tim.circle(100)
    tim.setheading(angle)
        
screen.exitonclick()


