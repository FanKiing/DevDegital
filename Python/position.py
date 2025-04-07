import tkinter as tk

root = tk.Tk()
root.title("Gestionnaires de positions")
root.geometry("400x400")

# Section 1 : Pack
frame1 = tk.Frame(root, bg="lightgray", height=100)
frame1.pack(fill="x")

tk.Button(frame1, text="Bouton 1").pack(side="left", padx=10)
tk.Button(frame1, text="Bouton 2").pack(side="left", padx=10)
tk.Button(frame1, text="Bouton 3").pack(side="left", padx=10)

# Section 2 : Grid
frame2 = tk.Frame(root, bg="white", height=200)
frame2.pack(fill="x", pady=10)

for i in range(3):
    for j in range(3):
        tk.Button(frame2, text=f"{3*i+j+1}", width=5).grid(row=i, column=j, padx=5, pady=5)

tk.Button(frame2, text="0", width=5).grid(row=3,column=0, padx=5, pady=5,columnspan=3)

# Section 3 : Place
frame3 = tk.Frame(root, bg="lightblue", height=100)
frame3.pack(fill="x")

tk.Button(frame3, text="Placé ici").place(x=150, y=30)

root.mainloop()
