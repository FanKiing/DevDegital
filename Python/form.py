import tkinter as tk
from tkinter import ttk
from abc import ABC, abstractmethod
import math

# Classe abstraite Forme
class Forme(ABC):
    @abstractmethod
    def surface(self):
        pass

    @abstractmethod
    def perimetre(self):
        pass

    def volume(self):
        return "Non applicable"  # Par défaut, pas de volume pour ces formes.

# Classe Rectangle
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def surface(self):
        return self.largeur * self.hauteur

    def perimetre(self):
        return 2 * (self.largeur + self.hauteur)

# Classe Cercle
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def surface(self):
        return math.pi * self.rayon ** 2

    def perimetre(self):
        return 2 * math.pi * self.rayon

    def volume(self):
        return (4 / 3) * math.pi * self.rayon ** 3

# Fonction pour afficher le bon frame selon la forme choisie
def afficher_frame_forme():
    if choix_forme.get() == "Rectangle":
        frame_rectangle.pack(fill="x", pady=10)
        frame_cercle.pack_forget()
    elif choix_forme.get() == "Cercle":
        frame_cercle.pack(fill="x", pady=10)
        frame_rectangle.pack_forget()

# Fonction pour effectuer les calculs
def calculer():
    calcul = choix_calcul.get()
    forme = choix_forme.get()

    try:
        if forme == "Rectangle":
            largeur = float(entry_largeur.get())
            hauteur = float(entry_hauteur.get())
            rect = Rectangle(largeur, hauteur)
            if calcul == "Surface":
                result_label.config(text=f"Surface : {rect.surface():.2f}")
            elif calcul == "Périmètre":
                result_label.config(text=f"Périmètre : {rect.perimetre():.2f}")
            else:
                result_label.config(text="Volume non applicable pour un rectangle.")
        elif forme == "Cercle":
            rayon = float(entry_rayon.get())
            cercle = Cercle(rayon)
            if calcul == "Surface":
                result_label.config(text=f"Surface : {cercle.surface():.2f}")
            elif calcul == "Périmètre":
                result_label.config(text=f"Périmètre : {cercle.perimetre():.2f}")
            elif calcul == "Volume":
                result_label.config(text=f"Volume : {cercle.volume():.2f}")
    except ValueError:
        result_label.config(text="Erreur : Veuillez entrer des valeurs valides.")

# Interface graphique Tkinter
root = tk.Tk()
root.title("Calculateur de Formes Géométriques")
root.geometry('400x400')

# Frame principale
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Choix de la forme
choix_forme = tk.StringVar(value="Rectangle")
tk.Label(main_frame, text="Choisissez une forme :").pack(anchor="w")
tk.Radiobutton(main_frame, text="Rectangle", variable=choix_forme, value="Rectangle", command=afficher_frame_forme).pack(anchor="w")
tk.Radiobutton(main_frame, text="Cercle", variable=choix_forme, value="Cercle", command=afficher_frame_forme).pack(anchor="w")

# Choix du calcul
choix_calcul = tk.StringVar(value="Surface")
tk.Label(main_frame, text="Que voulez-vous calculer ?").pack(anchor="w")
tk.Radiobutton(main_frame, text="Surface", variable=choix_calcul, value="Surface").pack(anchor="w")
tk.Radiobutton(main_frame, text="Périmètre", variable=choix_calcul, value="Périmètre").pack(anchor="w")
tk.Radiobutton(main_frame, text="Volume", variable=choix_calcul, value="Volume").pack(anchor="w")

# Frame pour Rectangle
frame_rectangle = tk.Frame(main_frame)
tk.Label(frame_rectangle, text="Largeur :").grid(row=0, column=0, padx=5, pady=5)
entry_largeur = tk.Entry(frame_rectangle)
entry_largeur.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_rectangle, text="Hauteur :").grid(row=1, column=0, padx=5, pady=5)
entry_hauteur = tk.Entry(frame_rectangle)
entry_hauteur.grid(row=1, column=1, padx=5, pady=5)

# Frame pour Cercle
frame_cercle = tk.Frame(main_frame)
tk.Label(frame_cercle, text="Rayon :").grid(row=0, column=0, padx=5, pady=5)
entry_rayon = tk.Entry(frame_cercle)
entry_rayon.grid(row=0, column=1, padx=5, pady=5)

# Afficher le frame Rectangle par défaut
afficher_frame_forme()

# Bouton calculer
btn_calculer = tk.Button(main_frame, text="Calculer", command=calculer)
btn_calculer.pack(pady=10)

# Résultat
result_label = tk.Label(main_frame, text="Résultat :")
result_label.pack(pady=10)

root.mainloop()
