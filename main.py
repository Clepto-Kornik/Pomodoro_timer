import tkinter
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


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")
    label2.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 != 0:
        count_down(work_sec)
        reps += 1
        label1.config(text="Work", fg=GREEN)
    elif reps % 8 == 0:
        count_down(short_break_sec)
        reps = 0
        label1.config(text="Short break", fg=PINK)
    elif reps % 2 == 0:
        count_down(long_break_sec)
        reps += 1
        label1.config(text="Long break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic Typing
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        label2.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)  # no white frame
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

label1 = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 48, "bold"))
label1.grid(column=1, row=0)

label2 = tkinter.Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 18, "bold"))
label2.grid(column=1, row=3)

button1 = tkinter.Button(text="Start", bg=PINK, fg=RED, font=(FONT_NAME, 16), highlightthickness=0, command=start_timer)
button1.grid(column=0, row=2)

button2 = tkinter.Button(text="Reset", bg=PINK, fg=RED, font=(FONT_NAME, 16), highlightthickness=0, command=reset_timer)
button2.grid(column=2, row=2)

window.mainloop()
