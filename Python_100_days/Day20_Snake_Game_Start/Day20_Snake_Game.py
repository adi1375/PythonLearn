from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.title("The Sanke Game")
screen.setup(height=800,width=800)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()

screen.onkey(key="Up",fun=snake.move_up)
screen.onkey(key="Down",fun=snake.move_down)
screen.onkey(key="Left",fun=snake.move_left)
screen.onkey(key="Right",fun=snake.move_right)

game_over = False

while not game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()    

    

screen.exitonclick()
