import tkinter as tk

# Fonction pour calculer le BMI
def calculer_bmi():
    try:
        poids = float(entry_poids.get())
        taille = float(entry_taille.get())
        # Calcul du BMI
        bmi = poids * 10000 / (taille ** 2)
        # Affichage du BMI et de la classification
        label_resultat.config(text=f"BMI: {bmi:.2f} ", fg="black")
        
        if bmi < 19:
            label_classification.config(text="Sous poids", fg="red")
        elif 19 <= bmi <= 25:
            label_classification.config(text="Normal", fg="green")
        else:
            label_classification.config(text="Surpoids", fg="orange")
    except ValueError:
        label_resultat.config(text="Veuillez entrer des valeurs valides", fg="red")
        label_classification.config(text="", fg="black")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice BMI")
root.geometry("300x250")

# Label titre
label_title = tk.Label(root, text="Body mass index", font=("Helvetica", 14))
label_title.pack(pady=10)

# Label et champ pour le poids
label_poids = tk.Label(root, text="Poids en (Kg)")
label_poids.pack()
entry_poids = tk.Entry(root)
entry_poids.pack(pady=5)

# Label et champ pour la taille
label_taille = tk.Label(root, text="Taille en (centimètre)")
label_taille.pack()
entry_taille = tk.Entry(root)
entry_taille.pack(pady=5)

# Bouton pour calculer
button_calculer = tk.Button(root, text="Calculer", command=calculer_bmi)
button_calculer.pack(pady=10)

# Labels pour afficher le résultat et la classification
label_resultat = tk.Label(root, text="BMI: ", font=("Helvetica", 12))
label_resultat.pack()

label_classification = tk.Label(root, text="", font=("Helvetica", 12))
label_classification.pack()

# Lancer l'interface graphique
root.mainloop()
