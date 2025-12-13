class CarModule:
def get_available_cars(self):
cursor.execute("SELECT * FROM cars WHERE status='Available'")
return cursor.fetchall()