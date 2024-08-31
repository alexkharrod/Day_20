from idlelib.colorizer import color_config
from turtle import Turtle, Screen




class Snake:
    segments = []
    starting_positions = [0, -20, -40]

    def __init__(self):


        for position in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(Snake.starting_positions[position], 0)
            Snake.segments.append(new_segment)



    def snake_move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = Snake.segments[snake -1].xcor()
            new_y = Snake.segments[snake - 1].ycor()
            Snake.segments[snake].goto(new_x, new_y)
        Snake.segments[0].forward(20)