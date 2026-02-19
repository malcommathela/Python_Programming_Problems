from tkinter import *


def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print("You have ordered: ")
    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entryBox.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)


window = Tk()

listbox = Listbox(window,
                  bg='#f7ffde',
                  font=("Arial", 30),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'soup')
listbox.insert(4, 'salad')
listbox.insert(5, 'garlic soup')

entryBox = Entry(window)
entryBox.pack()

addButton = Button(window, text='Submit', command=add)
addButton.pack()

submitButton = Button(window, text='Submit', command=submit)
submitButton.pack()

deleteButton = Button(window, text='Submit', command=delete)
deleteButton.pack()

window.mainloop()
