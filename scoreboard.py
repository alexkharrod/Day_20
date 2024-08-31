from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(-30, 270)
        self.score = 0
        self.write_score()


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, ALIGNMENT, FONT)
        self.score += 1
