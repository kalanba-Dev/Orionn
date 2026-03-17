import sqlite3

db = sqlite3.connect("database.db")

cursor = db.cursor()

cursor.execute("""
CREATE TABLE users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
email TEXT,
password TEXT
)
""")

db.commit()
db.close()

print("Base de datos creada")
