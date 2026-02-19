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
                ENG_sentence TEXT,
                Correct INT,
                Incorrect INT
            )
            """)
            conn.commit()

    def create_element_1(self, ENG_word, PL_translation, ENG_sentence, Correct, Incorrect):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_1_vocabulary (
            ENG_word, PL_translation, ENG_sentence, Correct, Incorrect
            )
            VALUES(?,?,?,?,?)
            """,
            (ENG_word, PL_translation, ENG_sentence, Correct, Incorrect))
            conn.commit()

    def get_random_element_1(self):
        """Zwraca losowy rekord z database_1_vocabulary jako dict lub None, jeśli tabela jest pusta."""
        with self.connect() as conn:
            # pozwala pobierać kolumny po nazwach
            conn.row_factory = __import__("sqlite3").Row
            c = conn.cursor()
            c.execute("""
                SELECT Ordinal_number, ENG_word, PL_translation, ENG_sentence, Correct, Incorrect
                FROM database_1_vocabulary
                ORDER BY RANDOM()
                LIMIT 1
            """)
            row = c.fetchone()
            return dict(row) if row else None


# ---------------------------------------------------------------------------------------
# database_2_1 - baza danych dla górnej części menu -> Word Formation
# ---------------------------------------------------------------------------------------

    def create_database_2_1(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_2_1_word_formation (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                Initial_sentence TEXT,
                Initial_word TEXT,
                Correct_word TEXT,
                PL_translation TEXT,
                Full_sentence TEXT,
                Correct INT,
                Incorrect INT
            )
            """)
            conn.commit()

    def create_element_2_1(self, Initial_sentence, Initial_word, Correct_word, PL_translation, Full_sentence, Correct, Incorrect):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_2_1_word_formation (
            Initial_sentence, Initial_word, Correct_word, PL_translation, Full_sentence, Correct, Incorrect
            )
            VALUES(?,?,?,?,?,?,?)
            """,
            (Initial_sentence, Initial_word, Correct_word, PL_translation, Full_sentence, Correct, Incorrect))
            conn.commit()


# ---------------------------------------------------------------------------------------
# database_2_2 - baza danych dla Transformations
# ---------------------------------------------------------------------------------------

    def create_database_2_2(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_2_2_transformations (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                Initial_sentence TEXT,
                Initial_word TEXT,
                Potential_sentence TEXT,
                Correct_answer TEXT,
                Correct_sentence TEXT,
                Correct INT,
                Incorrect INT
            )
            """)
            conn.commit()

    def create_element_2_2(self, Initial_sentence, Initial_word, Potential_sentence, Correct_answer, Correct_sentence, Correct, Incorrect):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_2_2_transformations (
            Initial_sentence, Initial_word, Potential_sentence, Correct_answer, Correct_sentence, Correct, Incorrect
            )
            VALUES(?,?,?,?,?,?,?)
            """,
            (Initial_sentence, Initial_word, Potential_sentence, Correct_answer, Correct_sentence, Correct, Incorrect))
            conn.commit()


# ---------------------------------------------------------------------------------------
# database_2_3 - baza danych dla Prepositions
# ---------------------------------------------------------------------------------------

    def create_database_2_3(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_2_3_prepositions (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                Initial_sentence TEXT,
                Correct_answer TEXT,
                Correct_sentence TEXT,
                Correct INT,
                Incorrect INT
            )
            """)
            conn.commit()

    def create_element_2_3(self, Initial_sentence, Correct_answer, Correct_sentence, Correct, Incorrect):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_2_3_prepositions (
            Initial_sentence, Correct_answer, Correct_sentence, Correct, Incorrect
            )
            VALUES(?,?,?,?,?)
            """,
            (Initial_sentence, Correct_answer, Correct_sentence, Correct, Incorrect))
            conn.commit()


