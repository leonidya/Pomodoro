from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.6
SHORT_BREAK_MIN = 0.10
LONG_BREAK_MIN = 0.20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_sign_label.config(text="")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sek = round(WORK_MIN*60)
    short_break_min = round(SHORT_BREAK_MIN*60)
    long_break_min = round(LONG_BREAK_MIN*60)
    if reps % 8 ==0:
        count_down(long_break_min)
        timer_label.config(text="L.BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        timer_label.config(text="S.BREAK", fg=PINK)
    else:
        count_down(work_sek)
        timer_label.config(text="WORK", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec=f"{count_sec}0"
    elif count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        check_marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            check_marks += "✔"
        check_sign_label.config(text=check_marks)
# ---------------------------- UI SETUP ------------------------------- #
# TODO: Create a window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# # TODO: TIME - after


# TODO: Create a canvas
tomato_img = PhotoImage(file="tomato.png")
canvas = Canvas( width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)

# TODO: Time label
timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
timer_label.grid(column=2, row=0)

# TODO: Check mark
check_mark = "✔"
check_sign_label = Label(fg=GREEN, bg=YELLOW)
check_sign_label.grid(column=2, row=4)

# TODO: Start_button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)
# TODO: Reset_button
reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=3, row=3)



window.mainloop()