from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        label.config(text="Break", fg=RED)

    elif reps % 2 == 0:
        count_down(short_break)
        label.config(text="Break", fg=GREEN)
    else:
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    sec = count % 60
    global timer
    minute = math.floor(count / 60)
    if sec < 10:
        sec = f"0{sec}"
    if minute < 10:
        minute = f"0{minute}"
    canvas.itemconfig(timer_text, text=f"{minute}:{sec}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps / 2)):
            marks += "✓"
        label_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomoderg")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)

timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))
label.grid(column=1, row=0)

btn_start = Button(text="Start", command=start_timer, highlightthickness=0)
btn_start.grid(column=0, row=2)

btn_reset = Button(text="Reset", highlightthickness=0, command=reset)
btn_reset.grid(column=2, row=2)

label_mark = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
label_mark.grid(column=1, row=2)
window.mainloop()
