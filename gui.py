import tkinter as tk
root = tk.Tk()

toggle_btn = tk.Button(text="Toggle", width=12, relief="raised", command=lambda:toggle(toggle_btn))
toggle_btn.pack(pady=5)

def toggle(button: tk.Button):
    if button.config('relief')[-1] == 'sunken':
        button.config(relief="raised")
    else:
        button.config(relief="sunken")



root.mainloop()