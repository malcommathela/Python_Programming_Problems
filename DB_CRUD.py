import sqlite3

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Update
cursor.execute(
    "UPDATE students SET marks=? WHERE name=?",
    (95, "Rahul")
)

# Delete
cursor.execute(
    "DELETE FROM students WHERE name=?",
    ("Priya",)
)

conn.commit()
conn.close()

print("Record updated and deleted successfully")