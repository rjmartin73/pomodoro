from tkinter import (Tk, Canvas, Label, Button, PhotoImage)
from playsound import playsound
from pathlib import Path

# ----------------------------- CONSTANTS ----------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = .1
SHORT_BREAK = 7
LONG_BREAK = 20
CHECK = "✓"
cycles = 0
timer = None
file_path = Path("./files/")
bg_img = str(file_path / "tomato.png")
sound_file = str(file_path / "Computer_Magic.mp3")

print(bg_img)
print(sound_file)


# ----------------------------- TIMER RESET ----------------------------- #
def timer_reset():
    global cycles
    window.after_cancel(timer)
    work_break_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    cycles = 0
    window.update()


# ----------------------------- TIMER MECHANISM ----------------------------- #
def timer_mechanism():
    global cycles
    cycles += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK * 60
    long_break_secs = LONG_BREAK * 60

    if cycles % 8 > 0:
        if cycles % 2 > 0:
            work_break_label.config(text="Work", fg=GREEN)
            countown_mechanism(int(work_secs))
        else:
            work_break_label.config(text="Break", fg=PINK)
            countown_mechanism(int(short_break_secs))
    else:
        work_break_label.config(text="Break", fg=RED)
        countown_mechanism(int(long_break_secs))


# --------------------------- COUNTDOWN MECHANISM --------------------------- #
def countown_mechanism(secs: int):
    minutes = secs // 60
    seconds = secs % 60
    canvas.itemconfig(timer_text, text=f"{minutes :02d}:{seconds :02d}")
    if secs > 0:
        global timer
        timer = window.after(1000, countown_mechanism, secs - 1)
    else:
        window.lift()
        window.update()
        window.attributes('-topmost', True)
        window.update()
        window.attributes('-topmost', False)
        window.update()
        playsound(sound_file)
        cycle_label.config(text=f"{CHECK * (cycles // 2)}")
        timer_mechanism()


# ----------------------------- UI SETUP ----------------------------- #
# window
window = Tk()
window.title("Pomodoro")
window.config(padx=75, pady=50, background=YELLOW)

# background image
bg_img = PhotoImage(file=bg_img)
work_break_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"),
                         background=YELLOW, foreground=GREEN)
work_break_label.grid(row=0, column=1)

# canvas
canvas = Canvas(window, width=200, height=224, highlightthickness=0,)
canvas.config(background=YELLOW,)
canvas.grid(row=1, column=1, )

bg = canvas.create_image(100, 112, image=bg_img,)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 25, "bold"))

# Buttons
start_stop = "Start"
start_button = Button(window, text=start_stop, highlightthickness=0,
                      borderwidth=0, command=lambda: timer_mechanism())
reset_button = Button(window, text="Reset", highlightthickness=0,
                      borderwidth=0, command=timer_reset)

cycle_label = Label(anchor="center", text="", font=(FONT_NAME, 30, "bold"),
                    background=YELLOW, foreground="green", padx=5, pady=4)

start_button.grid(row=2, column=0)
cycle_label.grid(row=2, column=1, )
reset_button.grid(row=2, column=2, )
window.lift()
window.attributes('-topmost', True)
window.update()
window.attributes('-topmost', False)

if __name__ == '__main__':
    window.mainloop()
