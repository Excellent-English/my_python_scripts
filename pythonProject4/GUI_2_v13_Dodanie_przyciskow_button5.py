import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
import random
import os
from tkinter import messagebox
from gtts import gTTS
import io
import pygame
import time
import threading

# region Podstawowa kontrola słownika i lokalizacji
# Pobierz ścieżkę do katalogu Dokumenty użytkownika
desktop_path = os.path.join(os.path.expanduser('~'), 'Downloads')
file_path = os.path.join(desktop_path, 'Słownik.txt')

# Utwórz plik, jeśli nie istnieje
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as plik:
        pass  # Utwórz pusty plik

# Zmienne globalne
random_key = None
random_value = None

# endregion

# region Funkcja do zapamiętywania liczby słówek, które mają być dostarczone użytkownikowi w trakcie pojedynczej sesji
def save_number(entry3):
    global number
    try:
        number = int(entry3.get())  # Konwersja na int
        print(f"Wpisana liczba: {number}")
    except ValueError:
        print("Proszę wpisać poprawną liczbę.")
# endregion

# region Funkcja potwierdzająca zamknięcie aplikacji
def confirm_exit():
    msg = CTkMessagebox(title="Zakończ", message="Czy na pewno chcesz zamknąć aplikację?", icon="question", option_1="Nie", option_2="Tak")
    if msg.get() == "Tak":
        root.quit()
# endregion

# region Funkcja do odtwarzania dźwięku
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
# endregion

# region Funkcje do otwierania nowych okien i ukrywania głównego okna
def przegladaj():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Przeglądaj Twoje słówka")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    new_window.bind('<Return>', lambda event: update_labels())

    # Utwórz pusty słownik
    slownik = {}

    # Otwórz plik txt do odczytu
    try:
        with open(file_path, 'r', encoding='utf-8') as plik:
            for linia in plik:
                # Usuń białe znaki z początku i końca linii oraz podziel na klucz i wartość
                klucz, wartosc = linia.strip().split(':')
                # Przypisz wartości do słownika, konwertując wartości numeryczne
                slownik[klucz] = int(wartosc) if wartosc.isdigit() else wartosc
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Plik Słownik.txt nie istnieje. Dodaj słówka, aby utworzyć plik.")

    # Funkcja aktualizująca etykiety
    def update_labels():
        if slownik:
            losowy_klucz = random.choice(list(slownik.keys()))
            losowa_wartosc = slownik[losowy_klucz]
            label_left.configure(text=losowy_klucz)
            label_right.configure(text=losowa_wartosc)
            word = losowa_wartosc
            threading.Thread(target=read_word, args=(word,)).start()
        else:
            label_left.configure(text="Brak słówek")
            label_right.configure(text="Wróć do głównego menu, wybierz opcję Dodaj, aby stworzyć nowy słownik.", wraplength=200)


    # Ustawienie przycisków --------------------------------------------------------------------------------------------------------------------------------------------------
    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 2)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # test
    upper_frame.grid_rowconfigure(0, weight=1)
    upper_frame.grid_columnconfigure(0, weight=1)

    # Utwórz lewą ramkę
    left_frame = ctk.CTkFrame(new_window, height=80, width=200)
    left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    left_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # test
    left_frame.grid_rowconfigure(0, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    # Utwórz prawą ramkę
    right_frame = ctk.CTkFrame(new_window, height=80, width=200)
    right_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
    right_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # test
    right_frame.grid_rowconfigure(0, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)


    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość przeglądania słówek dodanych do Twojego słownika. W celu sprawdzenia kolejnego słówka, naciskaj klawisz >>. Aby powrócić do głównego menu, użyj przycisku na dole. Miłej nauki!",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki
    ctk.CTkLabel(upper_frame,
                 text="W tym oknie masz możliwość przeglądania słówek dodanych do Twojego słownika. W celu sprawdzenia kolejnego słówka, naciskaj klawisz >>. Aby powrócić do głównego menu, użyj przycisku na dole. Miłej nauki!",
                 wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10,
                                                                               sticky="nsew")

    # Dodawanie etykiet z losowym kluczem i wartością
    label_left = ctk.CTkLabel(left_frame, text="", font=("Helvetica", 14), anchor="center", wraplength=220)
    label_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    label_right = ctk.CTkLabel(right_frame, text="", font=("Helvetica", 14), anchor="center", wraplength=220)
    label_right.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")



    # Dodawanie przycisku ">>"
    new_button = ctk.CTkButton(new_window, text=">>", font=("Helvetica", 14),text_color="white", command=update_labels)
    new_button.grid(row=2, column=0, pady=10)

    # Utwórz pole tekstowe pod przyciskiem ">>"
    ctk.CTkLabel(new_window,
                 text="(Enter)",
                 wraplength=450, font=("Helvetica", 12, "italic"), anchor="center").grid(row=3, column=0,
                                                                               sticky="nsew")

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=2, column=1, pady=10)

    # Pierwsze wywołanie funkcji aktualizującej etykiety
    update_labels()

