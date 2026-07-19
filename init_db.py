import sqlite3
import hashlib

connection = sqlite3.connect("users.db")

cursor = connection.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS users(

id INTEGER PRIMARY KEY AUTOINCREMENT,

username TEXT,

password TEXT

)

""")

password = hashlib.md5("admin123".encode()).hexdigest()

cursor.execute(

"INSERT INTO users(username,password) VALUES(?,?)",

("admin",password)

)

connection.commit()

connection.close()

print("Database Created Successfully.")