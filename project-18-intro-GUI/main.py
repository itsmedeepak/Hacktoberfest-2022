import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.width(8)


# colors = ["#DF9FCD", "#5C256F", "#CDC06A", "#3C5C1F", "#B494DB", "#246B66", "#9FC6DF", "#ABE3B7", "#AF9FDF",
# "#588E2F", "#953288", "#C2477A", "#A7C85B"]
def colors():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.color(r, g, b)


direction = [0, 90, 180, 270]
'''

def draw_shape(num):
    angle = 360 / num
    for i in range(num):
        timmy.fd(100)
        timmy.color(colors[i])
        timmy.rt(angle)


for i in range(3, 11):
    draw_shape(i)

screen = t.Screen()
screen.exitonclick()
'''

for i in range(200):
    timmy.fd(30)
    timmy.setheading(random.choice(direction))
    colors()
