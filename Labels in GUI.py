from  tkinter import *

window = Tk()
photo = PhotoImage(file='logo.png')
label = Label(window,text="Hello world",
              font=("Arial",40,'bold'),
              fg='#00ff00',
              bg="Black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='bottom')

# label.place(x=0, y=0)
label.pack()
window.mainloop()

