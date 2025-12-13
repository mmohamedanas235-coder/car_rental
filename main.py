import tkinter as tk

class CarRentalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Rental Management System")

if __name__ == "__main__":
    root = tk.Tk()
    app = CarRentalApp(root)
    root.mainloop()
