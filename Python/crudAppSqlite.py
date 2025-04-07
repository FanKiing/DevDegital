import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Création de la table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL
)
""")
conn.commit()

# Fonction pour insérer un étudiant
def add_student():
    name = name_var.get()
    age = age_var.get()
    major = major_var.get()
    
    if name == "" or age == "" or major == "":
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")
        return
    
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)", (name, age, major))
    conn.commit()
    load_students()
    clear_fields()

# Fonction pour charger les étudiants dans le Treeview
def load_students():
    for item in tree.get_children():
        tree.delete(item)
    
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row)

# Fonction pour supprimer un étudiant
def delete_student():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant.")
        return
    
    student_id = tree.item(selected_item, "values")[0]
    
    # Demander confirmation avant la suppression
    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cet étudiant ?")
    if confirm:  # Si l'utilisateur clique sur "Oui"
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        load_students()
        messagebox.showinfo("Succès", "L'étudiant a été supprimé avec succès.")
    else:
        messagebox.showinfo("Annulé", "La suppression a été annulée.")

# Fonction pour remplir les champs pour modification
def select_student():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant.")
        return
    
    student = tree.item(selected_item, "values")
    clear_fields()
    name_var.set(student[1])
    age_var.set(student[2])
    major_var.set(student[3])

# Fonction pour mettre à jour un étudiant
def update_student():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showwarning("Erreur", "Veuillez sélectionner un étudiant.")
        return
    
    student_id = tree.item(selected_item, "values")[0]
    name = name_var.get()
    age = age_var.get()
    major = major_var.get()
    
    if name == "" or age == "" or major == "":
        messagebox.showwarning("Erreur", "Tous les champs doivent être remplis.")
        return
    
    # Demander confirmation avant la modification
    confirm = messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir modifier les informations de cet étudiant ?")
    if confirm:  # Si l'utilisateur clique sur "Oui"
        cursor.execute("UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?", (name, age, major, student_id))
        conn.commit()
        load_students()
        messagebox.showinfo("Succès", "Les informations de l'étudiant ont été mises à jour avec succès.")
    else:
        messagebox.showinfo("Annulé", "La modification a été annulée.")

# Fonction pour vider les champs
def clear_fields():
    name_var.set("")
    age_var.set("")
    major_var.set("")

# Interface utilisateur
root = tk.Tk()
root.title("Gestion des étudiants")
root.geometry("600x400")

# Variables
name_var = tk.StringVar()
age_var = tk.StringVar()
major_var = tk.StringVar()

# Formulaire
form_frame = tk.Frame(root)
form_frame.pack(pady=10)

tk.Label(form_frame, text="Nom").grid(row=0, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Âge").grid(row=1, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=age_var).grid(row=1, column=1, padx=5, pady=5)

tk.Label(form_frame, text="Filière").grid(row=2, column=0, padx=5, pady=5)
tk.Entry(form_frame, textvariable=major_var).grid(row=2, column=1, padx=5, pady=5)

tk.Button(form_frame, text="Ajouter", command=add_student).grid(row=3, column=0, padx=5, pady=10)
tk.Button(form_frame, text="Mettre à jour", command=update_student).grid(row=3, column=1, padx=5, pady=10)

# Tableau (Treeview)
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("ID", "Nom", "Âge", "Filière")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", height=8)
tree.pack(side="left", fill="y")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side="right", fill="y")

# Boutons pour gestion des étudiants
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Supprimer", command=delete_student).grid(row=0, column=0, padx=10)
tk.Button(button_frame, text="Sélectionner", command=select_student).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Vider les champs", command=clear_fields).grid(row=0, column=2, padx=10)

# Charger les étudiants au démarrage
load_students()

root.mainloop()
