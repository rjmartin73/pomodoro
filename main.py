from tkinter import *
import time

# ----------------------------- CONSTANTS ----------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK = 5
LONG_BREAK = 20
CHECK = "✓"

# ----------------------------- TIMER RESET ----------------------------- #


def timer_reset():
    canvas.delete(2)
    canvas.itemconfig(timer_text, text="00:00")
    canvas.update()

    pass


# ----------------------------- TIMER MECHANISM ----------------------------- #
def timer_mechanism():
    cycles = 0
    while cycles <= 4:
        countown_mechanism(1)
        countown_mechanism(1)
        cycle_label.config(text=CHECK * cycles)
        canvas.update()
        cycles += 1


# ----------------------------- COUNTDOWN MECHANISM ----------------------------- #
def countown_mechanism(minutes: int):
    minutes = minutes
    seconds = -1

    while minutes >= 0:
        while seconds > 0:
            time.sleep(1)
            seconds -= 1
            canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
            canvas.itemconfig(bg)
            canvas.update()
        minutes -= 1
        seconds = 59
        canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")


# ----------------------------- UI SETUP ----------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=75, pady=50, background=YELLOW)

# background image
bg_img = PhotoImage(file="tomato.png")

work_break_label = Label(text="Timer", font=(FONT_NAME, 35, "normal"), background=YELLOW,
                         foreground=GREEN)
work_break_label.grid(row=0, column=1)

# canvas
canvas = Canvas(window, width=200, height=224, highlightthickness=0,)
canvas.config(background=YELLOW,)
canvas.grid(row=1, column=1, )
bg = canvas.create_image(100, 112, image=bg_img,)
timer_text = canvas.create_text(100, 130, text="00:05", fill="white", font=(FONT_NAME, 35, "bold"))



# Buttons

start_button = Button(window, text="Start", bg=YELLOW, highlightthickness=0, borderwidth=0,
                      command=timer_mechanism)
reset_button = Button(window, text="Reset", bg=YELLOW, highlightthickness=0, borderwidth=0,
                      command=timer_reset)

cycle_label = Label(anchor="center", text=f"{CHECK}", font=(FONT_NAME, 30, "bold"),
                    background=YELLOW, foreground="green", padx=5, pady=4)
start_button.grid(row=2, column=0)
cycle_label.grid(row=2, column=1, )
reset_button.grid(row=2, column=2, )



if __name__ == '__main__':
    window.mainloop()
