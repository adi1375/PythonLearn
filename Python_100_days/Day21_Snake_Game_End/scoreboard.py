from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = True):
        super().__init__(shape, undobuffersize, visible)
        self.penup()
        self.goto(0,370)
        self.score = 0
        with open("Python_100_days\Day21_Snake_Game_End\data.txt",mode="r") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.color("white")
        self.update_scoreboard()        
        
        
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("Python_100_days\Day21_Snake_Game_End\data.txt",mode="w") as data:
                data.write(f"{self.high_score}")  
        self.score = 0
        self.update_scoreboard()
          
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