def dodaj():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Dodaj słówko do listy")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    new_window.bind('<Return>', lambda event: save_record())

    # Funkcja do zapisywania rekordu do pliku
    def save_record():
        klucz = entry_key.get()
        wartosc = entry_value.get()
        if not klucz or not wartosc:
            CTkMessagebox(title="Brakujące dane", message="Uzupełnij wszystkie pola, aby dodać nowe słówko do słownika.", icon="cancel")
        else:
            with open(file_path, 'a', encoding='utf-8') as plik:
                plik.write(f"{klucz}:{wartosc}\n")
            entry_key.delete(0, "end")
            entry_value.delete(0, "end")
            CTkMessagebox(title="Sukces",
                          message="Rekord został pomyślnie dodany do słownika.", icon="check")


    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po prawej stronie oraz jego polskie tłumaczenie po lewej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    label_key = ctk.CTkLabel(master=new_window, text="Polskie tłumaczenie:")
    label_key.grid(row=1, column=0, pady=5, sticky="e")

    entry_key = ctk.CTkEntry(master=new_window)
    entry_key.grid(row=1, column=1, padx=5, pady=5, sticky="we")
    new_window.after(100, lambda: entry_key.focus_force())

    label_value = ctk.CTkLabel(master=new_window, text="Angielskie słówko:")
    label_value.grid(row=1, column=2, pady=5, sticky="e")

    entry_value = ctk.CTkEntry(master=new_window)
    entry_value.grid(row=1, column=3, padx=5, pady=5, sticky="we")

    save_button = ctk.CTkButton(master=new_window, text="Zapisz rekord (enter)", font=("Helvetica", 13), text_color="white", command=save_record)
    save_button.grid(row=2, column=0, columnspan=4, pady=10)

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 13), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=3, column=0, columnspan=4, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def uczsie():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Ucz się")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    new_window.bind('<Return>', lambda event: combined_function())

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew")
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text='W tym oknie będziesz w stanie sprawdzić swoją wiedzę. Na początku wpisz liczbę słówek do powtórki i po użyciu przycisku "Rozpocznij naukę" zostaniesz przeniesiony do nowego okna, w którym rozpocznie się sesja treningowa. Powodzenia!',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Ustawienie równomiernego rozkładu wierszy i kolumn w upper_frame
    upper_frame.grid_rowconfigure(0, weight=1)
    upper_frame.grid_columnconfigure(0, weight=1)

    # Utwórz pole tekstowe
    ctk.CTkLabel(new_window, text='Ile słówek chcesz pobrać do dzisiejszej sesji? Wpisz konkretną liczbę i kliknij przycisk "Rozpocznij naukę" lub użyj klawisza "Enter"',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


    # Tworzenie pola do wpisywania tekstu
    entry3 = ctk.CTkEntry(new_window, font=("Helvetica", 14), width=100, justify='center')
    entry3.grid(row=3, column=0, padx=10, pady=10)
    # Ustawienie pola entry3 jako aktywnego domyślnie
    new_window.after(100, lambda: entry3.focus_force())
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


    # Dodawanie przycisku "Rozpocznij naukę", zamknięcie starego okna i uruchomienie trybu nauki z zapamiętaną liczbą słówek pod zmienną global number
    def combined_function():
        save_number(entry3)
        new_window.destroy()  # Zamknięcie starego okna
        uczsie2()

    wykonaj_button = ctk.CTkButton(new_window, text="Rozpocznij naukę (enter)", font=("Helvetica", 14), width=150, text_color="white", command=lambda: combined_function())
    wykonaj_button.grid(row=4, column=0, padx=10, pady=10)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), width=150, text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=5, column=0, padx=10, pady=10)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def uczsie2():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Ucz się")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    new_window.bind('<Return>', lambda event: click_to_check())

    global random_key, random_value

    # Prace nad słownikiem --------------------------------------------------------------------------------------------------------------------------------------------------
    # Utwórz pusty słownik
    slownik_do_nauki = {}

    # Otwórz plik txt do odczytu
    try:
        with open(file_path, 'r', encoding='utf-8') as plik:
            for linia in plik:
                # Usuń białe znaki z początku i końca linii oraz podziel na klucz i wartość
                klucz_do_nauki, wartosc_do_nauki = linia.strip().split(':')
                # Przypisz wartości do słownika, konwertując wartości numeryczne
                slownik_do_nauki[klucz_do_nauki] = int(wartosc_do_nauki) if wartosc_do_nauki.isdigit() else wartosc_do_nauki
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Plik Słownik.txt nie istnieje. Dodaj słówka, aby utworzyć plik.")

    # Losowe pobranie x kluczy z oryginalnego słownika
    random_keys = random.sample(list(slownik_do_nauki.keys()), number)

    # Utworzenie nowego słownika z losowo wybranymi kluczami
    nowy_slownik_do_nauki = {key: slownik_do_nauki[key] for key in random_keys}

    print("Nowy słownik:", nowy_slownik_do_nauki)


    # Tworzenie ramek --------------------------------------------------------------------------------------------------------------------------------------------------
    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 2)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text='W tym oknie będziesz w stanie sprawdzić swoją wiedzę. Na początku wpisz liczbę słówek do powtórki i po użyciu przycisku "Rozpocznij naukę" zostaniesz przeniesiony do nowego okna, w którym rozpocznie się sesja treningowa. Powodzenia!',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


    # Utwórz 2 ramki, który zawierać będą informacje na temat liczby pozostałych słówek do nauki
    dict_length = len(nowy_slownik_do_nauki)
    print(dict_length)

    mid_left_frame = ctk.CTkFrame(new_window, height=50, width=200)
    mid_left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    mid_left_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    ctk.CTkLabel(mid_left_frame,
                         text=f'Pozostała liczba słówek do nauki: {dict_length}',
                         font=("Helvetica", 14), anchor="center").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
    # Skonfiguruj kolumny i wiersze, aby rozciągnąć widżet
    mid_left_frame.grid_columnconfigure(0, weight=1)
    mid_left_frame.grid_rowconfigure(1, weight=1)

    label_dla_random_key = ctk.CTkLabel(new_window,
                                        text="test",
                                        font=("Helvetica", 16),
                                        anchor="center",
                                        wraplength=200)
    label_dla_random_key.grid(row=3, column=0, padx=10, pady=10, sticky="nsew")

    # Skonfiguruj pole do wpisywania propozycji
    pole_do_wpisywania_propozycji = ctk.CTkEntry(master=new_window, width=150)
    pole_do_wpisywania_propozycji.grid(row=3, column=1, padx=5, pady=5, sticky="we")
    new_window.after(100, lambda: pole_do_wpisywania_propozycji.focus_force())


    # nadawanie wartości zmiennym random_key oraz random_value -------------------------------------------------------------------------------------------------------------
    # Wybierz losowy klucz
    random_key = random.choice(list(nowy_slownik_do_nauki.keys()))

    # Pobierz odpowiadającą wartość
    random_value = nowy_slownik_do_nauki[random_key]

    # Wydrukuj losowy klucz i odpowiadającą wartość
    print(f"Losowy klucz: {random_key}")
    print(f"Odpowiadająca wartość: {random_value}")
    label_dla_random_key.configure(text=random_key)


    # Tworzenie pętli do przeprowadzenia sesji szkoleniowej ----------------------------------------------------------------------------------------------------------------
    # Potwierdzanie zgodności tłumaczenia, usuwanie haseł ze słownika, wiadomość dla błędnego tłumaczenia ------------------------------------------------------------------

    def click_to_check():
        moja_odp = pole_do_wpisywania_propozycji.get()

        global random_key, random_value

        print(f"Moja odpowiedź: {moja_odp}")
        print(f"Random key: {random_key}")
        print(f"Random value: {random_value}")

        if moja_odp == random_value:
            del nowy_slownik_do_nauki[random_key]
            if len(nowy_slownik_do_nauki) > 0:  # Sprawdź, czy w słowniku jest jakakolwiek wartość
                CTkMessagebox(title="Sukces!", message=f"Udało Ci się!\n{random_key}\n{random_value}", icon="check")
                threading.Thread(target=read_word, args=(random_value,)).start()

            dict_length = len(nowy_slownik_do_nauki)
            print(dict_length)

            ctk.CTkLabel(mid_left_frame,
                         text=f'Pozostała liczba słówek do nauki: {dict_length}',
                         font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
            pole_do_wpisywania_propozycji.delete(0, 'end')  # Wyczyść pole Entry

            # del slownik_do_nauki[random_key]

            if len(nowy_slownik_do_nauki) > 0:
                random_key = random.choice(list(nowy_slownik_do_nauki.keys()))
                random_value = nowy_slownik_do_nauki[random_key]
                label_dla_random_key.configure(text=random_key)
            else:
                # Wyświetlenie komunikatu CTkMessagebox
                messagebox = CTkMessagebox(title="Sukces!",
                                               message="Brawo! Wykonałeś dobrą robotę! Trening możesz uznać za zakończony. Teraz przekierujemy Cię do okna, w którym możesz rozpocząć nową jednostkę treningową.",
                                               icon="check")
                messagebox.attributes('-topmost', True)  # Ustawienie okna wiadomości na wierzchu
                new_window.withdraw()  # Zamknij okno aplikacji
                # Opóźnienie wywołania funkcji uczsie
                root.after(100, uczsie)  # Opóźnienie o 2000 ms (2 sekundy)




        else:
            CTkMessagebox(title="Źle", message=f"Poprawny zestaw to:\n{random_key}\n{random_value}", icon="cancel")
            threading.Thread(target=read_word, args=(random_value,)).start()
            pole_do_wpisywania_propozycji.delete(0, 'end')  # Wyczyść pole Entry
            if len(nowy_slownik_do_nauki) > 0:
                random_key = random.choice(list(nowy_slownik_do_nauki.keys()))
                random_value = nowy_slownik_do_nauki[random_key]
                label_dla_random_key.configure(text=random_key)


    # Dodawanie przycisku "Sprawdź >>"
    verify_button = ctk.CTkButton(new_window, text="Sprawdź (enter)", font=("Helvetica", 14), width=150, text_color="white", command=click_to_check)
    verify_button.grid(row=5, column=1, pady=5)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), width=150, text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=7, column=0, pady=30)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def cwicz_wymowe():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Ćwicz wymowę")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po prawej stronie oraz jego polskie tłumaczenie po lewej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 13), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=3, column=0, columnspan=4, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def wpisuj_ze_sluchu():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Wpisywanie słów ze słuchu")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji click_to_check
    new_window.bind('<Return>', lambda event: click_to_check())

    global random_key, random_value

    # Prace nad słownikiem --------------------------------------------------------------------------------------------------------------------------------------------------
    # Utwórz pusty słownik
    slownik = {}

    # Otwórz plik txt do odczytu
    try:
        with open(file_path, 'r', encoding='utf-8') as plik:
            for linia in plik:
                # Usuń białe znaki z początku i końca linii oraz podziel na klucz i wartość
                klucz, wartosc = linia.strip().split(':')
                # Przypisz wartości do słownika, konwertując wartości numeryczne
                slownik[klucz] = int(wartosc) if wartosc.isdigit() else wartosc
    except FileNotFoundError:
        messagebox.showerror("Błąd", "Plik Słownik.txt nie istnieje. Dodaj słówka, aby utworzyć plik.")

    random_key = random.choice(list(slownik.keys()))
    random_value = slownik[random_key]

    print(random_key)
    print(random_value)

    word = random_value
    threading.Thread(target=read_word, args=(word,)).start()

    def nowe_slowko():
        global random_key, random_value
        random_key = random.choice(list(slownik.keys()))
        random_value = slownik[random_key]
        threading.Thread(target=read_word, args=(random_value,)).start()

    def click_to_check():
        global random_key, random_value
        print(random_key)
        print(random_value)

        moja_odp = entry_value.get()
        if moja_odp == random_value:
            CTkMessagebox(title="Sukces!", message=f"Udało Ci się!\n{random_key}\n{random_value}", icon="check")
            threading.Thread(target=read_word, args=(random_value,)).start()
            entry_value.delete(0, 'end')  # Wyczyść pole Entry
            random_key = random.choice(list(slownik.keys()))
            random_value = slownik[random_key]
            root.after(3000, lambda: threading.Thread(target=read_word, args=(random_value,)).start())

        else:
            CTkMessagebox(title="Źle", message=f"Poprawny zestaw to:\n{random_key}\n{random_value}", icon="cancel")
            threading.Thread(target=read_word, args=(random_value,)).start()
            entry_value.delete(0, 'end')  # Wyczyść pole Entry
            random_key = random.choice(list(slownik.keys()))
            random_value = slownik[random_key]


    def odtworz_slowko():
        global random_key, random_value
        threading.Thread(target=read_word, args=(random_value,)).start()







    # Tworzenie ramek i przycisków ------------------------------------------------------------------------------------------------------------------------------------
    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Skonfiguruj wiersze i kolumny w ramach upper_frame
    upper_frame.grid_rowconfigure(0, weight=1)
    upper_frame.grid_columnconfigure(0, weight=1)

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text='W tym oknie musisz wytężyć swój słuch i odgadnąć, jakie słowa wypowiada lektor. Pierwsze słówko zostało automatycznie wygenerowane, za to każde kolejne musisz przełączyć klikając na przycisk "Nowe słówko". Powodzenia!',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan = 4)

    # Dodawanie przycisku "Odtwórz"
    play_button = ctk.CTkButton(new_window, text="♫ Odtwórz ♫", font=("Helvetica", 13), text_color="white", command=odtworz_slowko)
    play_button.grid(row=2, column=1, pady=10)

    # Utwórz label z pytaniem co słyszysz oraz entry box na prawo od pytania
    label_key = ctk.CTkLabel(master=new_window, text="Co słyszysz?")
    label_key.grid(row=3, column=0, pady=5, sticky="e")

    entry_value = ctk.CTkEntry(master=new_window)
    entry_value.grid(row=3, column=1, padx=5, pady=5, sticky="we")
    new_window.after(500, lambda: entry_value.focus_force())

    # Dodawanie przycisku "Sprawdź (enter)"
    check_button = ctk.CTkButton(new_window, text="Sprawdź (enter)", font=("Helvetica", 13), text_color="white", command=click_to_check)
    check_button.grid(row=4, column=1, pady=10)

    # Dodawanie przycisku "Nowe słówko"
    new_button = ctk.CTkButton(new_window, text="⮌ Nowe słówko ⮌", font=("Helvetica", 13), text_color="white", command=nowe_slowko)
    new_button.grid(row=2, column=2, pady=10)

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 13), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=4, column=2, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def tlumacz_ze_sluchu():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Dobieranie tłumaczenia ze słuchu")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po prawej stronie oraz jego polskie tłumaczenie po lewej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 13), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=3, column=0, columnspan=4, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def dobieraj_obrazki():
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Obrazki - nauka ze słuchu")
    new_window.geometry('600x400+350+180')
    new_window.resizable(False, False)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po prawej stronie oraz jego polskie tłumaczenie po lewej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 13), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=3, column=0, columnspan=4, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

