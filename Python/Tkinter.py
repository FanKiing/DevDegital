#ex1
import tkinter as tk
from tkinter import ttk

def calculer_double():
    try:
        nombre = int(entry_nombre.get())
        double = 2 * nombre
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(0, f"{double}")
    except ValueError:
        entry_resultat.delete(0, tk.END)
        entry_resultat.insert(0, "Erreur")

fenetre = tk.Tk()
fenetre.title("Double d'un Nombre")

label_nombre = tk.Label(fenetre, text="Entrer N")
label_nombre.grid(row=0, column=0, padx=10, pady=10)

entry_nombre = tk.Entry(fenetre)
entry_nombre.grid(row=0, column=1, padx=10, pady=10)

label_resultat = tk.Label(fenetre, text="Le double de N =")
label_resultat.grid(row=1, column=0, padx=10, pady=10)

entry_resultat = tk.Entry(fenetre)
entry_resultat.grid(row=1, column=1, padx=10, pady=10)

bouton_valider = ttk.Button(fenetre, text="Valider l'opération", command=calculer_double)
bouton_valider.grid(row=2, column=0, columnspan=2, pady=10)

fenetre.mainloop()

#ex2

import tkinter as tk

def find_divisors():
    try:
        n = int(entry.get())
        divisors = [str(i) for i in range(1, n + 1) if n % i == 0]
        result_label.config(text="Diviseurs de N : " + " ".join(divisors))
    except ValueError:
        result_label.config(text="Veuillez entrer un entier valide.")

root = tk.Tk()
root.title("Diviseurs d'un Nombre")

tk.Label(root, text="Entrer la valeur de N").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root)
entry.grid(row=0, column=1, padx=10, pady=10)

validate_button = tk.Button(root, text="Valider l'opération", command=find_divisors)
validate_button.grid(row=1, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Diviseurs de N :")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

#ex3


