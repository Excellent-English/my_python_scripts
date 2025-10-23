import sqlite3

class Database:
    def __init__(self, name="zawodnicy.db"):
        self.name = name

    def connect(self):
        return sqlite3.connect(self.name)

    def create_table(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS zawodnicy (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                idZAWODNIKA INTEGER,
                imie TEXT,
                kondycja INTEGER,
                technika INTEGER,
                strzelec INTEGER
            )
            """)
            conn.commit()