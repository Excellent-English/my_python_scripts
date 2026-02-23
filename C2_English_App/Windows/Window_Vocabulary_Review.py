import customtkinter as ctk
from openpyxl.styles.builtins import comma

from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Frame import AppFrame
from C2_English_App.AllClasses.Button_Standard import Button_Standard
from C2_English_App.AllClasses.App_Database import Database


def run_vocabulary_review(menu_page):
    menu_page.withdraw()
    vocabulary_review_page = AppWindow(banner_text = "Review your dictionary")

# Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    vocabulary_review_page.bind('<Return>', lambda event: change_word())

# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie- 3 framy, 6 labeli i 1 button
# ---------------------------------------------------------------------------------------

# 3 frame'y dla tekstów widocznych w oknie aplikacji
    frame_eng = AppFrame(vocabulary_review_page)
    frame_eng.place(x=60, y=200)
    frame_pl = AppFrame(vocabulary_review_page)
    frame_pl.place(x=470, y=200)
    frame_sentence = AppFrame(vocabulary_review_page, width= 690, height= 70)
    frame_sentence.place(x=100, y=300)

# 3 labele z tekstami: eng, pl, sentence
    label_eng = App_Label_Standard(frame_eng, justify="center", anchor="center", text="")
    label_eng.place(relx=0.5, rely=0.5, anchor="center")
    label_pl = App_Label_Standard(frame_pl, justify="center", anchor="center", text="")
    label_pl.place(relx=0.5, rely=0.5, anchor="center")
    label_sentence = App_Label_Standard(frame_sentence, wraplength = 690, justify="center", anchor="center", text="")
    label_sentence.place(relx=0.5, rely=0.5, anchor="center")

# 3 labele z tekstami: opis okna, znak równości, Enter
    label_description = App_Label_Standard(vocabulary_review_page, font = ("Open Sans", 16) , wraplength = 700, width=700, justify="center", anchor="center", text="W tym oknie masz możliwość przeglądania słówek dodanych do Twojej bazy.\nW celu sprawdzenia kolejnego słówka, naciskaj klawisz >> (lub wybierz Enter na klawiaturze).\nMiłej nauki!")
    label_description.place(x=90, y=110)
    label_equal = App_Label_Standard(vocabulary_review_page, text="=")
    label_equal.place(x=425, y=230)
    label_enter = App_Label_Standard(vocabulary_review_page, font = ("Open Sans", 12), text="press Enter")
    label_enter.place(x=400, y=450)

# ustawienie buttona do zmieniania słówek oraz funkcja change_word generująca nowy zestaw
    def change_word():
        my_database = Database("../Databases/database_1.db")
        random_line = my_database.get_random_element_1()
        eng, pl, sentence = random_line

        label_eng.configure(text=eng)
        label_pl.configure(text=pl)
        label_sentence.configure(text=sentence)

# button >>
    button = Button_Standard(vocabulary_review_page, width= 100, height= 40, text = ">>", command=change_word)
    button.place(x=387, y=400)

# ---------------------------------------------------------------------------------------
# ustawienie pierwszego zestawu danych
# ---------------------------------------------------------------------------------------

# wywołanie randomowego rekordu z database_1
    my_database = Database("../Databases/database_1.db")
    random_line = my_database.get_random_element_1()
    eng, pl, sentence = random_line

    label_eng.configure(text=eng)
    label_pl.configure(text=pl)
    label_sentence.configure(text=sentence)





    vocabulary_review_page.mainloop()






if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_review(main_page)