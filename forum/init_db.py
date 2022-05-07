import os
import sqlite3

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
DB_PATH = f"{BASE_PATH}/database.sqlite"

if os.path.isfile(DB_PATH):
    os.remove(DB_PATH)

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

with open(f"{BASE_PATH}/schema.sql") as f:
    cursor.executescript(f.read())

with open(f"{BASE_PATH}/init.sql") as f:
    cursor.executescript(f.read())

connection.commit()

cursor.close()
connection.close()

print("Database created successfully.")
