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

# Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji change_word() lub check_answer()
    def on_enter(event=None):
        is_enabled = str(entry_box_eng.cget("state")) == "normal"
        if is_enabled:
            check_answer()
        else:
            change_word()

    # Powiązanie z oknem (obsłuży Enter z głównej klawiatury i z klawiatury numerycznej)
    vocabulary_listen_page.bind("<Return>", on_enter)
    vocabulary_listen_page.bind("<KP_Enter>", on_enter)


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

        label_enter_right.configure(text_color= "#808080")
        label_enter_left.configure(text_color= "white")

        button_replay.configure(state = "normal")
        button_next.configure(state="normal")
        button_check.configure(state="normal")
        button_show_answer.configure(state="normal")
        entry_box_eng.configure(state="normal")
        button_start.configure(state="disabled")

        my_database = Database("../Databases/database_1.db")
        random_line = my_database.get_random_element_1()
        eng, pl, sentence = random_line

        label_eng.configure(text=eng)
        label_pl.configure(text=pl)

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
            label_eng.configure(fg_color="#A8E6A3", text_color= "#808080")
            frame_pl.configure(fg_color="#A8E6A3")
            label_pl.configure(fg_color="#A8E6A3", text_color= "#808080")

            threading.Thread(target=read_word, args=(current_word,)).start()

            frame_eng.after(3000, lambda: (
                frame_eng.configure(fg_color="white"),
                label_eng.configure(fg_color="transparent", text_color= "white"),
                frame_pl.configure(fg_color="white"),
                label_pl.configure(fg_color="transparent", text_color= "white"),

                entry_box_eng.delete(0, "end"),
                change_word()
            ))
        else:
            frame_eng.configure(fg_color="#F8D7DA")
            label_eng.configure(fg_color="#F8D7DA", text_color= "#808080")
            frame_pl.configure(fg_color="#F8D7DA")
            label_pl.configure(fg_color="#F8D7DA", text_color= "#808080")

            threading.Thread(target=read_word, args=(current_word,)).start()

            frame_eng.after(3000, lambda: (
                frame_eng.configure(fg_color="white"),
                label_eng.configure(fg_color="transparent", text_color= "white"),
                frame_pl.configure(fg_color="white"),
                label_pl.configure(fg_color="transparent", text_color= "white"),
                entry_box_eng.delete(0, "end")
            ))


# funkcja pokazująca prawidłowe rozwiązanie i losująca nowy zestaw
    def show_answer():
        current_word = label_eng.cget("text")

        frame_eng.configure(fg_color="#F8D7DA")
        label_eng.configure(fg_color="#F8D7DA", text_color= "#808080")
        frame_pl.configure(fg_color="#F8D7DA")
        label_pl.configure(fg_color="#F8D7DA", text_color= "#808080")

        threading.Thread(target=read_word, args=(current_word,)).start()

        frame_eng.after(5000, lambda: (
            frame_eng.configure(fg_color="white"),
            label_eng.configure(fg_color="transparent", text_color= "white"),
            frame_pl.configure(fg_color="white"),
            label_pl.configure(fg_color="transparent", text_color= "white"),
            entry_box_eng.delete(0, "end"),
            change_word(),
            threading.Thread(target=read_word, args=(current_word,)).start()
        ))



# ---------------------------------------------------------------------------------------
# elementy widoczne w tym oknie
# ---------------------------------------------------------------------------------------

# 3 frame'y dla tekstów widocznych w oknie aplikacji
    frame_eng = AppFrame(vocabulary_listen_page)
    frame_eng.place(x=60, y=320)
    frame_pl = AppFrame(vocabulary_listen_page)
    frame_pl.place(x=470, y=320)

# 3 labele z tekstami: eng, pl, sentence
    label_eng = App_Label_Standard(frame_eng, justify="center", anchor="center", text="", text_color= "white")
    label_eng.place(relx=0.5, rely=0.5, anchor="center")
    label_pl = App_Label_Standard(frame_pl, justify="center", anchor="center", text="", text_color= "white")
    label_pl.place(relx=0.5, rely=0.5, anchor="center")

# labele z tekstami: opis okna, znak równości, Enter, jedynka do odsłuchania zdania
    label_description = App_Label_Standard(vocabulary_listen_page, font=("Open Sans", 20), wraplength=700, width=700,
                                           justify="center", anchor="center",
                                           text="What did you hear?")
    label_description.place(x=85, y=180)
    label_equal = App_Label_Standard(vocabulary_listen_page, text="=")
    label_equal.place(x=425, y=350)
    label_enter_right = App_Label_Standard(vocabulary_listen_page, text_color = "white", font=("Open Sans", 12), text="press Enter")
    label_enter_right.place(x=608, y=270)
    label_enter_left = App_Label_Standard(vocabulary_listen_page, font=("Open Sans", 12), text="press Enter")
    label_enter_left.place(x=100, y=250)

# 1 button odświeżający słowa/zdania widoczne na ekranie
    button_next = Button_Standard(vocabulary_listen_page, state = "disabled", width=100, height=40, text=">>", command=change_word)
    button_next.place(x=430, y=110)

# 1 button odsłuchujący angielskie zdania
    button_replay = Button_Standard(vocabulary_listen_page, state = "disabled", width=70, height=40, text="♫", command=hear_eng_sentence)
    button_replay.place(x=350, y=110)

# 1 button Start
    button_start = Button_Standard(vocabulary_listen_page, width=150, height=120, text="START", command=change_word)
    button_start.place(x=60, y=130)

# 2 buttony: Check i Show answer
    button_check = Button_Standard(vocabulary_listen_page, state = "disabled", font = ("Open Sans", 16), width=100, height=40, text="Check", command=check_answer)
    button_check.place(x=595, y=230)
    button_show_answer = Button_Standard(vocabulary_listen_page, state = "disabled", font = ("Open Sans", 16), width=100, height=40, text="Show answer", command=show_answer)
    button_show_answer.place(x=705, y=230)

# 1 entry box do wpisywania angielskiego słówka
    entry_box_eng = App_Entry_Box(vocabulary_listen_page, state= "disabled")
    entry_box_eng.place(x=275, y=230)
    vocabulary_listen_page.after(100, entry_box_eng.focus_set)




    vocabulary_listen_page.mainloop()


if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_vocabulary_listen(main_page)