from turtle import Turtle

SNAKE_BODY_SIZE = 3
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
               
        
    def create_snake(self):
        x_axis = 0
        for i in range(SNAKE_BODY_SIZE):
            self.snake_body.append(Turtle(shape="square"))
            self.snake_body[i].penup()
            self.snake_body[i].color("white")
            self.snake_body[i].goto(x=x_axis,y=0)
            x_axis-=20
        
        
    def move(self):
        for part in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[part-1].xcor()
            new_y = self.snake_body[part-1].ycor()
            self.snake_body[part].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
    
    
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
        
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        