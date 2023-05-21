from tkinter import *
import math

PINK = "#e2979c"
RED = "#E7305b"
GREEN = "#9bdeac"
YELLOW = "#f7F5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0

def reset_timer():
    window.after_cancel(timer)




def start_timer():
    global reps
    reps += 1


    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg = GREEN)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg = PINK, font=(FONT_NAME,40, "bold"))


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down,count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps / 2)
        for a in range(work_sessions):
            marks += "ok"
        check_marks.config(text=marks)

window = Tk()
window.title("pomodoro")
window.config(padx= 100, pady=50, bg=YELLOW)

title_label = Label(text="Timer",fg=GREEN, font=(FONT_NAME,40, "italic"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=600, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="fresher.gif")
canvas.create_image(250, 240, image=tomato_img)
timer_text = canvas.create_text(300, 140, text='00:00', fill= "blue", font=(FONT_NAME,40, "bold"))
canvas.grid(column=1, row=1)


start_button = Button(text="start" ,command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="pause", command = reset_timer)
reset_button.grid(column=2, rows=2)
#add reset

check_marks = Label(text="ok",fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
