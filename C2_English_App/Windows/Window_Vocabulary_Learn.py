import customtkinter as ctk

from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Frame import AppFrame
from C2_English_App.AllClasses.Button_Standard import Button_Standard
from C2_English_App.AllClasses.App_Database import Database
from C2_English_App.AllClasses.App_Entry_Box import App_Entry_Box


def run_vocabulary_learn(menu_page):
# Zamknij / ukryj główne okno
    menu_page.withdraw()
    vocabulary_learn_page = AppWindow(banner_text = "Learn and remember your words")

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

    def generate_random_list_of_words():
        my_database = Database("../Databases/database_1.db")
        amount = 2
        with my_database.connect() as conn:
            words_dict = get_random_words(conn, amount)
        print(words_dict)

    generate_random_list_of_words()

# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie
# ---------------------------------------------------------------------------------------

# 3 frame'y dla tekstów widocznych w oknie aplikacji
    frame_eng = AppFrame(vocabulary_learn_page)
    frame_eng.place(x=60, y=320)
    frame_pl = AppFrame(vocabulary_learn_page)
    frame_pl.place(x=470, y=320)

# 3 labele z tekstami: eng, pl, sentence
    label_eng = App_Label_Standard(frame_eng, justify="center", anchor="center", text="", text_color="white")
    label_eng.place(relx=0.5, rely=0.5, anchor="center")
    label_pl = App_Label_Standard(frame_pl, justify="center", anchor="center", text="", text_color="white")
    label_pl.place(relx=0.5, rely=0.5, anchor="center")

# labele z tekstami: opis okna, znak równości, Enter, jedynka do odsłuchania zdania
    label_description = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 20), wraplength=700, width=700,
                                           justify="center", anchor="center",
                                           text="How many words would you like to learn today?")
    label_description.place(x=85, y=120)
    label_equal = App_Label_Standard(vocabulary_learn_page, text="=")
    label_equal.place(x=425, y=350)
    label_enter_right = App_Label_Standard(vocabulary_learn_page, text_color="white", font=("Open Sans", 12), text="press Enter")
    label_enter_right.place(x=608, y=270)
    label_enter_left = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 12), text="press Enter")
    label_enter_left.place(x=100, y=250)

# 2 buttony: Check
    button_check = Button_Standard(vocabulary_learn_page, font=("Open Sans", 16), width=100, height=40, text="Check")
    button_check.place(x=595, y=230)

# 1 entry box do wpisywania angielskiego słówka
    entry_box_eng = App_Entry_Box(vocabulary_learn_page, width=80)
    entry_box_eng.place(x=397, y=160)
    vocabulary_learn_page.after(100, entry_box_eng.focus_set)

# rzeczy potrzebne do progress bara + wynik procentowy
    progress = 0.5
    progress_bar = ctk.CTkProgressBar(vocabulary_learn_page, width=300)
    progress_bar.place(x=285, y=435)
    progress_bar.set(progress)  # start od 0%

    label_percentage = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 12), text=f'{progress*100}%')
    label_percentage.place(x=415, y=450)






    vocabulary_learn_page.mainloop()




if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_learn(main_page)