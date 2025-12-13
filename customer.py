from tkinter import messagebox


class CustomerModule:
def add_customer(self, name, contact, email, license_no, address):
cursor.execute(
"INSERT INTO customers VALUES (NULL,?,?,?,?,?)",
(name, contact, email, license_no, address)
)
conn.commit()
messagebox.showinfo("Success", "Customer added successfully")