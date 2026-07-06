import sqlite3

conn = sqlite3.connect("database/activity.db")

cursor = conn.cursor()

cursor.execute("PRAGMA table_info(activities)")

print(cursor.fetchall())

conn.close()