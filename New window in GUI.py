from tkinter import *

def create_winow():
    new_window = Tk()
    old_window.destroy()

old_window = Tk()
Button(old_window,text="Create new window",command=create_winow)

old_window.mainloop()