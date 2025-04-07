import tkinter as tk
from tkinter import messagebox

# Fonction pour activer/désactiver les entrées associées
def toggle_entry(check_var, entry):
    if check_var.get():
        entry.config(state="normal")
    else:
        entry.delete(0, tk.END)
        entry.config(state="disabled")

# Fonction pour calculer la valeur énergétique
def calculate():
    try:
        total = 0
        if pain_var.get():
            total += float(pain_var.get()) * 4
        if viande_var.get():
            total += float(viande_var.get()) * 4
        if legume_var.get():
            total += float(legume_var.get()) * 9
        
        result_label.config(text=f"Valeur énergétique totale : {total} kcal")
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des valeurs numériques valides.")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculateur de Valeur Énergétique")

# Variables des checkboxes
pain_var = tk.BooleanVar()
viande_var = tk.BooleanVar()
legume_var = tk.BooleanVar()

# Création des widgets
pain_check = tk.Checkbutton(root, text="Pain (g)", variable=pain_var, 
                                command=lambda: toggle_entry(pain_var, pain_entry))
pain_check.grid(row=0, column=0, sticky="w")
pain_entry = tk.Entry(root, state="disabled")
pain_entry.grid(row=0, column=1)

viande_check = tk.Checkbutton(root, text="Viande (g)", variable=viande_var, 
                             command=lambda: toggle_entry(viande_var, viande_entry))
viande_check.grid(row=1, column=0, sticky="w")
viande_entry = tk.Entry(root, state="disabled")
viande_entry.grid(row=1, column=1)

legume_check = tk.Checkbutton(root, text="Legume (g)", variable=legume_var, 
                            command=lambda: toggle_entry(legume_var, legume_entry))
legume_check.grid(row=2, column=0, sticky="w")
legume_entry = tk.Entry(root, state="disabled")
legume_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculer", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="Valeur énergétique totale : 0 kcal")
result_label.grid(row=4, column=0, columnspan=2)

# Lancement de la boucle principale
root.mainloop()
