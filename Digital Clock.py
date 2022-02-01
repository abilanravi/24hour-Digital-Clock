import time
import sys
from tkinter import Tk
from tkinter import Label
#importing time and sys modules to help make the clock
#Tk for the screen and Label to use words

master_screen = Tk()
master_screen.title("Abilan's Digital Clock")

def get_time():
    timevari = time.strftime("%H:%M:%S %p")
    clock.config(text=timevari)
    clock.after(100,get_time)

Label(master_screen, font=("Times New Roman", 35), text="Abilan's Digital Clock", bg="yellow", fg="black").pack()
clock = Label(master_screen, font=("Impact",90), bg="yellow", fg="black")
clock.pack()

get_time()

master_screen.mainloop()
