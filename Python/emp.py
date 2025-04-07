from tkinter import *
from tkinter import ttk
from tkcalendar import DateEntry
from tkinter import messagebox

from tkinter.ttk import Combobox

import sqlite3

# Sqlite3
con = sqlite3.connect("emp.db")
cursor = con.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS employees(num_Emp INTEGER  PRIMARY KEY, nom TEXT, prenom TEXT, sexe TEXT, date_naissance DATE, fonction TEXT)")
con.commit()
con.close()

# Fonctions

def ajouter_emp():
    num_emp = emp_entry.get()
    nom_emp = nom_entry.get()
    prenom_emp = prenom_entry.get()
    sexe_emp = sexe.get()
    date_naissance_emp = date_entry.get()
    fonction_emp = fonction_entry.get()
    # Insert into db
    con = sqlite3.connect('emp.db')
    cursor = con.cursor()
    cursor.execute("INSERT INTO employees (num_Emp, nom, prenom, sexe, date_naissance, fonction) VALUES(?, ?, ?, ?, ?, ?) ",
                   (num_emp, nom_emp, prenom_emp, sexe_emp, date_naissance_emp, fonction_emp))
    con.commit()
    con.close()
    
    clear_entries()
    show_employees()

def supprimer_employee():
    # Get the selected item from the treeview
    selected_item = treeview.focus()
    if selected_item:
        employee_id = treeview.item(selected_item)['values'][0]

        # Delete the employee from the database
        con = sqlite3.connect('emp.db')
        cursor = con.cursor()
        cursor.execute("DELETE FROM employees WHERE num_Emp=?", (employee_id,))
        con.commit()
        con.close()

        # Refresh the treeview
        show_employees()
        clear_entries()

def modifier_employee():
    selected_item = treeview.selection()
    if not selected_item:
        return  # No item selected, exit the function

    selected_id = treeview.item(selected_item)['values'][0]
    nom = nom_entry.get()
    prenom = prenom_entry.get()
    date_naissance = date_entry.get()
    sexe_value = sexe.get()
    fonction = fonction_entry.get()

    # Input validation
    if not nom or not prenom or not date_naissance or not fonction:
        messagebox.showerror("Error", "Please fill in all the required fields.")
        return

    conn = sqlite3.connect('emp.db')
    cursor = conn.cursor()

    try:
       
        cursor.execute(
            "UPDATE employees SET nom = ?, prenom = ?, date_naissance = ?, sexe = ?, fonction = ? WHERE num_Emp = ?",
            (nom, prenom, date_naissance, sexe_value, fonction, selected_id)
        )
        conn.commit()
        show_employees()
        clear_entries()
    except sqlite3.Error as e:
        messagebox.showerror("Error", "An error occurred while updating the employee: " + str(e))
    finally:
        cursor.close()
        conn.close()
    show_employees()
    clear_entries()
    
