from abc import ABC, abstractmethod
import tkinter as tk

class Compte(ABC):
    def __init__(self,numero,propreitaire,solde_initial):
        self.numero = numero
        self.proprietaire = propreitaire
        self.solde = solde_initial
    @abstractmethod

    def obtenir_information(self):
        pass

class CompteCourant(Compte):
    def __init__(self, numero, proprietaire, solde_initial, montant_decouvert):
        super().__init__(numero, proprietaire, solde_initial)
        self.montant_decouvert = montant_decouvert

    def obtenir_information(self):
        return {
            "numero": self.numero,
            "proprietaire": self.proprietaire,
            "solde": self.solde,
            "type": "Courant",
            "taux_interet": "",
            "montant_decouvert": self.montant_decouvert
        }

class CompteEpargne(Compte):
    def __init__(self, numero, proprietaire, solde_initial, taux_interet):
        super().__init__(numero, proprietaire, solde_initial)
        self.taux_interet = taux_interet

    def obtenir_information(self):
        return {
            "numero": self.numero,
            "proprietaire": self.proprietaire,
            "solde": self.solde,
            "type": "Épargne",
            "taux_interet": self.taux_interet,
            "montant_decouvert": ""
        }
    
class GestionComptesApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gestion des Comptes Bancaires")
        self.geometry("800x400")
        self.numero = 1
        self.type_var = tk.StringVar(value="Courant")
        self.solde_var = tk.DoubleVar()
        self.proprietaire_var = tk.StringVar()
        self.solde_var = tk.DoubleVar()
        self.taux_ineret_var = tk.DoubleVar()
        self.montant_decouvert_var = tk.DoubleVar()

        self.comptes = []

        self.creer_widgets()

    def creer_widgets(self):
        tk.Label(self, text="Numéro:").grid(row=0, column=0 ,sticky='w')
        tk.Entry(self, textvariable=self.numero, state='disabled').grid(row=0, column=1)
        tk.Label(self, text="Propriétaire:").grid(row=1, column=0, sticky='w')
        tk.Entry(self, textvariable=self.proprietaire_var).grid(row=1, column=1)
        tk.Label(self, text="Solde Initial:").grid(row=2, column=0, sticky='w')
        tk.Entry(self, textvariable=self.solde_var).grid(row=2, column=1)
        tk.Label(self, text="Euro").grid(row=2, column=2, sticky='w')
        tk.Label(self, text="Type:").grid(row=3, column=0, sticky='w')
        tk.Radiobutton(self, text="Courant", variable=self.type_var, value="Courant", command=self.toggle_fields).grid(row=3, column=1)
        tk.Radiobutton(self, text="Épargne", variable=self.type_var, value="Épargne", command=self.toggle_fields).grid(row=3, column=2)
        tk.Label(self, text="Taux Intérêt:").grid(row=4, column=0, sticky='w')
        self.taux_interet_entry = tk.Entry(self, textvariable=self.taux_ineret_var, state='disabled')
        self.taux_interet_entry.grid(row=4, column=1)
        tk.Label(self, text="M. Découvert:").grid(row=5, column=0, sticky='w')
        self.montant_decouvert_entry = tk.Entry(self, textvariable=self.montant_decouvert_var, state='disabled')
        self.montant_decouvert_entry.grid(row=5, column=1)
        tk.Button(self, text="Création Compte", command=self.creer_compte).grid(row=6, column=0, columnspan=3)

        self.tableau = tk.Listbox(self,width=100, height=10)
        self.tableau.grid(row=7, column=0, columnspan=3)

    def toggle_fields(self):
        if self.type_var.get() == "Courant":
            self.taux_interet_entry.config(state='disabled')
            self.montant_decouvert_entry.config(state='normal')
        else:
            self.taux_interet_entry.config(state='normal')
            self.montant_decouvert_entry.config(state='disabled')
    
    def creer_compte(self):
        proprietaire = self.proprietaire_var.get()
        solde = self.solde_var.get()

        if self.type_var.get() == "Courant":
            montant_decouvert = self.montant_decouvert_var.get()
            compte = CompteCourant(self.numero, proprietaire, solde, montant_decouvert)
        else:
            taux_interet = self.taux_ineret_var.get()
            compte = CompteEpargne(self.numero, proprietaire, solde, taux_interet)

    def creer_compte(self):
        proprietaire = self.proprietaire_var.get()
        solde = self.solde_var.get()

        if self.type_var.get() == "Courant":
            montant_decouvert = self.montant_decouvert_var.get()
            compte = CompteCourant(self.numero, proprietaire, solde, montant_decouvert)
        else:
            taux_interet = self.taux_ineret_var.get()
            compte = CompteEpargne(self.numero, proprietaire, solde, taux_interet)

        self.comptes.append(compte)
        self.numero += 1
        self.rafficher_comptes()
        self.proprietaire_var.set("")
        self.solde_var.set(0)
        self.taux_ineret_var.set(0)
        self.montant_decouvert_var.set(0)

    def rafficher_comptes(self):
        self.tableau.delete(0, tk.END)
        for compte in self.comptes:
            info = compte.obtenir_information()
            self.tableau.insert(tk.END, f"{info['numero']} - {info['proprietaire']} - {info['solde']} - {info['type']} - {info['taux_interet']} - {info['montant_decouvert']}")
    
if __name__ == "__main__":
    app = GestionComptesApp()
    app.mainloop()


    

    