# endregion

# region Utwórz główne okno
root = ctk.CTk()
root.title("Wszystko dzięki Easy English!")
root.geometry('600x400+350+150')  # Ustawienie rozmiaru okna na 600x400 pikseli
root.resizable(False,False)

# Przechwycenie zdarzenia zamknięcia okna
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Tworzenie menu
menu = tk.Menu(root)
root.config(menu=menu)

# Dodanie menu "Ćwiczenia ogólne"
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Ćwiczenia ogólne", menu=file_menu)
file_menu.add_command(label="Przeglądaj", command=lambda: przegladaj())
file_menu.add_command(label="Dodaj lub zmień", command=lambda: dodaj())
file_menu.add_command(label="Ucz się", command=lambda: uczsie())
file_menu.add_command(label="Ćwicz wymowę", command=lambda: cwicz_wymowe())

# Dodanie menu "Ćwiczenia słuchowe"
file2_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Ćwiczenia słuchowe", menu=file2_menu)
file2_menu.add_command(label="Wpisuj ze słuchu", command=lambda: wpisuj_ze_sluchu())
file2_menu.add_command(label="Tłumacz ze słuchu", command=lambda: tlumacz_ze_sluchu())
file2_menu.add_command(label="Dobieraj obrazki", command=lambda: dobieraj_obrazki())

