from main import *
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Desk Sauce")
root.geometry('800x400')

# adding a label to the root window
lbl = Label(root, text = "Name your cleaning folder: ")
lbl.grid()

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column =1, row =0)


# function to display user text when
# button is clicked
def clicked():

    res = "You wrote: " + txt.get()
    lbl.configure(text = res)

# button widget with red color text inside
btn = Button(root, text = "Gimme the sauce" ,
             fg = "red", command=clicked)

btn.grid(column=3, row=10)

root.mainloop()