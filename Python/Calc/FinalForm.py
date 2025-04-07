import tkinter as tk
from abc import ABC, abstractmethod
import math

class Calculatrice(ABC):
    def __init__(self):
        self.operande = ""
        self.resultat = 0

    @abstractmethod
    def calculer(self, expression):
        pass

    def afficher_resultat(self):
        return self.resultat

class CalculatriceScientifique(Calculatrice):
    def __init__(self):
        super().__init__()

    def calculer(self, expression):
        try:
            self.operande = expression
            if "sin" in expression:
                self.resultat = math.sin(math.radians(float(expression[3:])))
            elif "cos" in expression:
                self.resultat = math.cos(math.radians(float(expression[3:])))
            elif "tan" in expression:
                self.resultat = math.tan(math.radians(float(expression[3:])))
            elif "sqrt" in expression:
                self.resultat = math.sqrt(float(expression[4:]))
            elif "^" in expression:
                base, power = map(float, expression.split("^"))
                self.resultat = math.pow(base, power)
            elif "log" in expression:
                self.resultat = math.log10(float(expression[3:]))
            else:
                self.resultat = eval(expression)
        except Exception:
            self.resultat = "Erreur"

class CalculatriceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice Scientifique")
        self.geometry("483x500")
        self.configure(bg="#2C3E50") 

        self.calculatrice = CalculatriceScientifique()

        self.creer_widgets()

    def creer_widgets(self):
        self.texte = tk.Entry(self, width=25, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
        self.texte.grid(row=0, column=0, columnspan=5, pady=15, padx=15)

        # Button layout
        boutons = [
            ('CE', 1, 0), ('C', 1, 1), ('%', 1, 2), ('/', 1, 3), ('sqrt', 1, 4),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3), ('^', 2, 4),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('log', 3, 4),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3), ('sin', 4, 4),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('cos', 5, 3), ('tan', 5, 4),
        ]

        for (text, row, col) in boutons:
            bg_color = "#34495E" if text not in "0123456789" else "#2ECC71"  
            fg_color = "white"
            if text in {"CE", "C", "="}:
                bg_color = "#E74C3C" 
            if text in {"sqrt", "sin", "cos", "tan", "log", "^"}:
                bg_color = "#F39C12"  

            bouton = tk.Button(
                self, text=text, width=5, height=2, font=("Arial", 14),
                bg=bg_color, fg=fg_color, activebackground="#1ABC9C",
                command=lambda t=text: self.on_button_click(t)
            )
            bouton.grid(row=row, column=col, padx=5, pady=5)

    def on_button_click(self, text):
        if text == "=":
            expression = self.texte.get()
            self.calculatrice.calculer(expression)
            self.texte.delete(0, tk.END)
            self.texte.insert(tk.END, self.calculatrice.afficher_resultat())
        elif text == "C":
            self.texte.delete(0, tk.END)
        elif text == "CE":
            current = self.texte.get()
            self.texte.delete(0, tk.END)
            self.texte.insert(tk.END, current[:-1]) 
        else:
            current = self.texte.get()
            self.texte.delete(0, tk.END)
            self.texte.insert(tk.END, current + text)

app = CalculatriceApp()
app.mainloop()
