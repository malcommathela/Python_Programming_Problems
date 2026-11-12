import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO students(name, marks) VALUES (?, ?)", ("Rahul", 85))
cursor.execute("INSERT INTO students(name, marks) VALUES (?, ?)", ("Priya", 92))

conn.commit()
conn.close()

print("Records inserted successfully")