import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
label1 = ttk.Label(frm, text="Hello World!")
button1 = ttk.Button(frm, text="Quit", command=root.destroy)

label1.grid(column=0, row=0)
button1.grid(column=1, row=0)

entry1 = tk.Entry()
entry1.grid()
contents = tk.StringVar()
contents.set("This is a variable")
entry1["textvariable"] = contents

def print_contents(event):
    print(contents.get())

entry1.bind('<Key-Return>', print_contents)

root.mainloop()