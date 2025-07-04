FONT = ("Courier", 12, "normal")
LEVEL_COORDINATE = (-260,260)
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("black")
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.goto(LEVEL_COORDINATE)
        self.write(f"Level: {self.level}", align="left", font=FONT)
        
    def increase_level(self):
        self.level+=1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)