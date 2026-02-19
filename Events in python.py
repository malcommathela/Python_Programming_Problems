from tkinter import *


def dosomething(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)


window = Tk()

window.bind("<Key>", dosomething) # (event, function)

label = Label(window, font=("Segue", 100))
label.pack()

window.mainloop()
