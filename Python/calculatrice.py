import tkinter as tk
from tkinter import StringVar
from math import pi

# Fonction pour mettre à jour l'affichage
def update_display(value):
    current = display_var.get()
    display_var.set(current + value)

# Fonction pour exécuter les calculs
def calculate():
    try:
        expression = display_var.get()
        expression = expression.replace('X^2', '**2')  # Remplacer X^2 par **2
        expression = expression.replace('Pi', str(pi))  # Remplacer Pi par sa valeur numérique
        result = str(eval(expression))  # Évaluation de l'expression
        display_var.set(result)
    except Exception as e:
        display_var.set("Erreur")  # Gestion des erreurs (par exemple division par zéro)

# Fonction pour effacer l'écran
def clear():
    display_var.set("")  # Efface le contenu de l'écran

# Fonction pour supprimer le dernier caractère
def backspace():
    current = display_var.get()
    display_var.set(current[:-1])  # Retire le dernier caractère

# Fenêtre principale
root = tk.Tk()
root.title("Calculatrice")

# Variable pour afficher le contenu de l'écran
display_var = StringVar()

# Champ d'affichage
entry = tk.Entry(root, textvariable=display_var, width=20, font=("Arial", 20), borderwidth=2, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Définition des boutons
buttons = [
    ('%', 1, 0), ('X^2', 1, 1), ('AC', 1, 2), ('<-', 1, 3),
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
    ('0', 5, 0), ('.', 5, 1), ('(', 5, 2), (')', 5, 3),
    ('Pi', 6, 0), ('Exp', 6, 1), ('/', 6, 2), ('=', 6, 3)
]

# Création des boutons et ajout d'événements
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=5, height=2, command=calculate)
    elif text == 'AC':
        button = tk.Button(root, text=text, width=5, height=2, command=clear)
    elif text == '<-':
        button = tk.Button(root, text=text, width=5, height=2, command=backspace)
    else:
        button = tk.Button(root, text=text, width=5, height=2, command=lambda text=text: update_display(text))
    button.grid(row=row, column=col, padx=5, pady=5)

# Lancer l'interface
root.mainloop()