# Dodanie menu "Pomoc"
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Pomoc", menu=help_menu)
help_menu.add_command(label="O programie")
help_menu.add_separator()
help_menu.add_command(label="Zamknij", command=confirm_exit)
# endregion

# region Tworzenie ramki głównej i wewnętrznej po to, aby pole z tekstem znajdowało się na samym środku
# Utwórz główną ramkę
main_frame = ctk.CTkFrame(root)
main_frame.pack(expand=True, fill='both', padx=10, pady=10)

# Utwórz ramkę, aby umieścić pole z tekstem i przyciski
frame = ctk.CTkFrame(main_frame, height=200)
frame.pack(expand=True, fill='both', padx=10, pady=10)

# Utwórz wewnętrzną ramkę do wyśrodkowania tekstu
inner_frame = ctk.CTkFrame(frame)
inner_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Utwórz pole tekstowe i dodaj je do wewnętrznej ramki
label = ctk.CTkLabel(inner_frame,
                     text="Witaj w moim świecie języka angielskiego. Ta aplikacja przygotowana jest dla wszystkich osób, które chciałyby nauczyć się komunikować w tym języku. Spróbuj i przekonaj się, jakie to proste!\nDo dyspozycji masz aż 7 trybów nauki, z których możesz korzystać. Powodzenia!",
                     wraplength=400, font=("Helvetica", 14))
