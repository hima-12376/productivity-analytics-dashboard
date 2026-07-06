import sqlite3
import pandas as pd
from pathlib import Path

DB_PATH = Path(__file__).parent / "activity.db"


class ActivityRepository:

    def get_all_sessions(self):
        conn = sqlite3.connect(DB_PATH)

        df = pd.read_sql_query(
            "SELECT * FROM activities",
            conn
        )

        conn.close()

        return df