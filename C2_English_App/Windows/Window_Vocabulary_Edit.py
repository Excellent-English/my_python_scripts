import customtkinter as ctk
# from click import command
from PIL import Image
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

    def go_back_to_menu():
        vocabulary_edit_page.destroy()
        menu_page.deiconify()

    vocabulary_edit_page.return_button.configure(command=go_back_to_menu)
    vocabulary_edit_page.bind("<Escape>", lambda event: go_back_to_menu())

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji change_word() lub check_answer()
    def on_enter(event=None):
        is_enabled = str(button_update.cget("state")) == "normal"
        if is_enabled:
            change_or_add()
        else:
            check_word()

    # Powiązanie z oknem (obsłuży Enter z głównej klawiatury i z klawiatury numerycznej)
    vocabulary_edit_page.bind("<Return>", on_enter)
    vocabulary_edit_page.bind("<KP_Enter>", on_enter)

    # ustawienie jedynki (zarówno u góry jak i z klawiatury numerycznej) na odsłuchanie zdania angielskiego
    vocabulary_edit_page.bind('1', lambda event: refresh_word())
    vocabulary_edit_page.bind('<KP_1>', lambda event: refresh_word())

    def refresh_word():
        entry_box_word.delete(0, ctk.END)
        entry_box_translation.delete(0, ctk.END)
        entry_box_sentence.delete(0, ctk.END)
        label_enter_to_update.configure(text="")
        label_check_result.configure(text="Press Enter", text_color="#808080")
        button_update.configure(state="disabled")
        vocabulary_edit_page.after(100, entry_box_word.focus_set)


    def check_word():
        eng_word = entry_box_word.get()

        # wyczyść poprzednie wartości w polach outputu
        entry_box_translation.delete(0, ctk.END)
        entry_box_sentence.delete(0, ctk.END)

        exists = my_database.word_exists_1(eng_word)
        if exists:
            label_check_result.configure(text="The word exists in your dictionary.", text_color="#6FBF73")
            vocabulary_edit_page.after(100, entry_box_translation.focus_set)
            button_update.configure(state="normal")
            label_enter_to_update.configure(text="Press Enter")
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
    label_check_result = App_Label_Standard(vocabulary_edit_page, font=("Open Sans", 12), text="Press Enter")
    label_check_result.place(x=500, y=230)
    label_enter_to_update = App_Label_Standard(vocabulary_edit_page, font=("Open Sans", 12))
    label_enter_to_update.place(x=500, y=430)
    label_press_1 = App_Label_Standard(vocabulary_edit_page, font=("Open Sans", 12), text="Press 1")
    label_press_1.place(x=665, y=175)

    entry_box_word = App_Entry_Box(vocabulary_edit_page)
    vocabulary_edit_page.after(300, entry_box_word.focus_set)
    entry_box_word.place(x=280, y=170)

    entry_box_translation = App_Entry_Box(vocabulary_edit_page)
    entry_box_translation.place(x=280, y=320)
    entry_box_sentence = App_Entry_Box(vocabulary_edit_page, width=650)
    entry_box_sentence.place(x=105, y=370)

    button_check = Button_Standard(vocabulary_edit_page, font = ("Open Sans", 16), width=100, height=40, text="Check", command=check_word)
    button_check.place(x=380, y=225)
    button_update = Button_Standard(vocabulary_edit_page, state = "disabled", font = ("Open Sans", 16), width=100, height=40, text="Update", command=change_or_add)
    button_update.place(x=380, y=425)

    # Dodanie przycisku zawierającego ikonę refresh- przycisk odświeża dane na ekranie
    image = Image.open("../Images/Refresh_icon.png")
    refresh_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    button_refresh = ctk.CTkButton(
        vocabulary_edit_page,
        image=refresh_icon,
        text="",
        width=35, height=35,
        fg_color="white",
        hover_color="white",
        border_width=1,
        border_color="#d7dbe0",
        command= refresh_word
    )
    button_refresh.image = refresh_icon
    button_refresh.place(x=615, y=170)




    vocabulary_edit_page.mainloop()

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_edit(main_page)