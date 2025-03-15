from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_pos=10
        self.y_pos=10
        self.ball_speed = 0.1
        self.respawn()
        
    def move(self):
        new_X_pos = self.xcor() + self.x_pos
        new_y_pos = self.ycor() + self.y_pos
        self.goto(new_X_pos,new_y_pos)
    
    def respawn(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        
    def bounce_y(self):
        self.y_pos*=-1
    
    def bounce_x(self):
        self.x_pos*=-1
        self.ball_speed *= 0.9
        