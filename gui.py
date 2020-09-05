from main import *
from tkinter import *
from tkinter import filedialog

# function to display user text when button is clicked
def clicked():
    res = "You wrote: " + txt.get()
    # name.configure(text=res)

def browse_button():
    # Allow user to select a directory and store it in global var
    # called folder_path
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)
    print(filename)

# create root window
root = Tk()

# root window title and dimension
root.title("Desk Sauce")
root.geometry('800x400')

# adding a label to the root window
name = Label(root, text="Name your cleaning folder: ")
name.grid()

browse = Label(root, text="Select location for cleaned items: ")
browse.grid(column=0, row=1)

# adding Entry Field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

browse = Button(root, text="Browse", fg="black", command=browse_button)
browse.grid(column=1, row=1)

done = Button(root, text="Gimme the sauce" , fg="black", command=clicked)
done.grid(column=1, row=10)

root.mainloop()