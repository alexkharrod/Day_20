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
        self.high_score = 0
        self.write_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"Game Over", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.write_score()
        self.score = 0


    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
