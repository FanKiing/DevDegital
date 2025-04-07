import tkinter as tk
from ttkbootstrap import Style
from tkinter import ttk
from ttkbootstrap import Entry
from ttkbootstrap.constants import *

def on_button_click(button_value):
    if button_value == "C":
        entry_var.set("") 
    elif button_value == "=":
        try:
            result = eval(entry_var.get()) 
            entry_var.set(result)  
        except Exception as e:
            entry_var.set("Erreur")  
    else:
        entry_var.set(entry_var.get() + str(button_value))  

root = tk.Tk()
root.title("Calculatrice avec ttkbootstrap")

style = Style(theme="darkly")  

entry_var = tk.StringVar()

entry = style.Entry(master=root, textvariable=entry_var, font=("Arial", 16), justify="right", width=20) entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3),
    ("=", 5, 0, 4) 
]

for button in buttons:
    text = button[0]
    row = button[1]
    column = button[2]
    colspan = button[3] if len(button) == 4 else 1

    btn = style.Button(
        master=root, text=text, bootstyle=PRIMARY if text in "0123456789" else SUCCESS, 
        command=lambda t=text: on_button_click(t), width=5
    )
    btn.grid(row=row, column=column, columnspan=colspan, padx=5, pady=5, sticky="nsew")

for i in range(4):
    root.grid_columnconfigure(i, weight=1)
for i in range(6):
    root.grid_rowconfigure(i, weight=1)

root.mainloop()