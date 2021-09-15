from tkinter import *
import time
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

def reset_time():
    ''' use itemconfig for canvas items, with the item you are changing first, and what you are changing afterwards'''
    global timer, reps
    window.after_cancel(timer)
    timer_label.config(text = "Timer")
    canvas.itemconfig(timer_text, text = "0:00")
    check_mark.config(text = '')
    reps = 0

# ----------------------x
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    shortbreak_sec = SHORT_BREAK_MIN * 60
    longbreak_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 1:
        countdown(work_sec)
        timer_label.config(text = "Time for Work!", fg = GREEN)
    elif reps % 2 == 0 and reps != 8:
        countdown(shortbreak_sec)
        timer_label.config(text = "Short break!", fg = PINK)
    else:
        reps = 0
        countdown(longbreak_sec)
        timer_label.config(text = "Long break!", fg = RED)
        


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    global reps, timer
    count_min = count // 60
    count_sec = str(count % 60)
    if len(count_sec) == 1:
        count_sec = "0" + count_sec

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        ''' initializes so that when the timer hits 0, the timer goes back'''
        start_timer()
        num_checks = reps // 2 
        check_mark.config(text = num_checks * "✔")

# ---------------------------- UI SETUP ------------------------------- #
''' initializes window '''
window = Tk()
window.title("Pomodoro App")
window.config(padx = 100, pady = 50, bg = YELLOW)

''' initializes Canvas image with layers'''
canvas = Canvas(width = 208, height = 224, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(103, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text = "0:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

'''Initializes Label for the Timer'''
timer_label = Label(text = "Timer", font = (FONT_NAME, 35, 'bold'), fg = GREEN, bg = YELLOW)
timer_label.grid(column = 1, row = 0)

''' Initializes Start Button with command start_timer '''
start_button = Button(text = "Start", fg = RED, highlightbackground = YELLOW, font = (FONT_NAME, 15, 'normal'), command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", fg = RED, highlightbackground = YELLOW, font = (FONT_NAME, 15, 'normal'), command = reset_time)
reset_button.grid(column = 2, row = 2)

check_mark = Label(fg = GREEN, bg = YELLOW, highlightthickness = 0, font = (FONT_NAME, 40, 'bold'))
check_mark.grid(column = 1, row = 3)



window.mainloop()