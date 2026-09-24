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
                Name STRING,
                Result REAL
            )
            """)
            conn.commit()


    def add_result(self, Name, Result):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO timer (
            Name, Result
            )
            VALUES(?, ?)
            """,
            (Name, Result))
            conn.commit()
            return c.lastrowid


    def get_place(self, lp):
        """
        Zwraca miejsce (1 = najlepsze) dla rekordu o podanym LP.
        Ranking: rosnąco po Result, a przy remisach rosnąco po LP.
        """
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            SELECT place
            FROM (
                SELECT
                    LP,
                    ROW_NUMBER() OVER (ORDER BY Result ASC, LP ASC) AS place
                FROM timer
            )
            WHERE LP = ?
            """, (lp,))
            row = c.fetchone()
            return row[0] if row else None
            # ROW_NUMBER() i OVER(...) to window functions w SQLite [3](https://sqlite.org/windowfunctions.html)[4](https://coddy.tech/docs/sqlite/window-functions)

    def count_results(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM timer")
            return c.fetchone()[0]



my_database = Database()
my_database.create_table()