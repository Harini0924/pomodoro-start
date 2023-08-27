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
reps=0
timer =None
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    checkmarks.config(text=" ")
    global reps
    reps =0



# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN *60
    long_break_sec = LONG_BREAK_MIN*60
    if(reps%2==0 and reps<8):
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
        reps += 1

    elif (reps % 2 != 0 and reps < 8):
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
        reps += 1

    elif (reps == 8):
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
        reps += 1



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):

    min = math.floor(count/60)
    seconds= count%60
    if seconds <10:
        seconds=(f"0{seconds}")

    canvas.itemconfig(timer_text, text=f"{min}:{seconds}")
    if count>0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        checkmarks.config(text=marks, fg=GREEN)



# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)



#Label
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME,45))
title_label.config(bg=YELLOW)
title_label.grid(column=1,row=0)


canvas = Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img =PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text= canvas.create_text(103,130, text="00:00", fill="white", font = (FONT_NAME, 35, "bold"))

canvas.grid(column=1,row=1)


#Buttons
start_button= Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0,row=2)

reset_button= Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2,row=2)

#checkmark
checkmarks= Label(text="", fg=GREEN)
checkmarks.config(bg=YELLOW)
checkmarks.grid(column=1,row=3)




window.mainloop()


