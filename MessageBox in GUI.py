from tkinter import *
from tkinter import messagebox


def click():
    messagebox.showinfo(title="This is an info message", message='You are a person')
    messagebox.showwarning(title='Warning!', message='You have a Virus!!!!!')
    messagebox.showerror(title='Error', message='Something went wrong')
    if messagebox.askokcancel(title='ask ok cancel', message='Do you want to do the thing',icon="warning"):
        print("You did a thing")
    else:
        print("You canceled a thing :( ")

    if messagebox.askretrycancel(title='ask ok cancel', message='Do you want to retry the thing'):
        print("You retried a thing")
    else:
        print("You canceled a thing :( ")

    if messagebox.askyesno(title='Ask yes or no', message='Do you like cake'):
        print('I like cake too')
    else:
        print("Why do you not cake")

    answer = messagebox.askquestion(title='Ask question', message='Do you like pie')
    if answer == 'yes':
        print('I like pie too')
    else:
        print('Why do you not like pie')

    answer = (messagebox.askyesnocancel(title='Yes no cancel', message='Do you like to code'))
    if answer == YES:
        print("You like to code :) ")
    elif answer == NO:
        print("Then why are you watching a video of coding")
    else:
        print("You have dodged the question")


window = Tk()

button = Button(window, command=click, text='click me')
button.pack()

window.mainloop()
