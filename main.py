import tkinter as tk
from tkinter import messagebox

class CarRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Management System")
        self.root.geometry("500x300")

        title = tk.Label(
            root,
            text="Car Rental Management System",
            font=("Arial", 16, "bold")
        )
        title.pack(pady=20)

        btn_customer = tk.Button(
            root,
            text="Add Customer",
            width=20,
            command=self.add_customer
        )
        btn_customer.pack(pady=10)

        btn_car = tk.Button(
            root,
            text="View Available Cars",
            width=20,
            command=self.view_cars
        )
        btn_car.pack(pady=10)

        btn_exit = tk.Button(
            root,
            text="Exit",
            width=20,
            command=root.quit
        )
        btn_exit.pack(pady=10)

    def add_customer(self):
        messagebox.showinfo("Info", "Add Customer Clicked")

    def view_cars(self):
        messagebox.showinfo("Info", "View Cars Clicked")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalApp(root)
    root.mainloop()
