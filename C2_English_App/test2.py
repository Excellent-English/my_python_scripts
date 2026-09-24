from C2_English_App.AllClasses.App_Database import Database

def get_random_words(conn, limit: int) -> dict:
    cursor = conn.cursor()

    cursor.execute("""
        SELECT ENG_word, PL_translation, ENG_sentence
        FROM database_1_vocabulary
        ORDER BY RANDOM()
        LIMIT ?
    """, (limit,))

    rows = cursor.fetchall()

    return {eng: [pl, sentence] for eng, pl, sentence in rows}


def start_quiz():
    my_database = Database("Databases/database_1.db")
    amount = 2
    with my_database.connect() as conn:
        words_dict = get_random_words(conn, amount)
    print(words_dict)


start_quiz()