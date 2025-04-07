import tkinter as tk
from tkinter import messagebox, ttk  # ttk pour la Combobox
from PIL import Image, ImageTk  # Pour gérer les images

# Fonction pour calculer le poids idéal
def calculer_poids():
    try:
        taille = int(entry_taille.get())  # Récupérer la taille
        genre = combo_genre.get()  # Récupérer le genre sélectionné
        
        if taille < 150:  # Condition pour taille inférieure à 150 cm
            messagebox.showerror("Erreur", "La taille doit être supérieure ou égale à 150 cm.")
            return
        
        # Formule pour calculer le poids idéal
        poids_ideal = (taille - 100) - ((taille - 150) / 4) if genre == "Homme" else (taille - 100) - ((taille - 150) / 2.5)
        entry_poids_ideal.config(state="normal")
        entry_poids_ideal.delete(0, tk.END)
        entry_poids_ideal.insert(0, f"{poids_ideal:.2f} kg")
        entry_poids_ideal.config(state="readonly")
    
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer une taille valide (nombre entier).")

# Fonction pour changer l'image selon le genre sélectionné
def changer_image(event):
    genre = combo_genre.get()
    if genre == "Homme":
        image_label.config(image=img_homme)
    elif genre == "Femme":
        image_label.config(image=img_femme)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Calculatrice de poids idéal")
root.geometry("400x400")

# Images (utilisation de PIL)
img_homme = ImageTk.PhotoImage(Image.open("src/homme.png").resize((80, 100)))
img_femme = ImageTk.PhotoImage(Image.open("src/femme.png").resize((80, 100)))

# Widgets
tk.Label(root, text="Taille en CM:", font=("Arial", 12)).pack(pady=5)
entry_taille = tk.Entry(root)
entry_taille.pack(pady=5)

tk.Label(root, text="Genre:", font=("Arial", 12)).pack(pady=5)
combo_genre = ttk.Combobox(root, values=["Homme", "Femme"], state="readonly")
combo_genre.pack(pady=5)
combo_genre.bind("<<ComboboxSelected>>", changer_image)  # Associer l'événement au changement d'image

# Image par défaut
image_label = tk.Label(root, image=img_homme)
image_label.pack(pady=5)

tk.Label(root, text="Poids idéal:", font=("Arial", 12)).pack(pady=5)
entry_poids_ideal = tk.Entry(root, state="readonly")
entry_poids_ideal.pack(pady=5)

btn_calculer = tk.Button(root, text="Calculer", command=calculer_poids)
btn_calculer.pack(pady=10)

# Lancer la fenêtre principale
root.mainloop()
