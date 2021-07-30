from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_fwd():
    timmy.fd(10)


def move_back():
    timmy.fd(-10)


def turn_left():
    head = timmy.heading() + 10
    timmy.lt(head)


def turn_right():
    head = timmy.heading() - 10
    timmy.rt(head)


screen.listen()
screen.onkey(key="w", fun=move_fwd)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=move_fwd)

screen.exitonclick()
