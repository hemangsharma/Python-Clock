from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000,time)


label = Label(root, font=("ds-digital", 100) , foreground = "black",  background = "white")
label.pack(anchor="center")
time()
root.wm_attributes("-alpha", 1)

root.mainloop()
