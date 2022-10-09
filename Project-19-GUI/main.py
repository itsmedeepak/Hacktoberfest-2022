from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
usr_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win this race? Enter a color")
color = ["red", "yellow", "orange", "blue", "green", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
turtle_list = []
screen.listen()

for i in range(0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color[i])
    turtle_list.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])

is_race_on = True
while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == usr_bet:
                print(f"You've won. The {wining_color} turtle is the winner")
            else:
                print(f"You've lost. The {wining_color} turtle is the winner")

        distance = random.randint(0, 10)
        turtle.fd(distance)

screen.exitonclick()
