from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

PADDLE_RIGHT = (560,0)
PADDLE_LEFT = (-560,0)


screen = Screen()
screen.title("CLASSIC PONG")
screen.setup(height=800, width=1200)
screen.bgcolor("black")
screen.tracer(0)

paddle_right = Paddle(PADDLE_RIGHT)
paddle_left = Paddle(PADDLE_LEFT)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(key="Up",fun=paddle_right.move_up)
screen.onkeypress(key="Down",fun=paddle_right.move_down)
screen.onkeypress(key="w",fun=paddle_left.move_up)
screen.onkeypress(key="s",fun=paddle_left.move_down)

game_over = False

while not game_over:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move()

    if ball.ycor() > 380 or ball.ycor() < - 380:
        ball.bounce_y()
        
    if ball.xcor() > 530 and ball.distance(paddle_right) <50 :
        ball.bounce_x()
    
    if ball.xcor() < -530 and ball.distance(paddle_left) <50 :
        ball.bounce_x()
    
    if ball.xcor() > 580 :
        scoreboard.point_left()
        ball.bounce_x()
        ball.respawn()
        
    if ball.xcor() < -580:
        scoreboard.point_right()
        ball.bounce_x()
        ball.respawn()

screen.exitonclick()