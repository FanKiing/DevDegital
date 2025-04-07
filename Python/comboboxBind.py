import tkinter as tk
from tkinter import ttk

def change_color(event):
    color = combo.get()
    colors = {"Rouge": "red", "Vert": "green", "Bleu": "blue", "Jaune": "yellow"}
    root.config(bg=colors.get(color, "white"))

# Interface
root = tk.Tk()
root.title("Changer Couleur")
root.geometry("300x200")

tk.Label(root, text="Choisissez une couleur :").pack(pady=5)
combo = ttk.Combobox(root, values=["Rouge", "Vert", "Bleu", "Jaune"], state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", change_color)

root.mainloop()
