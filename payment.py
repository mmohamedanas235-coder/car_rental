class PaymentModule:
def add_payment(self, rental_id, amount, method, status, date):
cursor.execute(
"INSERT INTO payments VALUES (NULL,?,?,?,?,?)",
(rental_id, amount, method, status, date)
)
conn.commit()