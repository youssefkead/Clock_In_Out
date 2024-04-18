import tkinter as tk
from tkinter import ttk
import pandas as pd
from datetime import datetime
import os

print(os.getcwd())

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

dict = {'text':[], 
        'timestamp':[]}
df = pd.DataFrame(dict)

def append_it(*args):
    df.loc[len(df.index)] = [contents.get(),datetime.now()]

entry1.bind('<Key-Return>', append_it)
button2 = ttk.Button(frm,text="Submit",command=append_it, padding=10)
button2.grid(column=1, row=5, pady=10)

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(2, weight=1)

#pandas and storing data in a csv

c = datetime.now()
current_time = c.strftime('%H:%M:%S')

# storing the current time in the variable
c2 = datetime.now().time()  # time object

print("c is", c)
print("c2 is", c2)

# Displays Time
print('Current Time is:', current_time)
print('Type(c):', type(c))

root.mainloop()

print(df)
path = "C:\\Users\\youssef\\Documents\\code_is_here"
df.to_csv(os.path.join(path,r'text_and_timestamps.csv'), sep=',', index=False, encoding='utf-8')

