import datetime
from tkinter import messagebox


class RentalModule:
def add_rental(self, customer_id, car_id, start_date, end_date, price):
start = datetime.datetime.strptime(start_date, "%Y-%m-%d")
end = datetime.datetime.strptime(end_date, "%Y-%m-%d")


if end <= start:
raise ValueError("End date must be after start date")


days = (end - start).days
total = days * price


cursor.execute(
"INSERT INTO rentals VALUES (NULL,?,?,?,?,?)",
(customer_id, car_id, start_date, end_date, total)
)
cursor.execute("UPDATE cars SET status='Rented' WHERE car_id=?", (car_id,))
conn.commit()
messagebox.showinfo("Success", "Rental added successfully")