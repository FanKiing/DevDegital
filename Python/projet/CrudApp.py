import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from DbManager import DbManager

class CrudApp:
    def __init__(self):
        self.db = DbManager()

        self.root = tk.Tk()
        self.root.title("Application CRUD")
        self.root.geometry("600x500")
        self.root.configure(bg="#f4f4f9")

        font_large = ("Helvetica", 12)
        font_medium = ("Helvetica", 10)
        font_bold = ("Helvetica", 12, "bold")

        self.id_label = Label(self.root, text="ID:", font=font_bold, bg="#f4f4f9")
        self.id_entry = Entry(self.root, font=font_medium, relief="solid")

        self.title_label = Label(self.root, text="Title:", font=font_bold, bg="#f4f4f9")
        self.title_entry = Entry(self.root, font=font_medium, relief="solid")

        self.description_label = Label(self.root, text="Description:", font=font_bold, bg="#f4f4f9")
        self.description_entry = Entry(self.root, font=font_medium, relief="solid")

        self.priority_label = Label(self.root, text="Priority:", font=font_bold, bg="#f4f4f9")
        self.priority_combobox = ttk.Combobox(self.root, values=["High", "Medium", "Low"], font=font_medium)

        self.status_label = Label(self.root, text="Status:", font=font_bold, bg="#f4f4f9")
        self.status_var = StringVar()
        self.status_var.set("To Do")
        self.status_radio_todo = Radiobutton(self.root, text="To Do", variable=self.status_var, value="To Do", font=font_medium, bg="#f4f4f9")
        self.status_radio_ongoing = Radiobutton(self.root, text="Ongoing", variable=self.status_var, value="Ongoing", font=font_medium, bg="#f4f4f9")
        self.status_radio_done = Radiobutton(self.root, text="Done", variable=self.status_var, value="Done", font=font_medium, bg="#f4f4f9")

        self.due_date_label = Label(self.root, text="Due Date:", font=font_bold, bg="#f4f4f9")
        self.due_date_entry = DateEntry(self.root, font=font_medium, relief="solid", date_pattern='y-mm-dd')

        self.create_button = Button(self.root, text="Create", command=self.create_task, font=font_bold, bg="#4CAF50", fg="white", relief="flat", height=2, width=15)
        self.update_button = Button(self.root, text="Update", command=self.update_task, font=font_bold, bg="#2196F3", fg="white", relief="flat", height=2, width=15)
        self.delete_button = Button(self.root, text="Delete", command=self.delete_task, font=font_bold, bg="#F44336", fg="white", relief="flat", height=2, width=15)

        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Description", "Priority", "Status", "Due Date"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Due Date", text="Due Date")
        
        self.tree.column("ID", width=50)
        self.tree.column("Title", width=150)
        self.tree.column("Description", width=200)
        self.tree.column("Priority", width=80)
        self.tree.column("Status", width=100)
        self.tree.column("Due Date", width=120)
        
        self.tree.tag_configure("oddrow", background="#f9f9f9")
        self.tree.tag_configure("evenrow", background="#e9e9e9")

        self.id_label.grid(row=0, column=0, sticky=W, padx=10, pady=5)
        self.id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

        self.title_label.grid(row=1, column=0, sticky=W, padx=10, pady=5)
        self.title_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.description_label.grid(row=2, column=0, sticky=W, padx=10, pady=5)
        self.description_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

        self.priority_label.grid(row=3, column=0, sticky=W, padx=10, pady=5)
        self.priority_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

        self.status_label.grid(row=4, column=0, sticky=W, padx=10, pady=5)
        self.status_radio_todo.grid(row=4, column=1, padx=5, pady=5, sticky=W)
        self.status_radio_ongoing.grid(row=4, column=2, padx=5, pady=5, sticky=W)
        self.status_radio_done.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        self.due_date_label.grid(row=5, column=0, sticky=W, padx=10, pady=5)
        self.due_date_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

        self.create_button.grid(row=6, column=0, padx=10, pady=20)
        self.update_button.grid(row=6, column=1, padx=10, pady=20)
        self.delete_button.grid(row=6, column=2, padx=10, pady=20)

        self.tree.grid(row=7, column=0, columnspan=4, padx=10, pady=20, sticky="nsew")

        self.root.grid_rowconfigure(7, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

    def create_task(self):
        id = self.id_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_combobox.get()
        status = self.status_var.get()
        due_date = self.due_date_entry.get()

        if title and description and priority and due_date:
            self.tree.insert("", "end", values=(id, title, description, priority, status, due_date))

    def update_task(self):
        try:
            selected_item = self.tree.selection()[0]
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to update.")
            return

        id = self.id_entry.get()
        title = self.title_entry.get()
        description = self.description_entry.get()
        priority = self.priority_combobox.get()
        status = self.status_var.get()
        due_date = self.due_date_entry.get()

        self.tree.item(selected_item, values=(id, title, description, priority, status, due_date))

    def delete_task(self):
        try:
            selected_item = self.tree.selection()[0]
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")
            return

        self.tree.delete(selected_item)

if __name__ == "__main__":
    app = CrudApp()
    app.root.mainloop()