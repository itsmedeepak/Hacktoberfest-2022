import turtle as t
import random

timmy = t.Turtle()
timmy.speed(20)

t.colormode(255)


def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


direction = [0, 90, 180, 270]
for i in range(360):
    colors()
    timmy.circle(100)
    curr_head = timmy.heading()
    timmy.setheading(curr_head + 5)
