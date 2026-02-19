from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

window = Tk()  # INSTANTIATE AN INSTANCE OF A WINDOW
window.geometry("420x420")
window.title("Malcom")


icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
window.config(background="#C424F5")

window.mainloop()  # place window on computer screen
