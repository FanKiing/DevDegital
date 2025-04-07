import sqlite3

class DatabaseManager:
    def __init__(self, db_name="contacts.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Créer la table si elle n'existe pas."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT
        )
        """)
        self.conn.commit()

    def add_contact(self, name, email, phone):
        """Ajouter un contact à la base de données."""
        self.cursor.execute("INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
        self.conn.commit()

    def get_contacts(self):
        """Récupérer tous les contacts."""
        self.cursor.execute("SELECT * FROM contacts")
        return self.cursor.fetchall()

    def update_contact(self, contact_id, name, email, phone):
        """Mettre à jour un contact."""
        self.cursor.execute("""
        UPDATE contacts SET name = ?, email = ?, phone = ? WHERE id = ?
        """, (name, email, phone, contact_id))
        self.conn.commit()

    def delete_contact(self, contact_id):
        """Supprimer un contact."""
        self.cursor.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self.conn.commit()

    def close(self):
        """Fermer la connexion à la base de données."""
        self.conn.close()
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class ContactApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion de Contacts")
        self.db_manager = DatabaseManager()

        # Cadre pour les entrées
        self.frame_inputs = tk.Frame(root)
        self.frame_inputs.pack(pady=10)

        tk.Label(self.frame_inputs, text="Nom:").grid(row=0, column=0, padx=5, pady=5)
        self.entry_name = tk.Entry(self.frame_inputs)
        self.entry_name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.entry_email = tk.Entry(self.frame_inputs)
        self.entry_email.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_inputs, text="Téléphone:").grid(row=2, column=0, padx=5, pady=5)
        self.entry_phone = tk.Entry(self.frame_inputs)
        self.entry_phone.grid(row=2, column=1, padx=5, pady=5)

        # Boutons pour les actions
        self.frame_buttons = tk.Frame(root)
        self.frame_buttons.pack(pady=10)

        self.btn_add = tk.Button(self.frame_buttons, text="Ajouter", command=self.add_contact)
        self.btn_add.grid(row=0, column=0, padx=5)

        self.btn_update = tk.Button(self.frame_buttons, text="Mettre à jour", command=self.update_contact)
        self.btn_update.grid(row=0, column=1, padx=5)

        self.btn_delete = tk.Button(self.frame_buttons, text="Supprimer", command=self.delete_contact)
        self.btn_delete.grid(row=0, column=2, padx=5)

        # Table pour afficher les contacts
        self.tree = ttk.Treeview(root, columns=("ID", "Nom", "Email", "Téléphone"), show="headings")
        self.tree.pack(pady=10)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Téléphone", text="Téléphone")
        self.tree.column("ID", width=30)
        self.tree.bind("<Double-1>", self.load_selected_contact)

        # Charger les contacts existants
        self.load_contacts()

    def add_contact(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if name:
            self.db_manager.add_contact(name, email, phone)
            self.clear_entries()
            self.load_contacts()
            messagebox.showinfo("Succès", "Contact ajouté avec succès!")
        else:
            messagebox.showerror("Erreur", "Le nom est obligatoire!")

    def load_contacts(self):
        """Charger les contacts dans le tableau."""
        for row in self.tree.get_children():
            self.tree.delete(row)

        contacts = self.db_manager.get_contacts()
        for contact in contacts:
            self.tree.insert("", "end", values=contact)

    def load_selected_contact(self, event):
        """Charger les informations du contact sélectionné dans les champs d'entrée."""
        selected_item = self.tree.selection()
        if selected_item:
            contact = self.tree.item(selected_item[0], "values")
            self.entry_name.delete(0, tk.END)
            self.entry_name.insert(0, contact[1])
            self.entry_email.delete(0, tk.END)
            self.entry_email.insert(0, contact[2])
            self.entry_phone.delete(0, tk.END)
            self.entry_phone.insert(0, contact[3])
            self.selected_contact_id = contact[0]

    def update_contact(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        if hasattr(self, "selected_contact_id") and name:
            self.db_manager.update_contact(self.selected_contact_id, name, email, phone)
            self.clear_entries()
            self.load_contacts()
            messagebox.showinfo("Succès", "Contact mis à jour avec succès!")
        else:
            messagebox.showerror("Erreur", "Sélectionnez un contact et entrez un nom!")

    def delete_contact(self):
        if hasattr(self, "selected_contact_id"):
            self.db_manager.delete_contact(self.selected_contact_id)
            self.clear_entries()
            self.load_contacts()
            messagebox.showinfo("Succès", "Contact supprimé avec succès!")
        else:
            messagebox.showerror("Erreur", "Sélectionnez un contact à supprimer!")

    def clear_entries(self):
        """Effacer les champs d'entrée."""
        self.entry_name.delete(0, tk.END)
        self.entry_email.delete(0, tk.END)
        self.entry_phone.delete(0, tk.END)
        self.selected_contact_id = None


# Lancement de l'application
root = tk.Tk()
app = ContactApp(root)
root.mainloop()
