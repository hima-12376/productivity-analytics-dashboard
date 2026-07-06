from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "activity.db"


def create_database():

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activities(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        application TEXT,

        category TEXT,

        window_title TEXT,

        start_time TEXT,

        end_time TEXT,

        duration INTEGER

    )
    """)

    conn.commit()

    conn.close()


def insert_activity(
    application,
    category,
    window_title,
    start_time,
    end_time,
    duration
):
    """
    Saves one completed activity session.
    """

    conn = sqlite3.connect(DB_PATH)

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO activities(

            application,

            category,

            window_title,

            start_time,

            end_time,

            duration

        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (

        application,

        category,

        window_title,

        start_time.isoformat(),

        end_time.isoformat(),

        duration

    ))

    conn.commit()

    conn.close()