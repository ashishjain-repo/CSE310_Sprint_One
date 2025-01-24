import tkinter as tk
from tkinter import *

class LoginScreen:
    def __init__(self, root):
        self.root = root
        self.root.title("IMS")

        # Create main frame
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)

        # Create title label
        self.title_label = tk.Label(self.main_frame, text="IMS", font=("Arial", 24))
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")

        # Create buttons frame
        self.buttons_frame = tk.Frame(self.main_frame)
        self.buttons_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create log in button
        self.log_in_button = tk.Button(self.buttons_frame, text="Log In", command=self.log_in, width=14, height=2)
        self.log_in_button.pack(side="left", padx=14)

        # Create create inventory button
        self.create_inventory_button = tk.Button(self.buttons_frame, text="Create Inventory", command=self.create_inventory, width=14, height=2)
        self.create_inventory_button.pack(side="left", padx=14)

        # Create exit button
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.destroy, width=10, height=2)
        self.exit_button.place(relx=0.5, rely=0.7, anchor="center")

    def log_in(self):
        print("Log in button clicked")
        self.root.withdraw()
        LoginWindow(self.root)

    def create_inventory(self):
        # Add create inventory functionality here
        print("Create inventory button clicked")
        self.root.withdraw()
        CreateInventoryWindow(self.root)

class UserInventoryWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)  # Pass the root to Toplevel
        self.window.title("IMS")
        self.window.geometry("800x600")  # Increased window size

        # Create back button
        self.back_button = tk.Button(self.window, text="Back", command=self.back, width=10, height=2)
        self.back_button.place(relx=0, rely=0, anchor="nw", x=5, y=5)

        # Create frame to hold categories
        self.categories_frame = tk.Frame(self.window)
        self.categories_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create button to create new category
        self.create_category_button = tk.Button(self.categories_frame, text="Create Category", command=self.create_category)
        self.create_category_button.pack()

        # Create frame to hold category buttons
        self.category_buttons_frame = tk.Frame(self.window)
        self.category_buttons_frame.place(relx=0.5, rely=0.7, anchor="center")

        # Create list to hold category buttons
        self.category_buttons = []

    def back(self):
        self.window.destroy()
        self.root.deiconify()

    def create_category(self):
        # Create new window to input category name
        self.category_name_window = tk.Toplevel(self.window)
        self.category_name_window.title("Create Category")

        # Create label and entry for category name
        self.category_name_label = tk.Label(self.category_name_window, text="Category Name:")
        self.category_name_label.pack()
        self.category_name_entry = tk.Entry(self.category_name_window, width=20)
        self.category_name_entry.pack()

        # Create button to create category
        self.create_category_button = tk.Button(self.category_name_window, text="Create Category", command=self.add_category)
        self.create_category_button.pack()

    def add_category(self):
        # Get category name from entry
        category_name = self.category_name_entry.get()

        # Create new button for category
        category_button = tk.Button(self.category_buttons_frame, text=category_name, command=lambda category_name=category_name: self.open_category_window(category_name))
        category_button.pack()

        # Add button to list of category buttons
        self.category_buttons.append(category_button)

        # Close category name window
        self.category_name_window.destroy()

    def open_category_window(self, category_name):
        # Create new window for category
        self.category_window = UserCategoryWindow(self.window, category_name)

