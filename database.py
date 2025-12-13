import sqlite3


conn = sqlite3.connect("car_rental.db")
cursor = conn.cursor()


cursor.execute(
"""
CREATE TABLE IF NOT EXISTS customers (
customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
contact TEXT,
email TEXT,
license_no TEXT,
address TEXT
)
"""
)


cursor.execute(
"""
CREATE TABLE IF NOT EXISTS cars (
car_id TEXT PRIMARY KEY,
brand TEXT,
model TEXT,
year TEXT,
rent_price REAL,
status TEXT
)
"""
)


cursor.execute(
"""
CREATE TABLE IF NOT EXISTS rentals (
rental_id INTEGER PRIMARY KEY AUTOINCREMENT,
customer_id INTEGER,
car_id TEXT,
start_date TEXT,
end_date TEXT,
total_cost REAL
)
"""
)


cursor.execute(
"""
CREATE TABLE IF NOT EXISTS payments (
payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
rental_id INTEGER,
amount REAL,
method TEXT,
status TEXT,
date TEXT
)
"""