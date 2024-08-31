from turtle import Turtle

STARTING_POSITIONS = [0, -20, -40]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position,0)
            self.segments.append(new_segment)



    def snake_move(self):
        for snake in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[snake -1].xcor()
            new_y = self.segments[snake - 1].ycor()
            self.segments[snake].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)