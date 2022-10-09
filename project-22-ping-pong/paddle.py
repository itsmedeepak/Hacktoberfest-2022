from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.color("#6f03fc")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_cor, 0)


'''paddle = Turtle("square")
paddle.color("#6f03fc")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(480, 0)'''
