from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.title("The Sanke Game")
screen.setup(height=800,width=800)
screen.bgcolor("black")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    
    # eat food, increase score
    if snake.head.distance(food) < 15:
        food.respawn()
        snake.extend_body()
        scoreboard.increase_score()

    # wall collision
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        scoreboard.reset_score()
        snake.reset_snake()
    
    # tail collision
    for part in snake.snake_body[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset_score()
            snake.reest_snake()
            
screen.exitonclick()
