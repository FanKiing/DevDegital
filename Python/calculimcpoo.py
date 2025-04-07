class IMCCalculator:
    def __init__(self, poids, taille):
        self.poids = poids  # en kg
        self.taille = taille  # en mètre

    def calculer_imc(self):
        """Calcule l'IMC"""
        if self.taille > 0:  # éviter la division par zéro
            return self.poids / (self.taille ** 2)
        return 0

    def categorie_imc(self, imc):
        """Retourne la catégorie de l'IMC"""
        if imc < 18.5:
            return "Maigreur"
        elif 18.5 <= imc < 24.9:
            return "Normal"
        elif 25 <= imc < 29.9:
            return "Surpoids"
        else:
            return "Obésité"
import tkinter as tk
from tkinter import messagebox

class IMCApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculateur d'IMC")
        self.root.geometry("300x200")

        # Création des champs d'entrée
        self.label_poids = tk.Label(root, text="Poids (kg):")
        self.label_poids.pack()

        self.entry_poids = tk.Entry(root)
        self.entry_poids.pack()

        self.label_taille = tk.Label(root, text="Taille (m):")
        self.label_taille.pack()

        self.entry_taille = tk.Entry(root)
        self.entry_taille.pack()

        # Bouton pour calculer l'IMC
        self.button_calculer = tk.Button(root, text="Calculer IMC", command=self.calculer_imc)
        self.button_calculer.pack()

        # Label pour afficher le résultat
        self.resultat_label = tk.Label(root, text="")
        self.resultat_label.pack()

    def calculer_imc(self):
        try:
            poids = float(self.entry_poids.get())
            taille = float(self.entry_taille.get())

            # Utiliser la classe IMCCalculator
            imc_calculator = IMCCalculator(poids, taille)
            imc = imc_calculator.calculer_imc()
            categorie = imc_calculator.categorie_imc(imc)

            # Affichage du résultat
            self.resultat_label.config(text=f"IMC: {imc:.2f} - {categorie}")
        except ValueError:
            messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

# Création de la fenêtre principale
root = tk.Tk()
app = IMCApp(root)
root.mainloop()
