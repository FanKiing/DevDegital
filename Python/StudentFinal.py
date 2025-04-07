from tkinter import Tk, Label, Entry, Button, Radiobutton, Frame, StringVar, Listbox, Scrollbar, messagebox
from tkinter import font

class StudentManagement:
    def __init__(self, master):
        self.master = master
        master.title("Gestion des Étudiants")
        master.geometry("870x670")
        master.config(bg="#E8F5E9") 

        self.custom_font = font.nametofont("TkDefaultFont")
        self.custom_font.configure(family="Helvetica", size=12)
        
        title_label = Label(master, text="Gestion des Étudiants", font=("Helvetica", 18, "bold"), bg="#81C784", fg="white")
        title_label.grid(row=0, columnspan=2, pady=20)

        Label(master, text="Nom:", font=self.custom_font, bg="#E8F5E9").grid(row=1, sticky="w", padx=30, pady=10)
        self.nom_entry = Entry(master, font=self.custom_font, width=30, relief="solid", borderwidth=1, highlightbackground="#81C784")
        self.nom_entry.grid(row=1, column=1, pady=10)

        Label(master, text="Âge:", font=self.custom_font, bg="#E8F5E9").grid(row=2, sticky="w", padx=30, pady=10)
        self.age_entry = Entry(master, font=self.custom_font, width=30, relief="solid", borderwidth=1, highlightbackground="#81C784")
        self.age_entry.grid(row=2, column=1, pady=10)

        Label(master, text="Cours:", font=self.custom_font, bg="#E8F5E9").grid(row=3, sticky="w", padx=30, pady=10)
        self.cours_entry = Entry(master, font=self.custom_font, width=30, relief="solid", borderwidth=1, highlightbackground="#81C784")
        self.cours_entry.grid(row=3, column=1, pady=10)

        add_button = Button(master, text="Ajouter Étudiant", command=self.add_student, font=("Helvetica", 12, "bold"), bg="#4CAF50", fg="white", relief="flat", width=20)
        add_button.grid(row=4, columnspan=2, pady=15)

        self.selected_cours = StringVar(value="Tous")
        Radiobutton(master, text="Tout", variable=self.selected_cours, value="Tous", font=self.custom_font, bg="#E8F5E9", selectcolor="#81C784").grid(row=5, column=0, padx=30)
        Radiobutton(master, text="Mathématiques", variable=self.selected_cours, value="Mathématiques", font=self.custom_font, bg="#E8F5E9", selectcolor="#81C784").grid(row=5, column=1, padx=30)
        Radiobutton(master, text="Informatique", variable=self.selected_cours, value="Informatique", font=self.custom_font, bg="#E8F5E9", selectcolor="#81C784").grid(row=5, column=2, padx=30)
        Radiobutton(master, text="Chimie", variable=self.selected_cours, value="Chimie", font=self.custom_font, bg="#E8F5E9", selectcolor="#81C784").grid(row=5, column=3, padx=30)

        filter_button = Button(master, text="Filtrer", command=self.filter_students, font=("Helvetica", 12, "bold"), bg="#2196F3", fg="white", relief="flat", width=20)
        filter_button.grid(row=6, columnspan=2, pady=10)

        self.student_list_frame = Frame(master, bg="#E8F5E9")
        self.student_list_frame.grid(row=7, columnspan=4, sticky="nsew", padx=30, pady=20)

        self.student_listbox = Listbox(self.student_list_frame, font=self.custom_font, height=10, bg="#F1F8E9", selectmode="single", relief="solid", bd=1)
        self.student_listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = Scrollbar(self.student_list_frame, orient="vertical", command=self.student_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.student_listbox.config(yscrollcommand=self.scrollbar.set)

        self.students = []
        self.update_student_list()

        update_button = Button(master, text="Mettre à jour", command=self.update_student, font=("Helvetica", 12, "bold"), bg="#FFC107", fg="white", relief="flat", width=20)
        update_button.grid(row=8, column=0, padx=30, pady=10)

        delete_button = Button(master, text="Supprimer", command=self.delete_student, font=("Helvetica", 12, "bold"), bg="#F44336", fg="white", relief="flat", width=20)
        delete_button.grid(row=8, column=1, padx=30, pady=10)

    def add_student(self):
        nom = self.nom_entry.get()
        age = self.age_entry.get()
        cours = self.cours_entry.get()

        if nom and age and cours:
            new_student = {"id": len(self.students) + 1, "nom": nom, "age": age, "cours": cours}
            self.students.append(new_student)

            self.nom_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.cours_entry.delete(0, 'end')

            self.update_student_list()

    def update_student_list(self):
        self.student_listbox.delete(0, 'end')

        selected_course = self.selected_cours.get()
        filtered_students = self.students if selected_course == "Tous" else [student for student in self.students if student["cours"] == selected_course]

        for student in filtered_students:
            self.student_listbox.insert('end', f"{student['id']} - {student['nom']} - {student['age']} - {student['cours']}")

    def filter_students(self):
        self.update_student_list()

    def update_student(self):
        selected_student_index = self.student_listbox.curselection()

        if not selected_student_index:
            messagebox.showwarning("Sélectionnez un étudiant", "Veuillez sélectionner un étudiant à mettre à jour.")
            return

        selected_student = self.students[selected_student_index[0]]

        # Get updated details
        nom = self.nom_entry.get()
        age = self.age_entry.get()
        cours = self.cours_entry.get()

        if nom and age and cours:
            selected_student['nom'] = nom
            selected_student['age'] = age
            selected_student['cours'] = cours

            self.nom_entry.delete(0, 'end')
            self.age_entry.delete(0, 'end')
            self.cours_entry.delete(0, 'end')

            self.update_student_list()
            messagebox.showinfo("Succès", "L'étudiant a été mis à jour avec succès.")
        else:
            messagebox.showwarning("Champs manquants", "Tous les champs doivent être remplis.")

    def delete_student(self):
        selected_student_index = self.student_listbox.curselection()

        if not selected_student_index:
            messagebox.showwarning("Sélectionnez un étudiant", "Veuillez sélectionner un étudiant à supprimer.")
            return

        selected_student = self.students[selected_student_index[0]]

        confirm_delete = messagebox.askyesno("Confirmation", f"Êtes-vous sûr de vouloir supprimer l'étudiant {selected_student['nom']} ?")

        if confirm_delete:
            self.students.remove(selected_student)
            self.update_student_list()
            messagebox.showinfo("Succès", "L'étudiant a été supprimé.")

if __name__ == "__main__":
    root = Tk()
    app = StudentManagement(root)
    root.mainloop()
