from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = -1
        self.penup()
        self.goto(-290, 260)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score}", align="left", font=FONT)
