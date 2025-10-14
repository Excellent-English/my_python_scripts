import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
import random
import os
from tkinter import messagebox

# region Podstawowa kontrola słownika i lokalizacji
# Pobierz ścieżkę do katalogu Dokumenty użytkownika
desktop_path = os.path.join(os.path.expanduser('~'), 'Downloads')
file_path = os.path.join(desktop_path, 'Słownik.txt')

# Utwórz plik, jeśli nie istnieje
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as plik:
        pass  # Utwórz pusty plik
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

# region Funkcje do otwierania nowych okien i ukrywania głównego okna
def przegladaj(bg_color):
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Przeglądaj Twoje słówka")
    new_window.geometry("600x400")
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

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
        else:
            label_left.configure(text="Brak słówek")
            label_right.configure(text="Wróć do głównego menu, wybierz opcję Dodaj, aby stworzyć nowy słownik.", wraplength=200)

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 2)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz lewą ramkę
    left_frame = ctk.CTkFrame(new_window, height=80, width=200)
    left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    left_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz prawą ramkę
    right_frame = ctk.CTkFrame(new_window, height=80, width=200)
    right_frame.grid(row=1, column=1, padx=10, pady=5, sticky="nsew")
    right_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


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
    label_left.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

    label_right = ctk.CTkLabel(right_frame, text="", font=("Helvetica", 14), anchor="center", wraplength=220)
    label_right.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")



    # Dodawanie przycisku ">>"
    new_button = ctk.CTkButton(new_window, text=">>", font=("Helvetica", 14),text_color="white", command=update_labels)
    new_button.grid(row=2, column=0, pady=10)

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=2, column=1, pady=10)

    # Pierwsze wywołanie funkcji aktualizującej etykiety
    update_labels()

def dodaj(bg_color):
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Dodaj słówko do listy")
    new_window.geometry("600x400")
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Funkcja do zapisywania rekordu do pliku
    def save_record():
        klucz = entry_key.get()
        wartosc = entry_value.get()
        if not klucz or not wartosc:
            messagebox.showwarning("Brakujące dane", "Uzupełnij wszystkie pola, aby dodać nowe słówko do słownika.")
        else:
            with open(file_path, 'a', encoding='utf-8') as plik:
                plik.write(f"{klucz}:{wartosc}\n")
            entry_key.delete(0, "end")
            entry_value.delete(0, "end")
            messagebox.showinfo("Sukces", "Rekord został pomyślnie dodany do słownika.")


    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 4)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po lewej stronie oraz jego polskie tłumaczenie po prawej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    label_key = ctk.CTkLabel(master=new_window, text="Polskie tłumaczenie:")
    label_key.grid(row=1, column=0, pady=5, sticky="e")

    entry_key = ctk.CTkEntry(master=new_window)
    entry_key.grid(row=1, column=1, padx=5, pady=5, sticky="we")

    label_value = ctk.CTkLabel(master=new_window, text="Angielskie słówko:")
    label_value.grid(row=1, column=2, pady=5, sticky="e")

    entry_value = ctk.CTkEntry(master=new_window)
    entry_value.grid(row=1, column=3, padx=5, pady=5, sticky="we")

    save_button = ctk.CTkButton(master=new_window, text="Zapisz rekord", font=("Helvetica", 14), text_color="white", command=save_record)
    save_button.grid(row=2, column=0, columnspan=4, pady=10)

    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=3, column=0, columnspan=4, pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def uczsie(bg_color):
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Ucz się")
    new_window.geometry("600x400")
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

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
    ctk.CTkLabel(new_window, text='Ile słówek chcesz pobrać do dzisiejszej sesji? Wpisz konkretną liczbę i kliknij przycisk "Rozpocznij naukę"',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


    # Tworzenie pola do wpisywania tekstu
    entry3 = ctk.CTkEntry(new_window, font=("Helvetica", 14), width=100, justify='center')
    entry3.grid(row=3, column=0, padx=10, pady=10)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


    # Dodawanie przycisku "Rozpocznij naukę", zamknięcie starego okna i uruchomienie trybu nauki z zapamiętaną liczbą słówek pod zmienną global number
    def combined_function():
        save_number(entry3)
        new_window.destroy()  # Zamknięcie starego okna
        button_window4("white")

    wykonaj_button = ctk.CTkButton(new_window, text="Rozpocznij naukę", font=("Helvetica", 14), width=150, text_color="white", command=lambda: combined_function())
    wykonaj_button.grid(row=4, column=0, padx=10, pady=10)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru


    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), width=150, text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=5, column=0, padx=10, pady=10)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def button_window4(bg_color):
    root.withdraw()
    new_window = ctk.CTkToplevel(root)
    new_window.title("Ucz się")
    new_window.geometry("600x400")
    new_window.focus_force()  # Ustawienie fokusu na nowe okno


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

    # Utwórz górną ramkę
    upper_frame = ctk.CTkFrame(new_window, height=90, width=480)
    upper_frame.grid(row=0, column=0, padx=60, pady=20, sticky="nsew", columnspan = 2)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Utwórz pole tekstowe i dodaj je do wewnętrznej ramki (inner_frame)
    ctk.CTkLabel(upper_frame,
                         text='W tym oknie będziesz w stanie sprawdzić swoją wiedzę. Na początku wpisz liczbę słówek do powtórki i po użyciu przycisku "Rozpocznij naukę" zostaniesz przeniesiony do nowego okna, w którym rozpocznie się sesja treningowa. Powodzenia!',
                         wraplength=450, font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


    # Utwórz 2 ramki, który zawierać będą informacj na temat liczby pozostałych słówek do nauki
    dict_length = len(nowy_slownik_do_nauki)
    print(dict_length)

    mid_left_frame = ctk.CTkFrame(new_window, height=30, width=200)
    mid_left_frame.grid(row=1, column=0, padx=10, pady=5, sticky="nsew")
    mid_left_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    ctk.CTkLabel(mid_left_frame,
                         text=f'Pozostała liczba słówek do nauki: {dict_length}',
                         font=("Helvetica", 14), anchor="center").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Konfiguracja siatki dla mid_left_frame
    mid_left_frame.grid_rowconfigure(0, weight=1)
    mid_left_frame.grid_columnconfigure(0, weight=1)

    # Utwórz lewą ramkę
    lower_left_frame = ctk.CTkFrame(new_window, height=60, width=200)
    lower_left_frame.grid(row=2, column=0, padx=10, pady=5, sticky="nsew")
    lower_left_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Dodaj kolumny i wiersze do ramki
    lower_left_frame.grid_columnconfigure(0, weight=1)
    lower_left_frame.grid_rowconfigure(0, weight=1)
    lower_left_frame.grid_rowconfigure(1, weight=1)
    lower_left_frame.grid_rowconfigure(2, weight=1)

    # Utwórz pole tekstowe i dodaj je do ramki
    random_key = random.choice(list(nowy_slownik_do_nauki.keys()))
    random_value = nowy_slownik_do_nauki[random_key]
    print(random_value)
    ctk.CTkLabel(lower_left_frame,
                         text=random_key,
                         wraplength=250, font=("Helvetica", 14), anchor="center").grid(row=2, column=0, padx=10, pady=10, sticky="n")

    # Utwórz prawą ramkę
    lower_right_frame = ctk.CTkFrame(new_window, height=80, width=200)
    lower_right_frame.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")
    lower_right_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    # Dodaj kolumny i wiersze do ramki
    lower_right_frame.grid_columnconfigure(0, weight=1)
    lower_right_frame.grid_rowconfigure(1, weight=1)

    entry_value = ctk.CTkEntry(master=lower_right_frame, width=150)
    entry_value.grid(row=1, column=0, padx=5, pady=5, sticky="we")

    # Dodawanie przycisku "Sprawdź >>"
    verify_button = ctk.CTkButton(new_window, text="Sprawdź >>", font=("Helvetica", 14), width=150, text_color="white")
    verify_button.grid(row=5, column=1, pady=5)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru




    # Tworzenie funkcji z pętlą, która sprawdzi entry_value i porówna go do value przypisanego do key, który losowo został wyświetlony w lower_left_frame





    # Dodawanie przycisku "Powrót do menu"
    back_button = ctk.CTkButton(new_window, text="Powrót do menu", font=("Helvetica", 14), width=150, text_color="white",
                                command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.grid(row=7, column=0, pady=30)
    upper_frame.grid_propagate(False)  # Wyłączenie automatycznego dostosowywania rozmiaru

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))
# endregion

