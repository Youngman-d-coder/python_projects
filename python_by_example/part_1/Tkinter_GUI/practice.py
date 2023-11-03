from tkinter import *
import random

def click():
    num = random.randint(1, 6)
    answer["text"] = num

w = Tk()
w.title("DIE ROLLER")
w.geometry("200x200")

button1 = Button(text = "Roll", command = click)
button1.place(x = 30, y = 30, width = 50, height = 25)

answer = Message(text = "")
answer.place(x = 40, y = 70, width = 80, height = 80)
answer["bg"] = "white"
answer["fg"] = "black"
answer

w.mainloop()