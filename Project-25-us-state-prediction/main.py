import turtle
import pandas

screen = turtle.Screen()
screen.title("US state game")
img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)
screen.setup(width=725, height=500)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
x_cor = data.x.to_list()
y_cor = data.y.to_list()
print(state_list)
print(x_cor)
print(y_cor)


guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title="Guess the state", prompt="What's another states name? ")
    if answer_state in state_list:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[answer_state == data.state]
        t.goto(float(state_data.x), float(state_data.y))
        t.write(answer_state)

screen.exitonclick()
