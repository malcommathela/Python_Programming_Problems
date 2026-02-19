from tkinter import *
from tkinter import filedialog


def openfile():
    print("File has been opened")


def savefile():
    print("File has been saved")


def cut():
    print("You cut some text")


def copy():
    print("You copied some text")


def paste():
    print("You pasted some text")


window = Tk()
fileImage = PhotoImage(file="file.png")
saveImage = PhotoImage(file="save.png")
exitImage = PhotoImage(file="exit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=('MW Boli', 15))
menubar.add_cascade(label='File',menu=fileMenu)
fileMenu.add_command(label='Open', command=openfile, image=fileImage, compound="left")
fileMenu.add_command(label='Save', command=savefile, image=saveImage, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label='Exit', command=quit, image=exitImage, compound="left")

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label='Cut', command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label='paste', command=paste)

window.mainloop()
