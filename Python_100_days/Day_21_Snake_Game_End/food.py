from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("yellow")
        self.speed(0)
        self.respawn()
        
    def respawn(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x,random_y)