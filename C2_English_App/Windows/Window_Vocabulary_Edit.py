import customtkinter as ctk
from click import command

from C2_English_App.AllClasses.App_Database import Database
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Entry_Box import App_Entry_Box
from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.Button_Standard import Button_Standard


def run_vocabulary_edit(menu_page):
    menu_page.withdraw()
    vocabulary_edit_page = AppWindow(banner_text = "Modify your dictionary")

    my_database = Database("../Databases/database_1.db")


# -----------------------------------------------------------------------------------------------------------------
# funkcje i opcje używane podczas pracy z aplikacją: sprawdzanie słowa, aktualizacja lub dodanie słowa
# -----------------------------------------------------------------------------------------------------------------

    def check_word():
        eng_word = entry_box_word.get()

        # wyczyść poprzednie wartości w polach outputu
        entry_box_translation.delete(0, ctk.END)
        entry_box_sentence.delete(0, ctk.END)

        exists = my_database.word_exists_1(eng_word)
        if exists:
            label_check_result.configure(text="The word exists in your dictionary.", text_color="#6FBF73")

            record = my_database.get_word_1(eng_word)
            if record:
                pl = record.get("PL_translation", "") or ""
                sent = record.get("ENG_sentence", "") or ""
                entry_box_translation.insert(0, pl)
                entry_box_sentence.insert(0, sent)

        else:
            label_check_result.configure(text="The word doesn't exist in your dictionary.", text_color="#E57373")

    def change_or_add():
        eng_word = entry_box_word.get()
        pl = entry_box_translation.get()
        sentence = entry_box_sentence.get()

        result = my_database.create_or_update_word_1(eng_word, pl, sentence)

        if result == "updated":
            label_check_result.configure(
                text="Record updated.",
                text_color="#2E7D32"
            )
        elif result == "inserted":
            label_check_result.configure(
                text="New record added.",
                text_color="#2E7D32"
            )


# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie
# ---------------------------------------------------------------------------------------

    label_question = App_Label_Standard(vocabulary_edit_page, font=("Open Sans", 20), wraplength=700, width=700, text= "Which word would you like to check/modify?")
    label_question.place(x=230, y=120)
    label_check_result = App_Label_Standard(vocabulary_edit_page, font=("Open Sans", 12))
    label_check_result.place(x=500, y=230)

    entry_box_word = App_Entry_Box(vocabulary_edit_page)
    entry_box_word.place(x=280, y=170)
    entry_box_translation = App_Entry_Box(vocabulary_edit_page, justify="left")
    entry_box_translation.place(x=120, y=320)
    entry_box_sentence = App_Entry_Box(vocabulary_edit_page, justify="left", width=500)
    entry_box_sentence.place(x=120, y=370)

    button_check = Button_Standard(vocabulary_edit_page, font = ("Open Sans", 16), width=100, height=40, text="Check", command=check_word)
    button_check.place(x=380, y=225)
    button_start = Button_Standard(vocabulary_edit_page, font = ("Open Sans", 16), width=150, height=90, text="CHANGE / ADD", command=change_or_add)
    button_start.place(x=650, y=320)



    vocabulary_edit_page.mainloop()

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_edit(main_page)