label.pack(expand=True)

# Ustawienie równomiernego rozkładu wierszy i kolumn
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
# endregion

# region Umieszczenie 8 przycisków w głównym oknie
# Utwórz ramkę, aby umieścić przyciski
frame = ctk.CTkFrame(root)
frame.pack(expand=True, fill='both', padx=20, pady=20)

# Utwórz 4 przyciski i dodaj je do ramki na przyciski
button1 = ctk.CTkButton(frame, text="Przeglądaj słówka", height=50, text_color="white", command=lambda: przegladaj())
button1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

button2 = ctk.CTkButton(frame, text="Dodaj lub zmień", height=50, text_color="white", command=lambda: dodaj())
button2.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

button3 = ctk.CTkButton(frame, text="Ucz się", height=50, text_color="white", command=lambda: uczsie())
button3.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

button4 = ctk.CTkButton(frame, text="Ćwicz wymowę", height=50, text_color="white", command=lambda: cwicz_wymowe())
button4.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

button5 = ctk.CTkButton(frame, text="Wpisuj ze słuchu", height=50, text_color="white", command=lambda: wpisuj_ze_sluchu())
button5.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

button6 = ctk.CTkButton(frame, text="Tłumacz ze słuchu", height=50, text_color="white", command=lambda: tlumacz_ze_sluchu())
button6.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

button7 = ctk.CTkButton(frame, text="Dobieraj obrazki", height=50, text_color="white", command=lambda: dobieraj_obrazki())
button7.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

button8 = ctk.CTkButton(frame, text="Zakończ", height=50, fg_color="#6B7280", text_color="white", command=confirm_exit)
button8.grid(row=2, column=3, padx=5, pady=10, sticky="nsew")

# Ustawienie równomiernego rozkładu kolumn
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)
frame.grid_columnconfigure(2, weight=1)
frame.grid_columnconfigure(3, weight=1)
# endregion

# region Uruchom aplikację
root.mainloop()
# endregion