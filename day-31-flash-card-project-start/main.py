from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=images_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=images_back)
    canvas.config()


window = Tk()
window.title("Flashy Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=524, bg=BACKGROUND_COLOR)
images_front = card_front_img = PhotoImage(file="images/card_front.png")
images_back = PhotoImage(file="images/card_back.png")
card_bg = canvas.create_image(400, 265, image=images_front)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
next_card()

right_btn_image = PhotoImage(file="images/right.png")
wrong_btn_image = PhotoImage(file="images/wrong.png")

wrong_btn = Button(image=wrong_btn_image, highlightthickness=0, command=next_card)
wrong_btn.grid(row=1, column=0)

right_btn = Button(image=right_btn_image, highlightthickness=0, command=flip_card)
right_btn.grid(row=1, column=1)

window.mainloop()
