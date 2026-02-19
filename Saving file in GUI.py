from tkinter import *
from tkinter import filedialog


def savefile():
    file = filedialog.asksaveasfile(initialdir="C:\\",
                                    indefaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".HTML"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text='Save', command=savefile)
text = Text(window)
text.pack()
button.pack()
window.mainloop()
