from tkinter import *


def submit():
    print("The temperature is: " + str(scale.get()) + 'degrees C')


window = Tk()

hotimage = PhotoImage(file='logo2.png')
hotLabel = Label(image=hotimage)
hotLabel.pack()

scale = Scale(window,
              from_=100,
              to=0,
              orient=VERTICAL,
              length=400,
              font=("Arial",20),
              tickinterval=5,# add numeric indicators for value
              resolution=5,
              troughcolor='#69faff',
              fg='#ff1c00',
              bg="#111111"
              )
scale.pack()
scale.set(((scale['from']-scale['to'])/2)+scale['to'])

coldimage = PhotoImage(file='logo1.png')
coldLabel = Label(image=coldimage)
coldLabel.pack()
button = Button(window, text='Submit', command=submit)
button.pack()
window.mainloop()
