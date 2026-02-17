import sqlite3

class Database:
    def __init__(self, name="vocabulary.db"):
        self.name = name

    def connect(self):
        return sqlite3.connect(self.name)

# ---------------------------------------------------------------------------------------
# database_1 - baza danych dla górnej części menu -> Vocabulary
# ---------------------------------------------------------------------------------------

    def create_database_1(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_1_vocabulary (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                ENG_word TEXT,
                PL_translation TEXT,
                ENG_sentence TEXT
            )
            """)
            conn.commit()

    def create_element_1(self, ENG_word, PL_translation, ENG_sentence):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_1_vocabulary (
            ENG_word, PL_translation, ENG_sentence
            )
            VALUES(?,?,?)
            """,
            (ENG_word, PL_translation, ENG_sentence))
            conn.commit()


# ---------------------------------------------------------------------------------------
# database_2_1 - baza danych dla górnej części menu -> Word Formation
# ---------------------------------------------------------------------------------------

    def create_database_2_1(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_2_1_word_formation (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                ENG_word TEXT,
                PL_translation TEXT,
                ENG_sentence TEXT
            )
            """)
            conn.commit()

    def create_element_2_1(self, ENG_word, PL_translation, ENG_sentence):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_2_1_word_formation (
            ENG_word, PL_translation, ENG_sentence
            )
            VALUES(?,?,?)
            """,
            (ENG_word, PL_translation, ENG_sentence))
            conn.commit()






my_database = Database("database_1.db")
my_database.create_database_1()
my_database.create_element_1("cat","kot","My cat is nice.")

my_database2 = Database("database_2_1.db")
my_database2.create_database_2_1()
my_database2.create_element_2_1("dog","pies","My dog is nice.")