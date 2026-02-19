from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(count)
    # print("You clicked the button")


window = Tk()

photo = PhotoImage(file='logo.png')

button = Button(window,
                text="Click me!",
                command=click,
                font=("Comic sans", 30),
                fg="#00ff00",
                bg='black',
                activeforeground='#00ff00',
                activebackground='black',
                state=ACTIVE,
                image=photo,
                compound='bottom')
button.pack()

window.mainloop()
