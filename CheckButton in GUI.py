from tkinter import *


def display():
    if (x.get() == 1):
        print("You agree")
    else:
        print("You don't agree")


window = Tk()

x = IntVar()

python_photo = PhotoImage(file='logo.png')

check_button = Checkbutton(window,
                           text='I agree to something',
                           variable=x,
                           offvalue=0,
                           command=display,
                           font=('Arial',20),
                           fg='#00ff00',
                           bg='black',
                           activebackground='black',
                           activeforeground='#00ff00',
                           pady=10,
                           padx=25,
                           image=python_photo)
check_button.pack()

window.mainloop()
