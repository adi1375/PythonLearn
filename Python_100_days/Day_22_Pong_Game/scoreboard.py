from turtle import Turtle

ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(50, 300)
        self.write(self.score_right, align=ALIGNMENT, font=("Courier", 60, "normal"))
        self.goto(-50, 300)
        self.write(self.score_left, align=ALIGNMENT, font=("Courier", 60, "normal"))
            
    def point_left(self):
        self.score_left+=1
        self.update_scoreboard()
        
    def point_right(self):
        self.score_right+=1
        self.update_scoreboard()