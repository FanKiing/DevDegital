import tkinter as tk
from tkinter import ttk, messagebox
from crud_operations import CRUDOperations


class CRUDApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Application CRUD")
        self.geometry("700x500")

        # Database instance
        self.db = CRUDOperations()

        # Form widgets
        self.create_form()
        
        # TreeView (tableau)
        self.create_treeview()
        
        # Load initial data
        self.populate_treeview()

    def create_form(self):
        form_frame = tk.Frame(self)
        form_frame.pack(pady=10)

        tk.Label(form_frame, text="Nom:").grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(form_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Email:").grid(row=1, column=0, padx=5, pady=5)
        self.email_entry = tk.Entry(form_frame)
        self.email_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(form_frame, text="Téléphone:").grid(row=2, column=0, padx=5, pady=5)
        self.phone_entry = tk.Entry(form_frame)
        self.phone_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Button(form_frame, text="Ajouter", command=self.add_entry).grid(row=3, column=0, padx=5, pady=10)
        tk.Button(form_frame, text="Modifier", command=self.update_entry).grid(row=3, column=1, padx=5, pady=10)
        tk.Button(form_frame, text="Supprimer", command=self.delete_entry).grid(row=3, column=2, padx=5, pady=10)

    def create_treeview(self):
        self.tree = ttk.Treeview(self, columns=("ID", "Nom", "Email", "Téléphone"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Téléphone", text="Téléphone")

        self.tree.column("ID", width=50, anchor="center")
        self.tree.column("Nom", width=150)
        self.tree.column("Email", width=200)
        self.tree.column("Téléphone", width=100)

        self.tree.pack(pady=20)

    def populate_treeview(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        data = self.db.read_all()
        for record in data:
            self.tree.insert("", "end", values=record)

    def add_entry(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not email or not phone:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        self.db.create(name, email, phone)
        self.populate_treeview()

    def update_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner une ligne à modifier.")
            return

        record_id = self.tree.item(selected_item, "values")[0]
        name = self.name_entry.get()
        email = self.email_entry.get()
        phone = self.phone_entry.get()

        if not name or not email or not phone:
            messagebox.showerror("Erreur", "Tous les champs sont obligatoires.")
            return

        self.db.update(int(record_id), name, email, phone)
        self.populate_treeview()

    def delete_entry(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner une ligne à supprimer.")
            return

        record_id = self.tree.item(selected_item, "values")[0]
        self.db.delete(int(record_id))
        self.populate_treeview()