class UserCategoryWindow:
    def __init__(self, root, category_name):
        self.root = root
        self.window = tk.Toplevel(self.root)
        self.window.title(category_name)
        self.window.geometry("800x600")

        # Back button
        self.back_button = tk.Button(self.window, text="Back", command=self.back, width=10, height=2)
        self.back_button.place(relx=0, rely=0, anchor="nw", x=5, y=5)

        # Canvas and scrollbar setup
        self.canvas = tk.Canvas(self.window)
        self.scrollbar = tk.Scrollbar(self.window, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Frame inside the canvas
        self.item_options_frame = tk.Frame(self.canvas)

        # Create window in the canvas
        self.canvas.create_window((0, 0), window=self.item_options_frame, anchor="nw")

        # Pack canvas and scrollbar
        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Add widgets inside the item_options_frame
        self.populate_item_options()

        # Update the scroll region dynamically
        self.item_options_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

    def populate_item_options(self):
        # Add widgets to the item options frame
        tk.Label(self.item_options_frame, text="Item Name:").pack()
        tk.Entry(self.item_options_frame, width=20).pack()

        pricing_type_frame = tk.Frame(self.item_options_frame)
        pricing_type_frame.pack()
        tk.Button(pricing_type_frame, text="Unit", command=self.select_unit).pack(side="left")
        tk.Button(pricing_type_frame, text="Weight", command=self.select_weight).pack(side="left")

        tk.Label(self.item_options_frame, text="Price per Unit:").pack()
        tk.Entry(self.item_options_frame, width=20).pack()

        tk.Label(self.item_options_frame, text="Weight:").pack()
        tk.Entry(self.item_options_frame, width=20).pack()

        tk.Label(self.item_options_frame, text="Price by Weight:").pack()
        tk.Entry(self.item_options_frame, width=20).pack()

        tk.Label(self.item_options_frame, text="Quantity:").pack()
        tk.Entry(self.item_options_frame, width=20).pack()

        tk.Button(self.item_options_frame, text="Add Item", command=self.add_item).pack()
        tk.Button(self.item_options_frame, text="Edit Category", command=self.edit_category).pack()
        tk.Button(self.item_options_frame, text="Edit Item", command=self.edit_item).pack()

        quantity_frame = tk.Frame(self.item_options_frame)
        quantity_frame.pack()
        tk.Button(quantity_frame, text="Add Quantity", command=self.add_quantity).pack(side="left")
        tk.Button(quantity_frame, text="Subtract Quantity", command=self.subtract_quantity).pack(side="left")

    def back(self):
        self.window.destroy()

    def select_unit(self):
        print("Unit button clicked")

    def select_weight(self):
        print("Weight button clicked")

    def add_item(self):
        print("Add item button clicked")

    def edit_category(self):
        print("Edit category button clicked")

    def edit_item(self):
        print("Edit item button clicked")

    def add_quantity(self):
        print("Add quantity button clicked")

    def subtract_quantity(self):
        print("Subtract quantity button clicked")




class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)  # Pass the root to Toplevel
        self.window.title("IMS")
        self.window.geometry("400x400")

        # Create back button
        self.back_button = tk.Button(self.window, text="Back", command=self.back, width=10, height=2)
        self.back_button.place(relx=0, rely=0, anchor="nw", x=5, y=5)

        # Create a frame to hold the login form
        self.login_frame = tk.Frame(self.window)
        self.login_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Create labels and fields for the login form
        tk.Label(self.login_frame, text="Username:").grid(row=1, column=0, padx=5, pady=5)
        self.log_in = tk.Entry(self.login_frame, width=20)
        self.log_in.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.login_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        self.password = tk.Entry(self.login_frame, width=20, show="*")
        self.password.grid(row=2, column=1, padx=5, pady=5)

        # Create login button
        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def login(self):
        print("Login submitted")
        self.window.destroy()
        UserInventoryWindow(self.root)

    def back(self):
        self.window.destroy()
        self.root.deiconify()

class CreateInventoryWindow:
    def __init__(self, root):
        self.root = root
        self.window = tk.Toplevel(self.root)  # Pass the root to Toplevel
        self.window.title("IMS")
        self.window.geometry("400x400")

        # Create back button
        self.back_button = tk.Button(self.window, text="Back", command=self.back, width=10, height=2)
        self.back_button.place(relx=0, rely=0, anchor="nw", x=5, y=5)

        # Create a frame to hold the create inventory form
        self.create_inventory_frame = tk.Frame(self.window)
        self.create_inventory_frame.place(relx=0.5, rely=0.5, anchor="center")

         # Create labels and fields for the user name form
        tk.Label(self.create_inventory_frame, text="User Name:").grid(row=1, column=0, padx=5, pady=5)

        self.inventory_name = tk.Entry(self.create_inventory_frame, width=20)
        self.inventory_name.grid(row=1, column=1, padx=5, pady=5)

         # Create labels and fields for the password form
        tk.Label(self.create_inventory_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)

        self.inventory_name = tk.Entry(self.create_inventory_frame, width=20)
        self.inventory_name.grid(row=2, column=1, padx=5, pady=5)

        # Create labels and fields for the create inventory form
        tk.Label(self.create_inventory_frame, text="Inventory Name:").grid(row=3, column=0, padx=5, pady=5)

        self.inventory_name = tk.Entry(self.create_inventory_frame, width=20)
        self.inventory_name.grid(row=3, column=1, padx=5, pady=5)

        # Create create inventory button
        self.submit_button = tk.Button(self.create_inventory_frame, text="Create Inventory", command=self.submit)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def submit(self):
        print("Create inventory submitted")
        self.window.destroy()
        UserInventoryWindow(self.root)

    def back(self):
        self.window.destroy()
        self.root.deiconify()



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    login_screen = LoginScreen(root)
    root.mainloop()