def select_employee():
     # Get the selected item from the treeview
    selected_item = treeview.focus()
    if selected_item:
        employee_id = treeview.item(selected_item)['values'][0]

        # Retrieve the employee details from the database
        conn = sqlite3.connect('emp.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE num_Emp=?", (employee_id,))
        employee = cursor.fetchone()
        conn.close()

        # Populate the entry fields with the employee details
        emp_entry.delete(0, END)
        emp_entry.insert(0, employee[0])
        nom_entry.delete(0, END)
        nom_entry.insert(0, employee[1])
        date_entry.delete(0, END)
        date_entry.insert(0, employee[4])
        prenom_entry.delete(0, END)
        prenom_entry.insert(0, employee[2])
        fonction_entry.delete(0, END)
        fonction_entry.insert(0, employee[5])

        # Select the appropriate radio button based on the prime value
        if employee[3] == "Masculin":
            male_radio.select()
        else:
            female_radio.select()
            

def clear_entries():
    emp_entry.delete(0, END)
    nom_entry.delete(0, END)
    prenom_entry.delete(0, END)
    date_entry.delete(0, END)
    fonction_entry.delete(0, END)
    male_radio.deselect()
    female_radio.deselect()

def show_employees():
    # Clear the treeview
    for record in treeview.get_children():
        treeview.delete(record)

    # Retrieve the employee data from the database
    con = sqlite3.connect('emp.db')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    con.close()

    # Insert the employee data into the treeview
    for employee in employees:
        treeview.insert("", END, values=employee)

# Crate main window
root = Tk()
root.title("Employee system")

# First Frame;

entry_frame = Frame(root)
entry_frame.grid(row=0, column=0, padx=5, pady=5)


emp_label = Label(entry_frame, text="Numero Employe:")
emp_label.grid(row=0, column=0, padx=5, pady=5)
emp_entry = Entry(entry_frame)
emp_entry.grid(row=0, column=1, padx=5, pady=5)

nom_label = Label(entry_frame, text="Nom:")
nom_label.grid(row=1, column=0, padx=5, pady=5)
nom_entry = Entry(entry_frame)
nom_entry.grid(row=1, column=1, padx=5, pady=5)

prenom_label = Label(entry_frame, text="Prenom:")
prenom_label.grid(row=2, column=0, padx=5, pady=5)
prenom_entry = Entry(entry_frame)
prenom_entry.grid(row=2, column=1, padx=5, pady=5)

sexe_label = Label(entry_frame, text="sexe")
sexe_label.grid(row=3, column=0, padx=5, pady=5)

sexe = StringVar()
male_radio = Radiobutton(entry_frame, text="Masculin", variable=sexe, value="Masculin")
male_radio.grid(row=3, column=1, sticky="w")
female_radio = Radiobutton(entry_frame, text="feminin", variable=sexe, value="feminin")
female_radio.grid(row=3, column=1, sticky="e")

date_label = Label(entry_frame, text="Date de naissance: ")
date_label.grid(row=4, column=0, padx=5, pady=5)
date_entry = DateEntry(entry_frame, date_pattern="dd/MM/yyyy")
date_entry.grid(row=4, column=1, padx=5, pady=5)

fonction_label = Label(entry_frame, text="fonction:")
fonction_label.grid(row=5, column=0, padx=5, pady=5)


fonctions = ["Développeur", "Chef de projet", "Analyste", "Administrateur système"]
# Créez le Combobox pour les fonctions
fonction_entry= Combobox(entry_frame, values=fonctions)
fonction_entry.grid(row=5, column=1, padx=5, pady=5)


# Buttons 
# createButtons
button_frame = Frame(root)
button_frame.grid(row=0, column=1, padx=10, pady=10)

ajouter_button = Button(button_frame, text="Ajouter", command=ajouter_emp)
ajouter_button.pack(fill="x", pady=5)

modifier_button = Button(button_frame, text="Modifier", command=modifier_employee)
modifier_button.pack(fill="x", pady=5)

select_button = Button(button_frame, text="select", command=select_employee)
select_button.pack(fill="x", pady=5)

supprimer_button = Button(button_frame, text="Supprimer", command=supprimer_employee)
supprimer_button.pack(fill="x", pady=5)

fermer_button = Button(button_frame, text="Fermer", command=root.quit)
fermer_button.pack(fill="x", pady=5)

# Create Treeview
treeview_frame = Frame(root)
treeview_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

treeview = ttk.Treeview(treeview_frame, columns=( "Numero Employe", "Nom", "Prenom", "Sexe", "Date de naissance",  "fonction"), show="headings")

treeview.column("Numero Employe", width=70)
treeview.column("Nom", width=100)
treeview.column("Prenom", width=70)
treeview.column("Sexe", width=100)
treeview.column("Date de naissance", width=100)
treeview.column("fonction", width=70)
treeview.heading("Numero Employe", text="Numero Employe")
treeview.heading("Nom", text="Nom")
treeview.heading("Prenom", text="Prenom")
treeview.heading("Sexe", text="Sexe")
treeview.heading("Date de naissance", text="Date de naissance")
treeview.heading("fonction", text="fonction")
treeview.pack(side="left", fill="y")

treeview_scroll = ttk.Scrollbar(treeview_frame, orient="vertical", command=treeview.yview)
treeview_scroll.pack(side="right", fill="y")
treeview.configure(yscrollcommand=treeview_scroll.set)

show_employees()
root.mainloop()


