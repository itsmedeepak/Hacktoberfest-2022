from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.l_score = -1
        self.r_score = -1
        self.l_point()
        self.r_point()

    def update(self, l_score, r_score):
        self.clear()
        self.goto(-100, 240)
        self.write(l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 240)
        self.write(r_score, align="center", font=("courier", 40, "normal"))

    def l_point(self):
        self.l_score += 1
        self.goto(-100, 240)
        self.update(self.l_score, self.r_score)

    def r_point(self):
        self.r_score += 1
        self.update(self.l_score, self.r_score)