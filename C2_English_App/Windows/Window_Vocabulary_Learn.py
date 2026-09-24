import customtkinter as ctk
import random

from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Frame import AppFrame
from C2_English_App.AllClasses.App_Database import Database
from C2_English_App.AllClasses.App_Entry_Box import App_Entry_Box

random_eng = "aaa"
random_pl = "aaa"
words_left = ""
attempts_correct = 0
attempts_wrong = 0
progress = 0.0
random_dict = {}


def run_vocabulary_learn(menu_page):
# Zamknij / ukryj główne okno
    menu_page.withdraw()
    vocabulary_learn_page = AppWindow(banner_text = "Learn and remember your words")


# ---------------------------------------------------------------------------------------
# funkcje i opcje używane podczas pracy z aplikacją
# ---------------------------------------------------------------------------------------

    def go_back_to_menu():
        vocabulary_learn_page.destroy()
        menu_page.deiconify()

    vocabulary_learn_page.return_button.configure(command=go_back_to_menu)
    vocabulary_learn_page.bind("<Escape>", lambda event: go_back_to_menu())


    def get_random_words(conn, limit: int) -> dict:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT ENG_word, PL_translation
            FROM database_1_vocabulary
            ORDER BY RANDOM()
            LIMIT ?
        """, (limit,))

        rows = cursor.fetchall()
        vocabulary_learn_page.after(300, entry_box_eng_word.focus_set)
        return {eng: pl for eng, pl in rows}


    def generate_random_list_of_words(event=None):
        global words_left
        entry_box_number.configure(state="disabled")
        words_left = int(entry_box_number.get())
        label_words_left.configure(text=f"Words to learn: {words_left}")
        my_database = Database("../Databases/database_1.db")
        with my_database.connect() as conn:
            words_dict = get_random_words(conn, words_left)
        return words_dict


    def learn_random_list_of_words(event=None):
        global random_pl, random_eng, random_dict
        random_dict = generate_random_list_of_words()
        print(random_dict)
        print(len(random_dict))
        random_eng, random_pl = random.choice(list(random_dict.items()))
        print(random_eng, random_pl)

        label_pl.configure(text=random_pl)
        return random_dict, random_pl, random_eng

    def check_if_correct():
        global random_pl, random_eng, attempts_correct, attempts_wrong, progress, random_dict
        print(random_dict)
        if random_eng == entry_box_eng_word.get().strip(): # if the translation is correct
            print("ok")
            frame_pl.configure(fg_color="#A8E6A3")
            label_pl.configure(fg_color="#A8E6A3", text_color= "#808080")
            entry_box_eng_word.configure(fg_color="#A8E6A3", text_color= "#808080")

            del random_dict[random_eng]
            words_left = len(random_dict)
            label_words_left.configure(text=f"Words to learn: {words_left}")

            random_eng, random_pl = random.choice(list(random_dict.items()))

            frame_pl.after(3000, lambda: (
            frame_pl.configure(fg_color="transparent"),
            label_pl.configure(fg_color="white"),
            entry_box_eng_word.configure(fg_color="#f1f4f9", text_color="#4d4d4d"),
            entry_box_eng_word.delete(0, "end"),
            print(random_eng),
            print(random_pl),
            label_pl.configure(text=random_pl)
            ))

            attempts_correct += 1
            if attempts_wrong == 0:
                progress = 0
            else:
                progress = attempts_correct / (attempts_correct + attempts_wrong)
            progress_bar.set(progress)
            label_percentage.configure(text=f"{progress * 100:.1f}%")
            print(attempts_correct)
            print(attempts_wrong)

        else: # if the translation is wrong
            print("nie ok")
            frame_pl.configure(fg_color="#F8D7DA")
            label_pl.configure(fg_color="#F8D7DA", text_color= "#808080")
            entry_box_eng_word.configure(fg_color="#F8D7DA", text_color= "#808080")

            random_eng, random_pl = random.choice(list(random_dict.items()))

            frame_pl.after(5000, lambda: (
            frame_pl.configure(fg_color="transparent"),
            label_pl.configure(fg_color="white"),
            entry_box_eng_word.configure(fg_color="#f1f4f9", text_color="#4d4d4d"),
            entry_box_eng_word.delete(0, "end"),
            print(random_eng),
            print(random_pl),
            label_pl.configure(text=random_pl)
            ))

            attempts_wrong += 1
            if attempts_wrong == 0:
                progress = 0
            else:
                progress = attempts_correct / (attempts_correct + attempts_wrong)
            progress_bar.set(progress)
            label_percentage.configure(text=f"{progress * 100:.1f}%")
            print(attempts_correct)
            print(attempts_wrong)



        return attempts_correct, attempts_wrong

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji change_word() lub check_answer()
    def on_enter(event=None):
        is_enabled = str(entry_box_number.cget("state")) == "normal"
        if is_enabled:
            learn_random_list_of_words()
        else:
            check_if_correct()

    # Powiązanie z oknem (obsłuży Enter z głównej klawiatury i z klawiatury numerycznej)
    vocabulary_learn_page.bind("<Return>", on_enter)
    vocabulary_learn_page.bind("<KP_Enter>", on_enter)

# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie
# ---------------------------------------------------------------------------------------

# 3 frame'y dla tekstów widocznych w oknie aplikacji
    frame_pl = AppFrame(vocabulary_learn_page)
    frame_pl.place(x=60, y=290)

# label z polskim tłumaczeniem + entry box do wpisywania tłumaczenia
    label_pl = App_Label_Standard(frame_pl, justify="center", anchor="center", text="")
    label_pl.place(relx=0.5, rely=0.5, anchor="center")

    entry_box_eng_word = App_Entry_Box(vocabulary_learn_page, width=350, height=80)
    entry_box_eng_word.place(x=470, y=290)

# labele z tekstami: opis okna, znak równości, Enter, jedynka do odsłuchania zdania
    label_description = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 20), wraplength=700, width=700,
                                           justify="center", anchor="center",
                                           text="How many words would you like to learn today?")
    label_description.place(x=85, y=120)
    label_equal = App_Label_Standard(vocabulary_learn_page, text="=")
    label_equal.place(x=425, y=320)
    label_press_enter = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 12), text="press Enter")
    label_press_enter.place(x=490, y=165)

    label_words_left = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 14), text=f"Words to learn: {words_left}")
    label_words_left.place(x=375, y=240)

# 1 entry box do wpisywania angielskiego słówka
    entry_box_number = App_Entry_Box(vocabulary_learn_page, width=80)
    entry_box_number.place(x=397, y=160)
    vocabulary_learn_page.after(300, entry_box_number.focus_set)

# rzeczy potrzebne do progress bara + wynik procentowy
    progress_bar = ctk.CTkProgressBar(vocabulary_learn_page, width=300, height=30, progress_color="#22c55e", fg_color="#f1f4f9", border_color="#d7dbe0", border_width=1)
    progress_bar.place(x=275, y=395)
    progress_bar.set(progress)

    label_percentage = App_Label_Standard(vocabulary_learn_page, font=("Open Sans", 12), text=f'{progress*100}%')
    label_percentage.place(x=415, y=425)




    vocabulary_learn_page.mainloop()


if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_learn(main_page)