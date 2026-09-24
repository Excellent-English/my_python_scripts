import os
import psycopg
from dotenv import load_dotenv
load_dotenv()

class Database:
    def __init__(self):
        self.host = os.environ["AWS_PG_HOST"]
        self.port = os.environ["AWS_PG_PORT"]
        self.dbname = os.environ["AWS_PG_DB"]
        self.user = os.environ["AWS_PG_USER"]
        self.password = os.environ["AWS_PG_PASSWORD"]
        self.sslmode = os.environ["AWS_PG_SSLMODE"]


    def connect(self):
        return psycopg.connect(host = self.host, port = self.port, dbname = self.dbname,  user = self.user,  password = self.password, sslmode = self.sslmode)

    def create_table(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS players (
                LP INTEGER PRIMARY KEY AUTOINCREMENT,
                Season INTEGER,
                Round INTEGER,
                ID INTEGER,
                Name STRING,
                TeamID INTEGER,
                Age INTEGER,
                Country INTEGER,
                Value INTEGER,
                Salary INTEGER,
                Price INTEGER,
                EndOfSale STRING,
                Matches INTEGER,
                Goals INTEGER,
                Assists INTEGER,
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