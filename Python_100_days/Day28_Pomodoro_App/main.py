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
REPS = 0
TIMER = NONE

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(TIMER)
    count_min = 0
    count_sec = 0
    global REPS
    REPS = 0
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    label_timer.config(text="TIMER", fg=RED)
    label_checkmark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    work_time = WORK_MIN
    short_break_time = SHORT_BREAK_MIN
    long_break_time = LONG_BREAK_MIN
    REPS+=1
    if REPS%8 == 0:
        label_timer.config(text="BREAK",fg=GREEN)
        countdown(long_break_time * 60)
    elif REPS%2 != 0:
        label_timer.config(text="WORK",fg=RED)
        countdown(work_time * 60)
       
    elif REPS%2 == 0:
        label_timer.config(text="BREAK",fg=PINK)
        countdown(short_break_time * 60)
        
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global TIMER
    count_min = math.floor(count/60)
    count_sec = count % 60
    
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
       TIMER = window.after(1000,countdown,count-1)
    else:
        start_timer()
        work_sessions = math.floor(REPS/2)
        for _ in range(work_sessions):
            label_checkmark.config(text="✓"*work_sessions)
        
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="Python_100_days/Day28_Pomodoro_App/tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text = canvas.create_text(102,130, text="00:00",fill="white",font=(FONT_NAME,40,"bold"))
canvas.grid(row=1,column=1)


label_timer = Label(text="TIMER",font=("Courier", 40, "bold"),bg=YELLOW,fg=RED)
label_timer.grid(row=0,column=1)


label_checkmark =Label(text="",fg=GREEN,font=(FONT_NAME,16,"bold"),bg=YELLOW)
label_checkmark.grid(row=3,column=1)
label_checkmark.config(padx=10,pady=30)

button_start =Button(text="START",bg=PINK,fg="white",font=("Helvetica",10,"bold"),command=start_timer)
button_start.grid(row=2,column=0) 

button_reset =Button(text="RESET",bg=PINK,fg="white",font=("Helvetica",10,"bold"),command=reset_timer)
button_reset.grid(row=2,column=2)

window.mainloop()