# region Utwórz główne okno
root = ctk.CTk()
root.title("Wszystko dzięki Easy English!")
root.geometry("600x400")  # Ustawienie rozmiaru okna na 600x400 pikseli

# Przechwycenie zdarzenia zamknięcia okna
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Tworzenie menu
menu = tk.Menu(root)
root.config(menu=menu)

# Dodanie menu "Plik"
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Przeglądaj", command=lambda: przegladaj("white"))
file_menu.add_command(label="Dodaj", command=lambda: dodaj("white"))
file_menu.add_command(label="Ucz się", command=lambda: uczsie("white"))
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=confirm_exit)

# Dodanie menu "Pomoc"
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Pomoc", menu=help_menu)
help_menu.add_command(label="O programie")
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
                     text="Witaj w moim świecie języka angielskiego. Ta aplikacja przygotowana jest dla wszystkich osób, które chciałyby nauczyć się komunikować w tym języku. Spróbuj i przekonaj się, jakie to proste!\nDo dyspozycji masz 3 tryby, z których możesz korzystać: przeglądanie słownika, dodawanie słów do słownika oraz tryb nauki. Powodzenia!",
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
button1 = ctk.CTkButton(frame, text="Przeglądaj", height=50, text_color="white", command=lambda: przegladaj("white"))
button1.grid(row=1, column=0, padx=5, pady=10, sticky="nsew")

button2 = ctk.CTkButton(frame, text="Dodaj", height=50, text_color="white", command=lambda: dodaj("white"))
button2.grid(row=1, column=1, padx=5, pady=10, sticky="nsew")

button3 = ctk.CTkButton(frame, text="Ucz się", height=50, text_color="white", command=lambda: uczsie("white"))
button3.grid(row=1, column=2, padx=5, pady=10, sticky="nsew")

button4 = ctk.CTkButton(frame, text="---", height=50, fg_color="#D3D3D3")
button4.grid(row=1, column=3, padx=5, pady=10, sticky="nsew")

button5 = ctk.CTkButton(frame, text="---", height=50, fg_color="#D3D3D3")
button5.grid(row=2, column=0, padx=5, pady=10, sticky="nsew")

button6 = ctk.CTkButton(frame, text="---", height=50, fg_color="#D3D3D3")
button6.grid(row=2, column=1, padx=5, pady=10, sticky="nsew")

button7 = ctk.CTkButton(frame, text="---", height=50, fg_color="#D3D3D3")
button7.grid(row=2, column=2, padx=5, pady=10, sticky="nsew")

button8 = ctk.CTkButton(frame, text="Zakończ", height=50,text_color="white", command=confirm_exit)
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