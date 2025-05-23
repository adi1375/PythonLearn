import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(key="Up",fun=player.move_up)
# screen.onkey(key="Down",fun=player.move_down)
# screen.onkey(key="Left",fun=player.move_left)
# screen.onkey(key="Right",fun=player.move_right)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car_manager.create_car()
    car_manager.move_cars()
    
    if player.ycor() > 280:
        player.respawn()
        scoreboard.increase_level()
        car_manager.increase_speed()
        
    for car in car_manager.cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
            

screen.exitonclick()