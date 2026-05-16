import sqlite3

class Database:
    def __init__(self, name="timer.db"):
        self.name = name

    def connect(self):
        return sqlite3.connect(self.name)

    def create_table(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS timer (
                LP INTEGER PRIMARY KEY AUTOINCREMENT,
                Name INTEGER,
                Result INTEGER
            )
            """)
            conn.commit()


my_database = Database()
my_database.create_table()