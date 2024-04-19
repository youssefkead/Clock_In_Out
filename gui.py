# Python program to illustrate a stop watch 
# using Tkinter 
#importing the required libraries 
import tkinter as Tkinter 
from tkinter import ttk
from datetime import datetime, timedelta
import time

s = time.strftime("%r, %T ", time.gmtime())
#global variables
counter = datetime.now()
start_time = datetime.now()
elapsed_time = counter - start_time
time_at_stop = timedelta()
#time_at_stop = datetime.strptime("00:00:00","%H:%M:%S")

running = False

def counter_label(label):
    def count():
        if running:
            global counter
            global start_time
            global elapsed_time
            global time_at_stop
            global start_time_label
            counter = datetime.now()
            # To manage the initial delay.
            elapsed_time = counter - start_time + time_at_stop
            elapsed_time = elapsed_time - timedelta(microseconds=elapsed_time.microseconds)
            display = elapsed_time

            label['text']=display   # Or label.config(text=display)
            start_time_label['text']=start_time.strftime("%H:%M:%S")
            # label.after(arg1, arg2) delays by
            # first argument given in milliseconds
            # and then calls the function given as second argument.
            # Generally like here we need to call the
            # function in which it is present repeatedly.
            # Delays by 1000ms=1 seconds and call count again.
            label.after(500, count)
            
   
    # Triggering the start of the counter. 
    count()

# start function of the stopwatch 
def Start(label): 
    global running
    global start_time
    global counter
    global time_at_stop

    start_time = datetime.now()
    counter = start_time + time_at_stop
    running=True
    counter_label(label) 
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'

# Stop function of the stopwatch 
def Stop(): 
    global running
    global elapsed_time
    global time_at_stop
    time_at_stop = elapsed_time

    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running = False

# Reset function of the stopwatch 
def Reset(label): 
    global counter
    global start_time
    global time_at_stop
    start_time = datetime.now()
    counter = datetime.now()
    time_at_stop = timedelta()
    # If rest is pressed after pressing stop. 
    if running==False:       
        reset['state']='disabled'
        label['text']='Welcome!'
   
    # If reset is pressed while the stopwatch is running. 
    else:                
        label['text']= datetime.now() - datetime.now()
   
root = Tkinter.Tk() 
root.title("Stopwatch") 
mainframe = ttk.Frame(root)
mainframe.grid(row=1,column=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(2, weight=1)

mainframe.grid_columnconfigure(0, weight=1)
mainframe.grid_columnconfigure(2, weight=1)
mainframe.grid_rowconfigure(0, weight=1)
mainframe.grid_rowconfigure(4, weight=1)

start_time_label = ttk.Label(mainframe, text=datetime.strftime(start_time,"%H:%M:%S"))
start_time_label.grid(row=1,column=1)
# Fixing the window size. 
root.minsize(width=250, height=70) 
label = ttk.Label(mainframe, text="Welcome!", foreground="black", font="Verdana 30 bold") 
label.grid(row=2,column=1) 
f = ttk.Frame(mainframe)
start = ttk.Button(f, text='Start', width=6, command=lambda:Start(label)) 
stop = ttk.Button(f, text='Stop',width=6,state='disabled', command=Stop) 
reset = ttk.Button(f, text='Reset',width=6, state='disabled', command=lambda:Reset(label)) 
f.grid(row=3,column=1,pady=5)
start.grid(column=0,row=0) 
stop.grid(column=1,row=0) 
reset.grid(column=2,row=0) 
root.mainloop()