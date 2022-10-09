from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=1000, height=600)
screen.title("Ping-Pong")
screen.tracer(0)

l_paddle = Paddle(-480)
r_paddle = Paddle(480)
ball = Ball()
score = Score()


def go_up():
    new_y = r_paddle.ycor()
    if new_y <= 235:
        new_y += 20
        r_paddle.goto(480, new_y)


def go_down():
    new_y = r_paddle.ycor()

    if new_y >= -235:
        new_y -= 20
        r_paddle.goto(480, new_y)


def go_up_r():
    new_y = l_paddle.ycor()
    if new_y <= 235:
        new_y += 20
        l_paddle.goto(-480, new_y)


def go_down_r():
    new_y = l_paddle.ycor()

    if new_y >= -235:
        new_y -= 20
        l_paddle.goto(-480, new_y)


screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_up_r, "w")
screen.onkey(go_down_r, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detecting collision with walls

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detecting collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 420 or ball.distance(l_paddle) < 50 and ball.xcor() < -420:
        ball.bounce_x()



    if ball.xcor() > 480:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -480:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
