import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def load_image():
    path = entry.get()
    try:
        img = Image.open(path)
        img = img.resize((300, 300))
        img_tk = ImageTk.PhotoImage(img)
        image_label.config(image=img_tk)
        image_label.image = img_tk
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger l'image : {e}")

# Interface
root = tk.Tk()
root.title("Afficheur d'Images")

tk.Label(root, text="Chemin de l'image :").pack(pady=5)
entry = tk.Entry(root, width=50)
entry.pack(pady=5)

button = tk.Button(root, text="Charger", command=load_image)
button.pack(pady=5)

image_label = tk.Label(root)
image_label.pack(pady=10)

root.mainloop()
