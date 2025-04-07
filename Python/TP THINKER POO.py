import tkinter as tk
from tkinter import messagebox, ttk
class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Store Name")

        self.data = []

        tk.Label(root, text="ID").grid(row=0, column=0)
        self.id_entry = tk.Entry(root)
        self.id_entry.grid(row=0, column=1)

        tk.Label(root, text="Name").grid(row=1, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=1, column=1)

        tk.Label(root, text="Price").grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        tk.Label(root, text="Quantity").grid(row=3, column=0)
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=3, column=1)

        self.enter_button = tk.Button(root, text="Enter", bg="blue", fg="white", command=self.enter_data)
        self.enter_button.grid(row=4, column=0)

        self.update_button = tk.Button(root, text="Update", bg="yellow", command=self.update_data)
        self.update_button.grid(row=4, column=1)

        self.delete_button = tk.Button(root, text="Delete", bg="red", fg="white", command=self.delete_data)
        self.delete_button.grid(row=4, column=2)

        self.data_list = tk.Listbox(root, height=10, width=50)
        self.data_list.grid(row=0, column=3, rowspan=5)
        self.data_list.bind('<<ListboxSelect>>', self.on_select)
        self.store_table = ttk.Treeview(self.root, columns=("id", "Name", "Price", "Quantity"))
        self.store_table.place(x=20, y=320, height=150)
        self.store_table.heading("id", text="id")
        self.store_table.heading("Name", text="First Name")
        self.store_table.heading("Price", text="Price")
        self.store_table.heading("Quantity", text="Quantity")
 
        self.store_table['show'] = 'headings'
 

    def enter_data(self):
        try:
            item_id = int(self.id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            if any(item["ID"] == item_id for item in self.data):
                messagebox.showerror("Error", "ID must be unique.")
                return

            self.data.append({"ID": item_id, "Name": name, "Price": price, "Quantity": quantity})
            self.refresh_listbox()
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your fields.")

    def update_data(self):
        try:
            selected_index = self.data_list.curselection()
            if not selected_index:
                messagebox.showerror("Error", "No item selected.")
                return

            item_id = int(self.id_entry.get())
            name = self.name_entry.get()
            price = float(self.price_entry.get())
            quantity = int(self.quantity_entry.get())

            current_index = selected_index[0]
            self.data[current_index] = {"ID": item_id, "Name": name, "Price": price, "Quantity": quantity}
            self.refresh_listbox()
            self.clear_entries()
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your fields.")

    def delete_data(self):
        selected_index = self.data_list.curselection()
        if not selected_index:
            messagebox.showerror("Error", "No item selected.")
            return

        current_index = selected_index[0]
        del self.data[current_index]
        self.refresh_listbox()
        self.clear_entries()

    def refresh_listbox(self):
        self.data_list.delete(0, tk.END)
        for item in sorted(self.data, key=lambda x: x["ID"]):
            self.data_list.insert(tk.END, f'{item["ID"]} \t {item["Name"]} \t {item["Price"]} \t {item["Quantity"]}')

    def clear_entries(self):
        self.id_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def on_select(self, event):
        try:
            selected_index = self.data_list.curselection()
            if not selected_index:
                return

            current_index = selected_index[0]
            selected_item = self.data[current_index]

            self.id_entry.delete(0, tk.END)
            self.id_entry.insert(0, selected_item["ID"])

            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(0, selected_item["Name"])

            self.price_entry.delete(0, tk.END)
            self.price_entry.insert(0, selected_item["Price"])

            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(0, selected_item["Quantity"])
        except IndexError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
