import sqlite3

class Database:
    def __init__(self, name="players.db"):
        self.name = name

    def connect(self):
        return sqlite3.connect(self.name)

    def create_table(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS players (
                LP INTEGER PRIMARY KEY AUTOINCREMENT,
                ID INTEGER,
                Name STRING,
                TeamID INTEGER,
                Age INTEGER,
                Country INTEGER,
                Value INTEGER,
                Salary INTEGER,
                Price INTEGER,
                EndOfSale STRING,
                Stamina INTEGER,
                Speed INTEGER,
                Technique INTEGER,
                Passing INTEGER,
                GK INTEGER,
                DEF INTEGER,
                MID INTEGER,
                ATT INTEGER
            )
            """)
            conn.commit()