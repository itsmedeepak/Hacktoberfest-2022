from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.clear()
        self.goto(0, 100)
        self.write("GAME OVER", align="center", font=("Arial", 35, "normal"))
        self.goto(0, -100)
        self.update_score()


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()
