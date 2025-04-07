import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Combobox Example")
root.geometry("300x200")

# Function to handle selection from the combobox
def on_combobox_select(event):
    selected_item = combobox.get()
    label.config(text=f"Selected: {selected_item}")

# Create a label to display the selected option
label = tk.Label(root, text="Select a fruit", font=("Arial", 14))
label.pack(pady=20)

# Create a combobox with a list of options
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
combobox = ttk.Combobox(root, values=fruits, state="readonly")  # "readonly" makes it non-editable
combobox.pack(pady=10)

# Bind the combobox to an event when an item is selected
combobox.bind("<<ComboboxSelected>>", on_combobox_select)

# Start the main event loop
root.mainloop()
