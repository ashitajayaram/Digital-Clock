from tkinter import Tk
from tkinter import Label
import time

root=Tk()
root.title("Clock")

def current_time():
    displaytime=time.strftime("%I:%M:%S %p")
    digi_clock.config(text=displaytime)
    digi_clock.after(200,current_time)

digi_clock = Label(root, font=("Times New Roman", 120), bg="pink", fg="silver")
digi_clock.pack()

current_time()

root.mainloop()
