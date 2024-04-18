import tkinter as tk
from tkinter import ttk

root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
label1 = ttk.Label(frm, text="Hello World!", padding=10)
button1 = ttk.Button(frm, text="Quit", command=root.destroy, padding=2)

label1.grid(column=1, row=1, pady=2)
button1.grid(column=1, row=2, pady=2)

entry1 = tk.Entry(frm)
entry1.grid(column=1, row=3, pady=20)
contents = tk.StringVar()
contents.set("This is a variable")
entry1["textvariable"] = contents

def print_contents(event):
    print(contents.get())

entry1.bind('<Key-Return>', print_contents)

def print_it(event):
    print("Works!")

button2 = ttk.Button(frm,text="Submit",command=print_it, padding=10)
button2.grid(column=1, row=5, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(2, weight=1)

root.mainloop()