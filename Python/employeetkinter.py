from tkinter import Tk,ttk,messagebox
from tkinter import *
from tkcalendar import DateEntry
import sqlite3

window = Tk()
window.geometry("800x800+300+100")

conn = sqlite3.connect("employees.db")
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS employees(Numero_employé INTEGER PRIMARY KEY, Nom TEXT, Prenom TEXT, Sexe TEXT, Date_naissance TEXT, Fonction TEXT)")

def Ajouter():
    try:
        if num_entry.get() and nom_entry.get() and prenom_entry.get() and fonction_entry.get():
            cur.execute("INSERT INTO employees VALUES(?,?,?,?,?,?)",(num_entry.get(), nom_entry.get(), prenom_entry.get(),radio.get(),date_entry.get_date(), fonction_entry.get()))
            conn.commit()
            Afficher()
    except: messagebox.ERROR("error","error has occured")

def Delete():
    selected = tree.selection()
    selected_id = tree.item(selected)["values"][0]
    #delete after confirmation => messagebox.question
    cur.execute("DELETE FROM employees WHERE numero_employé = ?",(selected_id,))
    conn.commit()
    Afficher()

def Afficher():
    for item in tree.get_children():
        tree.delete(item)
    data = cur.execute("SELECT * FROM employees")
    for item in data:
        tree.insert("",'end',values=item)

frame1 = Frame(window,width=800,height=450)
frame1.place(x=0,y=0)
frame2 = Frame(window,width=800,height=250)
frame2.place(x=0,y=450)
frame3 = Frame(window,width=800,height=100)
frame3.place(x=0,y=700)

num_lbl = Label(frame1,text="Numero Employé :", font=("sans serif",16), padx=20,pady=20)
num_lbl.grid(row=0,column=0)
nom_lbl = Label(frame1,text="Nom :", font=("sans serif",16), padx=20,pady=20)
nom_lbl.grid(row=1,column=0)
Prenom_lbl = Label(frame1,text="Prenom :", font=("sans serif",16), padx=20,pady=20)
Prenom_lbl.grid(row=2,column=0)
sexe_lbl = Label(frame1,text="Sexe :", font=("sans serif",16), padx=20,pady=20)
sexe_lbl.grid(row=3,column=0)
Date_lbl = Label(frame1,text="Date de naissance :", font=("sans serif",16), padx=20,pady=20)
Date_lbl.grid(row=4,column=0)
fonction_lbl = Label(frame1,text="Fonction :", font=("sans serif",16), padx=20,pady=20)
fonction_lbl.grid(row=5,column=0)

num_entry = Entry(frame1,font=("sans serif",16),width=30)
num_entry.grid(row=0,column=1, columnspan=2,padx=100)
nom_entry = Entry(frame1,font=("sans serif",16),width=30)
nom_entry.grid(row=1,column=1, columnspan=2,padx=100)
prenom_entry = Entry(frame1,font=("sans serif",16),width=30)
prenom_entry.grid(row=2,column=1, columnspan=2,padx=100)
radio = StringVar(frame1)
fem_entry = Radiobutton(frame1,font=("sans serif",16), text="Feminin",variable=radio , value=1)
masc_entry = Radiobutton(frame1,font=("sans serif",16), text="Masculin",variable=radio , value=2)
fem_entry.grid(row=3,column=2)
masc_entry.grid(row=3,column=1)
date_entry = DateEntry(frame1,selected_mode="days",width=30)
date_entry.grid(row=4,column=1, columnspan=2,padx=100)
#combobox
fonction_entry = Entry(frame1,font=("sans serif",16),width=30)
fonction_entry.grid(row=5,column=1, columnspan=2,padx=100)

tree = ttk.Treeview(frame2, columns=(1,2,3,4,5,6), show="headings")
tree.place(x=0,y=0)
tree.heading(1,text="numero employé")
tree.heading(2,text="Nom")
tree.heading(3,text="Prenom")
tree.heading(4,text="Sexe")
tree.heading(5,text="Date de naissance")
tree.heading(6,text="Fonction")
tree.column(1,width=800//6)
tree.column(2,width=800//6)
tree.column(3,width=800//6)
tree.column(4,width=800//6)
tree.column(5,width=800//6)
tree.column(6,width=800//6)

ajouter_btn = Button(frame3,text="Ajouter",bg="green",font=("sans serif",16),fg="white",width=15, command=Ajouter)
ajouter_btn.grid(row=0,column=1,padx=4)
modifier_btn = Button(frame3,text="Modifier",bg="yellow",font=("sans serif",16),fg="white",width=15)
modifier_btn.grid(row=0,column=2,padx=4)
supprimer_btn = Button(frame3,text="Supprimer",bg="red",font=("sans serif",16),fg="white",width=15,command=Delete)
supprimer_btn.grid(row=0,column=3,padx=4)
afficher_btn = Button(frame3,text="Afficher",bg="orange",font=("sans serif",16),fg="white",width=15,command=Afficher)
afficher_btn.grid(row=0,column=4,padx=4)

Afficher()

window.mainloop()