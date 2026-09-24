from PlayerDatabase import PlayerDatabase

def test_connection():
    try:
        db = PlayerDatabase()
        with db.connect() as conn:
            with conn.cursor() as c:
                c.execute("SELECT 1;")
                result = c.fetchone()
                print("[DEBUG] Połączenie z AWS PostgreSQL działa:", result)
        return True
    except Exception as e:
        print("[ERROR] Nie udało się połączyć z bazą:", e)
        return False

def main():
    if not test_connection():
        print("[DEBUG] Kończę program, bo baza nie działa.")
        return
    print("[DEBUG] Można lecieć dalej ze skraperem.")
    # tutaj Twój dalszy kod
    # np. scrape players
    # db = PlayerDatabase()
    # db.create_player(player)

if __name__ == "__main__":
    main()