from tkinter import Tk, Label, Canvas, PhotoImage, Button
import math
from notification import toast
import customtkinter

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#5F8D4E"
YELLOW = "#150050"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

# Reset the time to 00:00
def reset_time():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    title.config(text="Timer", fg=GREEN)
    check_mark.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

# Show window on the screen
def popup():
    window.deiconify()
    
# Start de time 
def start_time():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps >= 1:

        if reps % 8 == 0:
            count_douwn(long_break_sec)
            title.config(text="Break", fg=RED)
            toast.msg = "Back to work!"
            popup()
        elif reps % 2 == 0:
            count_douwn(short_break_sec)
            title.config(text="Break", fg=PINK)
            toast.msg = "Back to work!"
            popup()
        else:
            count_douwn(work_sec)
            title.config(text="Work", fg=GREEN)
            toast.msg = "Take a 5 minutes break!"
            if reps == 7:
                toast.msg = "Take a long pause of 20 minutes break!"
            popup()
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Show the time in the window
def count_douwn(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"      


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_douwn, count - 1)
        if count == 2:
            toast.show()
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)
        

# ---------------------------- UI SETUP ------------------------------- #

# Create the window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Title
title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
title.grid(column=1, row=0)

# Check Mark
check_mark = Label(font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

# Image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=("Orbitron", 25, "bold"))
canvas.grid(column=1, row=1)

# Start Button
start_button = customtkinter.CTkButton(master=window, text="Start", command=start_time)
start_button.grid(column=0, row=2)

# Reset Button
reset_button = customtkinter.CTkButton(master=window, text="Reset", command=reset_time)
reset_button.grid(column=2, row=2)

window.mainloop()
