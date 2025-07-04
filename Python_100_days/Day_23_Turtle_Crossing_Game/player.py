STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
from turtle import Turtle

class Player(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.respawn()

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # def move_down(self):
    #     new_y = self.ycor() - 20
    #     self.goto(x=self.xcor(), y=new_y)
    
    # def move_left(self):
    #     new_x = self.xcor() - 20
    #     self.goto(x=new_x, y=self.ycor())
    
    # def move_right(self):
    #     new_x = self.xcor() + 20
    #     self.goto(x=new_x, y=self.ycor())
    
    def respawn(self):
        self.goto(STARTING_POSITION)