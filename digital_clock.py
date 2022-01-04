from tkinter import *
from time import strftime

root = Tk()
root.title("Clock")
lbl = Label(root, font=('callibri', 45, "bold"),
            background = 'black',
            foreground = 'white')


def time():
    stringtime = strftime('%H:%M:%S %p')
    lbl.config(text=stringtime)
    lbl.after(1000, time)

lbl.pack(anchor='center')
time()

mainloop()