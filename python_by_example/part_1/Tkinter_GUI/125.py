from tkinter import *
import random

def roll_die():
    num = random.randint(1, 6)
    answer["text"] = num

def clear_result():
    answer["text"] = ""

w = Tk()
w.title("DIE ROLLER")
w.geometry("250x200")

button1 = Button(text="Roll", command=roll_die)
button1.place(x=65, y=165, width=50, height=25)
button1["bg"] = "black"
button1["fg"] = "white"

clear_button = Button(text="Clear", command=clear_result)
clear_button.place(x=125, y=165, width=50, height=25)
clear_button["bg"] = "black"
clear_button["fg"] = "white"

answer = Message(text="", font=("arial", 35))
answer.place(x=50, y=10, width=150, height=150)
answer.configure(font = ("arial", 100))
answer["bg"] = "black"
answer["fg"] = "white"

w.mainloop()