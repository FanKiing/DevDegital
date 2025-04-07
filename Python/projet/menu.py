import tkinter as tk
from tkinter import font as tkfont
from CrudApp import CrudApp

def ouvrir_crud_app():
    CrudApp()

def ouvrir_fichiers():
    print("Option Fichiers sélectionnée.")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Menu Principal")

    root.configure(bg="#f4f4f9")

    custom_font = tkfont.Font(family="Helvetica", size=12, weight="bold")

    label = tk.Label(root, text="Menu Principal", font=("Helvetica", 18, "bold"), bg="#f4f4f9", fg="#333")
    label.pack(pady=20)

    bouton_crud_app = tk.Button(
        root, 
        text="CRUD App", 
        command=ouvrir_crud_app, 
        font=custom_font, 
        bg="#4CAF50", 
        fg="white", 
        relief="flat", 
        height=2, 
        width=20, 
        activebackground="#45a049"
    )
    bouton_crud_app.pack(pady=10)

    bouton_fichiers = tk.Button(
        root, 
        text="Fichiers", 
        command=ouvrir_fichiers, 
        font=custom_font, 
        bg="#2196F3", 
        fg="white", 
        relief="flat", 
        height=2, 
        width=20, 
        activebackground="#0b7dda"
    )
    bouton_fichiers.pack(pady=10)

    root.geometry("400x250")
    root.eval('tk::PlaceWindow %s center' % root.winfo_toplevel())

    root.mainloop()

