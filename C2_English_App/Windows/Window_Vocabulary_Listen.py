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
from C2_English_App.AllClasses.App_Entry_Box import App_Entry_Box


def run_vocabulary_listen(menu_page):
    menu_page.withdraw()
    vocabulary_listen_page = AppWindow(banner_text = "Listen and write what you heard")

# ---------------------------------------------------------------------------------------
# funkcje i opcje używane podczas pracy z aplikacją: odsłuchiwanie słowa, zmiana słowa
# ---------------------------------------------------------------------------------------

# Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    # vocabulary_listen_page.bind('<Return>', lambda event: change_word())
# ustawienie jedynki (zarówno u góry jak i z klawiatury numerycznej) na odsłuchanie zdania angielskiego
    vocabulary_listen_page.bind('1', lambda event: hear_eng_sentence())
    vocabulary_listen_page.bind('<KP_1>', lambda event: hear_eng_sentence())

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
        current_word = label_eng.cget("text")
        threading.Thread(target=read_word, args=(current_word,)).start()


# funkcja do przycisku "Check", czyli sprawdzania poprawności odpowiedzi
    def check_answer():
        current_word = label_eng.cget("text")
        if entry_box_eng.get_text() == current_word:
            frame_eng.configure(fg_color="#A8E6A3")
            label_eng.configure(fg_color="#A8E6A3")
            frame_eng.after(2000, lambda: (frame_eng.configure(fg_color="white"), label_eng.configure(fg_color="transparent")))
        else:
            frame_eng.configure(fg_color="#F8D7DA")
            label_eng.configure(fg_color="#F8D7DA")
            frame_eng.after(2000, lambda: (frame_eng.configure(fg_color="white"), label_eng.configure(fg_color="transparent")))


# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie- 3 framy, 6 labeli i 1 button
# ---------------------------------------------------------------------------------------

# 3 frame'y dla tekstów widocznych w oknie aplikacji
    frame_eng = AppFrame(vocabulary_listen_page)
    frame_eng.place(x=60, y=320)
    frame_pl = AppFrame(vocabulary_listen_page)
    frame_pl.place(x=470, y=320)
    frame_sentence = AppFrame(vocabulary_listen_page, width=690, height=70)
    frame_sentence.place(x=100, y=420)

# 3 labele z tekstami: eng, pl, sentence
    label_eng = App_Label_Standard(frame_eng, justify="center", anchor="center", text="")
    label_eng.place(relx=0.5, rely=0.5, anchor="center")
    label_pl = App_Label_Standard(frame_pl, justify="center", anchor="center", text="")
    label_pl.place(relx=0.5, rely=0.5, anchor="center")
    label_sentence = App_Label_Standard(frame_sentence, wraplength=690, justify="center", anchor="center", text="")
    label_sentence.place(relx=0.5, rely=0.5, anchor="center")

# 4 labele z tekstami: opis okna, znak równości, Enter, jedynka do odsłuchania zdania
    label_description = App_Label_Standard(vocabulary_listen_page, font=("Open Sans", 20), wraplength=700, width=700,
                                           justify="center", anchor="center",
                                           text="What did you hear?")
    label_description.place(x=85, y=180)
    label_equal = App_Label_Standard(vocabulary_listen_page, text="=")
    label_equal.place(x=425, y=350)
    label_enter = App_Label_Standard(vocabulary_listen_page, font=("Open Sans", 12), text="press Enter")
    label_enter.place(x=610, y=270)
    label_press_1 = App_Label_Standard(vocabulary_listen_page, font=("Open Sans", 12), text="press 1")
    label_press_1.place(x=733, y=270)

# 1 button odświeżający słowa/zdania widoczne na ekranie
    button_next = Button_Standard(vocabulary_listen_page, width=100, height=40, text=">>", command=change_word)
    button_next.place(x=430, y=110)

# 1 button odsłuchujący angielskie zdania
    button_replay = Button_Standard(vocabulary_listen_page, width=70, height=40, text="♫", command=hear_eng_sentence)
    button_replay.place(x=350, y=110)

# 1 button Start
    button_next = Button_Standard(vocabulary_listen_page, width=150, height=120, text="START", command=change_word)
    button_next.place(x=60, y=130)

# 2 buttony: Check i Show answer
    button_check = Button_Standard(vocabulary_listen_page, font = ("Open Sans", 16), width=100, height=40, text="Check", command=check_answer)
    button_check.place(x=595, y=230)
    button_show_answer = Button_Standard(vocabulary_listen_page, font = ("Open Sans", 16), width=100, height=40, text="Show answer", command=change_word)
    button_show_answer.place(x=705, y=230)

# 1 entry box do wpisywania angielskiego słówka
    entry_box_eng = App_Entry_Box(vocabulary_listen_page)
    entry_box_eng.place(x=275, y=230)
    vocabulary_listen_page.after(100, entry_box_eng.focus_set)



# ---------------------------------------------------------------------------------------
# ustawienie pierwszego zestawu danych
# ---------------------------------------------------------------------------------------

# wywołanie randomowego rekordu z database_1 i automatyczne uruchomienie odtwarzania słówka angielskiego
#     my_database = Database("../Databases/database_1.db")
#     random_line = my_database.get_random_element_1()
#     eng, pl, sentence = random_line
#
#     label_eng.configure(text=eng)
#     label_pl.configure(text=pl)
#     label_sentence.configure(text=sentence)
#
#     threading.Thread(target=read_word, args=(eng,)).start()



    vocabulary_listen_page.mainloop()


if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_listen(main_page)