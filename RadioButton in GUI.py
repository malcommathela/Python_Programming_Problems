from tkinter import *

def order():
    if x.get()==0:
        print("You ordered pizza")

    elif x.get()==1:
        print("You ordered hamburger")

    elif x.get()==2:
        print("You ordered hotdog")

    else:
        print("huh?")
food = ['pizza', 'hamburger', 'hot dog']
window = Tk()
pizzaImage = PhotoImage(file='logo.png')
hamburgerImage = PhotoImage(file='logo.png')
hotdogImage = PhotoImage(file='logo.png')
foodImages = [pizzaImage,hamburgerImage,hotdogImage]
x = IntVar
for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],
                               variable=x, # groups radiobutton together if they share a single variable
                               value=index, # assigns each radiobutton a different value
                               padx=25,
                               font=('Impact', 50),
                               image=foodImages[index],
                               compound ='Left',
                               command=order,
                               indicatoron=0,
                               width=375 # sets width of radiobutons)
    radio_button.pack(anchor=w)
window.mainloop()
