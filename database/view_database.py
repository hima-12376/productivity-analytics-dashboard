import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "activity.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

cursor.execute("""
SELECT
    id,
    application,
    window_title,
    start_time,
    end_time,
    duration
FROM activities
""")

rows = cursor.fetchall()

print("\nActivity History\n")

for row in rows:
    print(row)

conn.close()