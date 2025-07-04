from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(coordinate)
        self.speed(0)
        
    def move_up(self):
            new_y = self.ycor() + 20
            self.goto(x=self.xcor(), y=new_y)
            
    def move_down(self):
            new_y = self.ycor() - 20
            self.goto(x=self.xcor(), y=new_y)