# ---------------------------------------------------------------------------------------
# database_2_4 - baza danych dla Multiple choice
# ---------------------------------------------------------------------------------------

    def create_database_2_4(self):
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            CREATE TABLE IF NOT EXISTS database_2_4_multiple_choice (
                Ordinal_number INTEGER PRIMARY KEY AUTOINCREMENT,
                Initial_sentence TEXT,
                Variant_A TEXT,
                Variant_B TEXT,
                Variant_C TEXT,
                Variant_D TEXT,
                Correct_answer TEXT,
                Correct_sentence TEXT,
                Correct INT,
                Incorrect INT
            )
            """)
            conn.commit()

    def create_element_2_4(self, Initial_sentence, Variant_A, Variant_B, Variant_C, Variant_D, Correct_answer, Correct_sentence, Correct, Incorrect):

        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
            INSERT INTO database_2_4_multiple_choice (
            Initial_sentence, Variant_A, Variant_B, Variant_C, Variant_D, Correct_answer, Correct_sentence, Correct, Incorrect
            )
            VALUES(?,?,?,?,?,?,?,?,?)
            """,
            (Initial_sentence, Variant_A, Variant_B, Variant_C, Variant_D, Correct_answer, Correct_sentence, Correct, Incorrect))
            conn.commit()


# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------


# my_database = Database("database_1.db")
# my_database.create_database_1()
# my_database.create_element_1("cat","kot","My cat is nice.", 0, 0)
#
# my_database.create_element_1("meticulous","skrupulatny","She is meticulous about documenting every detail of the project.", 0, 0)
# my_database.create_element_1("inevitable","nieunikniony","Given the circumstances, a confrontation was inevitable.", 0, 0)
# my_database.create_element_1("resilient","odporny psychicznie","Children are often more resilient than adults assume.", 0, 0)
# my_database.create_element_1("scrutinize","dokładnie analizować","The committee will scrutinize the proposal before approving it.", 0, 0)
# my_database.create_element_1("contemplate","rozważać","He is contemplating a complete change of career.", 0, 0)
# my_database.create_element_1("subtle","subtelny","There was a subtle change in her tone that suggested irritation.", 0, 0)
# my_database.create_element_1("coherent","spójny","The argument was logical but not entirely coherent.", 0, 0)
# my_database.create_element_1("counterproductive","przynoszący odwrotny skutek","Constant criticism can be counterproductive in the long run.", 0, 0)
# my_database.create_element_1("deliberate","zamierzony","His silence was deliberate and meant to send a message.", 0, 0)

# aby dodać pojedyncze rekordy do bazy danych database_1:
# my_database = Database("database_1.db")
# my_database.create_element_1("alleviate","łagodzić, zmniejszać","This policy aims to alleviate the pressure on small businesses.", 0, 0)




# my_database2 = Database("database_2_1.db")
# my_database2.create_database_2_1()
# my_database2.create_element_2_1(
#     "The manager’s refusal to explain his decision only increased the staff’s sense of ...",
#     "UNDERSTAND",
#     "misunderstanding",
#     "nieporozumienie",
#     "The manager’s refusal to explain his decision only increased the staff’s sense of misunderstanding.",
#     0,
#     0)


# my_database3 = Database("database_2_2.db")
# my_database3.create_database_2_2()
# my_database3.create_element_2_2(
#     "It was only after the meeting had ended that he realised how serious the situation was.",
#     "DID",
#     "Not until the meeting had ended ... how serious the situation was.",
#     "did he realise",
#     "Not until the meeting had ended did he realise how serious the situation was.",
#     0,
#     0)


# my_database4 = Database("database_2_3.db")
# my_database4.create_database_2_3()
# my_database4.create_element_2_3(
#     "If you don't ... our demands, we will destroy your business.",
#     "meet",
#     "If you don't meet our demands, we will destroy your business.",
#     0,
#     0)


# my_database5 = Database("database_2_4.db")
# my_database5.create_database_2_4()
# my_database5.create_element_2_4(
#     "He was ... intensively before the tennis tournament.",
#     "practised",
#     "coached",
#     "learned",
#     "taught",
#     "coached",
#     "He was coached intensively before the tennis tournament.",
#     0,
#     0)



my_database = Database()
rec = my_database.get_random_element_1()
if rec is None:
    print("Brak danych w tabeli.")
else:
    print(f"{rec['ENG_word']} → {rec['PL_translation']}\n{rec['ENG_sentence']}")
