from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

entry1 = Entry()
entry1.grid()
contents = StringVar()
contents.set("This is a variable")
entry1["textvariable"] = contents

def print_contents(event):
    print(contents.get())

entry1.bind('<Key-Return>', print_contents)

root.mainloop()