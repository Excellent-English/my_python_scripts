import io
import time

import customtkinter as ctk
from gtts import gTTS
from openpyxl.styles.builtins import comma
import threading
import pygame

from C2_English_App.AllClasses.App_Label_Standard import App_Label_Standard
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Frame import AppFrame
from C2_English_App.AllClasses.Button_Standard import Button_Standard
from C2_English_App.AllClasses.App_Database import Database


def run_vocabulary_review(menu_page):
    menu_page.withdraw()
    vocabulary_review_page = AppWindow(banner_text = "Review your dictionary")


# ---------------------------------------------------------------------------------------
# funkcje i opcje używane podczas pracy z aplikacją: odsłuchiwanie słowa, zmiana słowa
# ---------------------------------------------------------------------------------------


    def go_back_to_menu():
        vocabulary_review_page.destroy()
        menu_page.deiconify()

    vocabulary_review_page.return_button.configure(command=go_back_to_menu)
    vocabulary_review_page.bind("<Escape>", lambda event: go_back_to_menu())


# Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    vocabulary_review_page.bind('<Return>', lambda event: change_word())
# ustawienie jedynki (zarówno u góry jak i z klawiatury numerycznej) na odsłuchanie zdania angielskiego
    vocabulary_review_page.bind('1', lambda event: hear_eng_sentence())
    vocabulary_review_page.bind('<KP_1>', lambda event: hear_eng_sentence())


    # funkcja do odtwarzania dźwięku
    def read_word(word):
        if not word:
            print("Brak tekstu do przetworzenia")
            return
        tts = gTTS(text=word, lang='en')
        fp = io.BytesIO()
        tts.write_to_fp(fp)
        fp.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(fp)
        pygame.mixer.music.play()

        # Czeka, aż dźwięk się odtworzy
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)


# zmiana zestawu widocznego na ekranie
    def change_word():
        my_database = Database("../Databases/database_1.db")
        random_line = my_database.get_random_element_1()
        eng, pl, sentence = random_line

        label_eng.configure(text=eng)
        label_pl.configure(text=pl)
        label_sentence.configure(text=sentence)

        threading.Thread(target=read_word, args=(eng,)).start()


# funkcja do odtwarzania angielskiego zdania
    def hear_eng_sentence():
        current_sentence = label_sentence.cget("text")
        threading.Thread(target=read_word, args=(current_sentence,)).start()

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

# 4 labele z tekstami: opis okna, znak równości, Enter, jedynka do odsłuchania zdania
    label_description = App_Label_Standard(vocabulary_review_page, font = ("Open Sans", 16) , wraplength = 700, width=700, justify="center", anchor="center", text="You have a possibility to review the words added to your dictionary.\nUse >> button to move on to the next word (or press Enter).\nGood luck!")
    label_description.place(x=90, y=110)
    label_equal = App_Label_Standard(vocabulary_review_page, text="=")
    label_equal.place(x=425, y=230)
    label_enter = App_Label_Standard(vocabulary_review_page, font = ("Open Sans", 12), text="press Enter")
    label_enter.place(x=400, y=442)
    label_press_1 = App_Label_Standard(vocabulary_review_page, font = ("Open Sans", 12), text="press 1")
    label_press_1.place(x=806, y=355)

# 1 button odświeżający słowa/zdania widoczne na ekranie
    button_next = Button_Standard(vocabulary_review_page, width= 100, height= 40, text = ">>", command=change_word)
    button_next.place(x=387, y=400)

# 1 button odsłuchujący angielskie zdania
    button_replay = Button_Standard(vocabulary_review_page, width=70, height=40, text="♫", command=hear_eng_sentence)
    button_replay.place(x=800, y=315)


# ---------------------------------------------------------------------------------------
# ustawienie pierwszego zestawu danych
# ---------------------------------------------------------------------------------------

# wywołanie randomowego rekordu z database_1 i automatyczne uruchomienie odtwarzania słówka angielskiego
    my_database = Database("../Databases/database_1.db")
    random_line = my_database.get_random_element_1()
    eng, pl, sentence = random_line

    label_eng.configure(text=eng)
    label_pl.configure(text=pl)
    label_sentence.configure(text=sentence)

    threading.Thread(target=read_word, args=(eng,)).start()

# otwarcie okna aplikacji
    vocabulary_review_page.mainloop()




if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_review(main_page)