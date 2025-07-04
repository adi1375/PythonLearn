# import colorgram

# colors = colorgram.extract("Python_100_days\Day18_Hirst_Painting\hirst.jpg", 30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)
from turtle import Turtle,Screen
import random

tim=Turtle()
screen = Screen()
screen.colormode(255)


rgb_colors = [(247, 241, 232), (236, 241, 248), (248, 239, 243), (239, 247, 244), (140, 165, 192), (211, 155, 116), (23, 37, 56), (192, 142, 152), (60, 102, 134), (148, 69, 58), (231, 212, 107), (143, 177, 162), (141, 68, 77), (145, 28, 35), (46, 36, 32), (46, 32, 37), (66, 110, 96), (33, 51, 46), (135, 32, 27), (227, 168, 174), (234, 169, 161), (186, 98, 107), (194, 95, 82), (175, 188, 216), (18, 92, 69), (110, 124, 158), (33, 61, 105), (173, 203, 193), (21, 79, 98), (60, 149, 185)]

tim.speed(0)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(400)
tim.setheading(0)


for i in range(1, 101):
    tim.dot(20,random.choice(rgb_colors))
    
    tim.forward(50)

    if i%10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
   

screen.exitonclick()