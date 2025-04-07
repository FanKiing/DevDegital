from tkinter import Tk, Label, Entry, Button, Radiobutton, Frame, StringVar, Listbox, Scrollbar
from tkinter import ttk

class StudentManagement:
    def __init__(self, master):
        self.master = master
        master.title("Gestion des Étudiants")

        Label(master, text="Nom:").grid(row=0)
        self.nom_entry = Entry(master)
        self.nom_entry.grid(row=0, column=1)

        Label(master, text="Âge:").grid(row=1)
        self.age_entry = Entry(master)
        self.age_entry.grid(row=1, column=1)

        Label(master, text="Cours:").grid(row=2)
        self.cours_entry = Entry(master)
        self.cours_entry.grid(row=2, column=1)

        Button(master, text="Ajouter Étudiant", command=self.add_student).grid(row=3, columnspan=2)

        self.selected_cours = StringVar(value="Tous")
        Radiobutton(master, text="Tout", variable=self.selected_cours, value="Tous").grid(row=4, column=0)
        Radiobutton(master, text="Mathématiques", variable=self.selected_cours, value="Mathématiques").grid(row=4, column=1)
        Radiobutton(master, text="Informatique", variable=self.selected_cours, value="Informatique").grid(row=4, column=2)
        Radiobutton(master, text="Chimie", variable=self.selected_cours, value="Chimie").grid(row=4, column=3)

        self.student_list_frame = Frame(master)
        self.student_list_frame.grid(row=5, columnspan=4, sticky="nsew")

        self.student_listbox = Listbox(self.student_list_frame)
        self.student_listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.student_list_frame, orient="vertical", command=self.student_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.student_listbox.config(yscrollcommand=self.scrollbar.set)

        self.students = []

        self.update_student_list()

        self.table = ttk.Treeview(self.student_list_frame, columns=['Nom', 'Age', 'Cours'], show='headings')
        self.table.heading('Nom', text='Nom')
        self.table.heading('Age', text='Âge')
        self.table.heading('Cours', text='Cours')
        self.table.column('Nom', width=60)
        self.table.column('Age', width=120)
        self.table.column('Cours', width=120)

        self.table.bind('<Delete>', self.delete_student)
        self.table.pack(padx=20, pady=20, fill="both", expand=True)

    def add_student(self):
        nom = self.nom_entry.get()
        age = self.age_entry.get()
        cours = self.cours_entry.get()

        new_student = {"id": len(self.students) + 1, "nom": nom, "age": age, "cours": cours}
        self.students.append(new_student)

        self.nom_entry.delete(0, 'end')
        self.age_entry.delete(0, 'end')
        self.cours_entry.delete(0, 'end')

        self.update_student_list()
        self.update_treeview()

    def update_student_list(self):
        self.student_listbox.delete(0, 'end')

        selected_course = self.selected_cours.get()

        filtered_students = self.students if selected_course == "Tous" else [student for student in self.students if student["cours"] == selected_course]

        for student in filtered_students:
            self.student_listbox.insert('end', f"{student['id']} - {student['nom']} - {student['age']} - {student['cours']}")

    def update_treeview(self):
        for row in self.table.get_children():
            self.table.delete(row)

        for student in self.students:
            self.table.insert('', 'end', values=(student['nom'], student['age'], student['cours']))

    def delete_student(self, event):
        selected_item = self.table.selection()[0]
        self.table.delete(selected_item)

if __name__ == "__main__":
    root = Tk()
    app = StudentManagement(root)
    root.mainloop()