import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

class SystemeDeGestionDeRestaurant:
    def __init__(self, root):
        self.root = root
        self.root.title("Systeme De Gestion De Restaurant Marocain")
        self.root.geometry("800x400")

        self.menu = {
            "Couscous": 50,
            "Tajine": 70,
            "Pastilla": 80,
            "Briouates": 40,
            "Harira": 25,
            "Thé": 15,
            "Café": 20
        }

        self.item_vars = {}

        

        menu_frame = tk.Frame(root, bd=10, relief=tk.GROOVE)
        menu_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        tk.Label(menu_frame, text="Menu", font=("Arial", 16, "bold"), fg="blue").pack()

        self.cost_label = {}

        for item, price in self.menu.items():
            frame = tk.Frame(menu_frame)
            frame.pack(anchor="w")

            tk.Label(frame, text=f"{item} Rs.{price}", font=("Arial", 12)).pack(side=tk.LEFT)

        self.bill_frame = tk.Frame(self.root, bd=10, relief=tk.GROOVE)
        self.bill_frame.pack_forget()

        tk.Label(self.bill_frame, text="Facture", font=("Arial", 16, "bold"), fg="blue").pack()
        

        self.bill_text = {
            "Numéro de Facture": tk.StringVar(value=str(random.randint(10000, 99999))),
            "Date": tk.StringVar(value=datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
            "Coût": tk.StringVar(),
            "Frais de Service": tk.StringVar(),
            "Taxe": tk.StringVar(),
            "Total": tk.StringVar()
        }

        for key, value in self.bill_text.items():
            frame = tk.Frame(self.bill_frame)
            frame.pack(anchor="w")

            tk.Label(frame, text=key, font=("Arial", 12, "bold"), width=15, anchor="w").pack(side=tk.LEFT)
            tk.Entry(frame, textvariable=value, font=("Arial", 12, "bold"), bg="lightyellow").pack(side=tk.LEFT)

        tk.Button(self.root, text="Générer la Facture", command=self.generer_facture, font=("Arial", 12, "bold"), bg="lightblue").pack(pady=10)

    def generer_facture(self):
        self.bill_frame.pack()
        cout_total = sum(self.menu[item] * quantity for item, quantity in self.cost_label.items())
        frais_service = round(cout_total * 0.05, 2)
        taxe = round(cout_total * 0.18, 2)
        total = cout_total + frais_service + taxe

        self.bill_text["Coût"].set(f"Rs.{cout_total}")
        self.bill_text["Frais de Service"].set(f"Rs.{frais_service}")
        self.bill_text["Taxe"].set(f"Rs.{taxe}")
        self.bill_text["Total"].set(f"Rs.{total}")

        messagebox.showinfo("Facture", "La facture a été générée avec succès.")

if __name__ == "__main__":
    root = tk.Tk()
    app = SystemeDeGestionDeRestaurant(root)
    root.mainloop()