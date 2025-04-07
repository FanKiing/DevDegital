import tkinter as tk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x500")
        
        # Frame pour Entry et Bouton Ajouter
        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)
        
        # Entry pour ajouter une tâche
        self.task_entry = tk.Entry(input_frame, width=25)
        self.task_entry.pack(side="left", padx=5)
        
        # Bouton Ajouter à côté de l'Entry
        self.add_button = tk.Button(input_frame, text="Ajouter", command=self.add_todo)
        self.add_button.pack(side="left")
        
        # Frame pour afficher les tâches
        self.todo_frame = tk.Frame(self.root)
        self.todo_frame.pack(fill="x",pady=10)
    
    def add_todo(self):
        task_text = self.task_entry.get().strip()
        if task_text:  # Vérifier si l'entrée n'est pas vide
            # Créer une Frame pour chaque tâche
            task_frame = tk.Frame(self.todo_frame)
            task_frame.pack(fill="x", pady=5)
            
            # Variable pour l'état de la checkbox
            var = tk.BooleanVar()
            
          
            
            # Checkbox pour marquer comme complétée
            checkbox = tk.Checkbutton(
                task_frame, 
                variable=var, 
                command=lambda: self.toggle_strike(task_label, var)
            )
            checkbox.pack(side="left", padx=5)
              # Label pour afficher la tâche
            task_label = tk.Label(task_frame, text=task_text, font=("Arial", 12))
            task_label.pack(side="left", padx=5)
            
            # Bouton Supprimer
            delete_button = tk.Button(task_frame, text="Supprimer", command=lambda: self.delete_task(task_frame))
            delete_button.pack(side="right", padx=5)
            
            # Effacer l'entrée après l'ajout
            self.task_entry.delete(0, tk.END)
    
    def toggle_strike(self, label, var):
        """Barre ou rétablit le texte selon l'état de la checkbox."""
        if var.get():  # Si la checkbox est cochée
            label.config(font=("Arial", 12, "overstrike"))  # Texte barré
        else:  # Si la checkbox est décochée
            label.config(font=("Arial", 12, "normal"))  # Texte normal
    
    def delete_task(self, task_frame):
        task_frame.destroy()  # Supprimer la tâche de l'interface


root = tk.Tk()
app = TodoApp(root)
root.mainloop()
