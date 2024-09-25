import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - Price: {self.price} - Quantity: {self.quantity}"


class ShoppingListApp:
    def __init__(self, ShoppingListFrame):
        self.root = ShoppingListFrame
        #self.root.title("Shopping List App")
        self.shopping_list = ShoppingList()

        font = Font(family="Arial", size=10)


        list_controls_frame = tk.Frame(self.root)
        list_controls_frame.grid(row=0, column=1, padx=27)
        self.item_name_label = tk.Label(list_controls_frame, text="Item Name:", font=font)
        self.item_name_entry = tk.Entry(list_controls_frame, font=font)
        self.item_price_label = tk.Label(list_controls_frame, text="Price(per item):", font=font)
        self.item_price_entry = tk.Entry(list_controls_frame, font=font)
        self.item_quantity_label = tk.Label(list_controls_frame, text="Item Quantity:", font=font)
        self.item_quantity_entry = tk.Entry(list_controls_frame, font=font)

        self.addRemoveFrame = Frame(list_controls_frame,padx=10,pady=10)
        self.addRemoveFrame.grid(row=6,column=0)
        self.space1 = Label(self.addRemoveFrame)
        self.space1.grid(row=0,column=1)
        self.add_button = tk.Button(self.addRemoveFrame, text="Add Item", command=self.validation, font=font)
        self.remove_button = tk.Button(self.addRemoveFrame, text="Remove Item", command=self.remove_item, font=font)

        self.clearViewFrame = Frame(list_controls_frame,padx=10,pady=10)
        self.clearViewFrame.grid(row=7,column=0)

        self.space2 = Label(self.clearViewFrame)
        self.space2.grid(row=0,column=1)

        self.clear_button = tk.Button(self.clearViewFrame, text="Clear List", command=self.clear_list, font=font)
        # self.view_button = tk.Button(self.clearViewFrame, text="View List", command=self.view_list, font=font)

        self.sortContainer = Frame(list_controls_frame,padx=10,pady=10)
        self.sortingMethod = ttk.Combobox(self.sortContainer, width=14)
        self.sortingMethod["values"] = ["Sort by Letter","Sort by Price"]
        self.sortingMethod.grid(row=0,column=0)

        self.sortBtn = Button(self.sortContainer,text="Start sort",command=self.selectedSort)
        self.sortBtn.grid(row=0, column=1)
        self.sortContainer.grid(row=8,column=0)


        self.saveLoadContainer = Frame(list_controls_frame,padx=10,pady=10)
        self.saveLoadContainer.grid(row=9,column=0)
        self.space3 = Label(self.saveLoadContainer)
        self.space3.grid(row=0,column=1)
        self.save_button = tk.Button(self.saveLoadContainer, text="Save Data", command=self.save_data, font=font)
        # self.load_button = tk.Button(self.saveLoadContainer, text="Load Data", command=self.load_data, font=font)

        self.total_price_button = tk.Button(list_controls_frame, text="Calculate Total Price", command=self.calculate_total_price, font=font)

        self.item_name_label.grid(row=0, column=0)
        self.item_name_entry.grid(row=1, column=0)
        self.item_price_label.grid(row=2, column=0)
        self.item_price_entry.grid(row=3, column=0)
        self.item_quantity_label.grid(row=4, column=0)
        self.item_quantity_entry.grid(row=5, column=0)


        self.add_button.grid(row=0, column=0)
        self.remove_button.grid(row=0, column=2)
        

        self.clear_button.grid(row=0, column=0)
        # self.view_button.grid(row=0, column=2)


        self.save_button.grid(row=0, column=0)
        # self.load_button.grid(row=0, column=2)

        self.total_price_button.grid(row=10, column=0)

        self.errorString = StringVar()
        self.errorString.set("")
        self.errorMsg = Label(list_controls_frame,textvariable=self.errorString,foreground="red")
        self.errorMsg.grid(row=11,column=0)

        listBoxFrame = tk.Frame(self.root, height=10, width=50)
        listBoxFrame.grid(row=0, column=0)

        ytaskScrollbar = Scrollbar(listBoxFrame,orient=VERTICAL)
        ytaskScrollbar.grid(row=0,column=1,sticky=NS)

        xtaskScrollbar = Scrollbar(listBoxFrame,orient=HORIZONTAL)
        xtaskScrollbar.grid(row=1,column=0,sticky=EW)

        self.item_listbox = tk.Listbox(listBoxFrame, height=11, width=33, font=("Arial",20),yscrollcommand=ytaskScrollbar.set,
                   xscrollcommand=xtaskScrollbar.set,)
        self.item_listbox.grid(row=0, column=0, padx=10, pady=10)

        ytaskScrollbar.config(command=self.item_listbox.yview)
        xtaskScrollbar.config(command=self.item_listbox.xview)

        self.load_data()
        self.item_listbox.bind("<<ListboxSelect>>", self.on_item_selected)

    def validation(self):
        if self.item_name_entry.get() == "":
            self.errorString.set("Please enter the item name")
            return 

        if not self.item_price_entry.get().replace(".","").isnumeric():
            self.errorString.set("Please enter a valid item price")
            return 
        
        if not self.item_quantity_entry.get().isnumeric():
            self.errorString.set("Please enter a valid item quantity")
            return 
        
        self.add_item()

    def selectedSort(self):

        if self.sortingMethod.get() == "Sort by Letter":
            self.sort_by_letter()
        elif self.sortingMethod.get() == "Sort by Price":
            self.sort_by_price()
        else:
            self.errorString.set("Please select a sorting method")

    def add_item(self):
        name = self.item_name_entry.get()
        price = float(self.item_price_entry.get())
        quantity = int(self.item_quantity_entry.get())
        self.shopping_list.add_item(name, price, quantity)
        self.clear_entries()
        self.view_list()

    def remove_item(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            selected_item = self.item_listbox.get(selected_index)
            name = selected_item.split(" - ")[0]
            removed = self.shopping_list.delete_item(name)
            self.save_data(1)
            if removed:
                messagebox.showinfo("Remove Item", "Item removed from the shopping list.")
            else:
                self.errorString.set("Item not found in the shopping list.")
            self.clear_entries()
            self.view_list()
        else:
            self.errorString.set("No item selected.")

    def clear_list(self):
        self.shopping_list.clear_list()
        self.save_data(1)
        messagebox.showinfo("Clear List", "Shopping list cleared.")
        self.view_list()

    def view_list(self):
        self.item_listbox.delete(0, tk.END)
        items = self.shopping_list.view_list()
        for item in items:
            self.item_listbox.insert(tk.END, item)

    def sort_by_letter(self):
        self.shopping_list.radix_sort()
        self.view_list()

    def sort_by_price(self):
        self.shopping_list.shell_sort()
        self.view_list()

    def save_data(self,num=0):
        filename = ".//Pages//ShoppingList//shopping_data.txt"
        self.shopping_list.save_data_to_file(filename)
        if num == 0:
            messagebox.showinfo("Update Saved", f"Update has been made in {filename}.")

    def load_data(self):
        filename = ".//Pages//ShoppingList//shopping_data.txt"
        self.shopping_list.load_data_from_file(filename)
        self.view_list()

    def clear_entries(self):
        self.item_name_entry.delete(0, tk.END)
        self.item_price_entry.delete(0, tk.END)
        self.item_quantity_entry.delete(0, tk.END)

    def calculate_total_price(self):
        total_price = self.shopping_list.calculate_total_price()
        messagebox.showinfo("Calculate Total Price", f"The total price of all items is: {total_price}")

    def on_item_selected(self, event):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            selected_item = self.item_listbox.get(selected_index)
            name, price, quantity = selected_item.split(" - ")[0], selected_item.split(" - ")[1], selected_item.split(" - ")[2].split(": ")[1]
            # self.item_name_entry.delete(0, tk.END)
            # self.item_name_entry.insert(tk.END, name)
            # self.item_price_entry.delete(0, tk.END)
            # self.item_price_entry.insert(tk.END, price)
            # self.item_quantity_entry.delete(0, tk.END)
            # self.item_quantity_entry.insert(tk.END, quantity)

    def run(self):
        self.root


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        item = Item(name, price, quantity)
        self.items.append(item)

    def delete_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return True
        return False

    def clear_list(self):
        self.items = []

    def view_list(self):
        item_list = []
        for item in self.items:
            item_list.append(str(item))
        return item_list

    def radix_sort(self):
        max_length = 0
        for item in self.items:
            if len(item.name) > max_length:
                max_length = len(item.name)
        for i in range(max_length - 1, -1, -1):
            self.counting_sort(i)

    def counting_sort(self, index):
        count = [0] * 128
        sorted_items = [None] * len(self.items)
        for item in self.items:
            char_index = ord(item.name[index]) if index < len(item.name) else 0
            count[char_index] += 1
        for i in range(1, len(count)):
            count[i] += count[i - 1]
        for i in range(len(self.items) - 1, -1, -1):
            item = self.items[i]
            char_index = ord(item.name[index]) if index < len(item.name) else 0
            sorted_items[count[char_index] - 1] = item
            count[char_index] -= 1
        for i in range(len(self.items)):
            self.items[i] = sorted_items[i]

    def shell_sort(self):
        n = len(self.items)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = self.items[i]
                j = i
                while j >= gap and self.items[j - gap].price > temp.price:
                    self.items[j] = self.items[j - gap]
                    j -= gap
                self.items[j] = temp
            gap //= 2

    def save_data_to_file(self, filename):
        with open(filename, "w") as file:
            for item in self.items:
                file.write(f"{item.name},{item.price},{item.quantity}\n")

    def load_data_from_file(self, filename):
        self.items = []
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines:
                data = line.strip().split(",")
                name = data[0]
                price = float(data[1])
                quantity = int(data[2])
                print(line)
                self.add_item(name, price, quantity)

    def calculate_total_price(self):
        total_price = 0
        for item in self.items:
            total_price += item.price * item.quantity
        return total_price


if __name__ == "__main__":
    app = ShoppingListApp()
    app.run()


