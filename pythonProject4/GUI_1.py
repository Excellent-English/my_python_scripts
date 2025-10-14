import tkinter as tk
from tkinter import messagebox
import random
import os

# Pobierz ścieżkę do katalogu Dokumenty użytkownika
desktop_path = os.path.join(os.path.expanduser('~'), 'Downloads')
file_path = os.path.join(desktop_path, 'Słownik.txt')

# Utwórz plik, jeśli nie istnieje
if not os.path.exists(file_path):
    with open(file_path, 'w', encoding='utf-8') as plik:
        pass  # Utwórz pusty plik

# Funkcja do zamykania aplikacji z potwierdzeniem
def confirm_exit():
    answer = messagebox.askyesno("Zakończ", "Czy na pewno chcesz zamknąć aplikację?")
    if answer:
        root.quit()

# Funkcja do zapamiętywania liczby słówek, które mają być dostarczone użytkownikowi w trakcie pojedynczej sesji
def save_number(entry3):
    global number
    try:
        number = int(entry3.get())  # Konwersja na int
        print(f"Wpisana liczba: {number}")
    except ValueError:
        print("Proszę wpisać poprawną liczbę.")


# Funkcje do otwierania nowych okien i ukrywania głównego okna
def open_window1(bg_color):
    root.withdraw()
    new_window = tk.Toplevel(root)
    new_window.title("Przeglądaj słówka dodane do Twojej listy")
    new_window.geometry("600x400")
    new_window.configure(bg=bg_color)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    # Dodawanie pola tekstowego z wyjaśnieniem
    tk.Label(new_window,
             text="W tym oknie masz możliwość przeglądania słówek dodanych do Twojego słownika.\nW celu sprawdzenia kolejnego słówka, naciskaj klawisz >>.\nAby powrócić do głównego menu, użyj przycisku na dole. Miłej nauki!",
             font=("Helvetica", 14), wraplength=400, bg='white').pack(pady=10, padx=10)

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
            label_left.config(text=losowy_klucz)
            label_right.config(text=losowa_wartosc)
        else:
            label_left.config(text="Brak słówek")
            label_right.config(text="Wróć do głównego menu, wybierz opcję Dodaj, aby stworzyć nowy słownik.", wraplength=200)


    # Dodawanie etykiet z losowym kluczem i wartością
    frame = tk.Frame(new_window, bg=bg_color)
    frame.pack(pady=10)

    label_left = tk.Label(frame, text="", font=("Helvetica", 14), bg='white', wraplength=300)
    label_left.pack(side=tk.LEFT, padx=10)

    label_right = tk.Label(frame, text="", font=("Helvetica", 14), bg='white', wraplength=150)
    label_right.pack(side=tk.RIGHT, padx=10)

    # Pierwsze wywołanie funkcji aktualizującej etykiety
    update_labels()

    # Dodawanie przycisku ">>"
    new_button = tk.Button(new_window, text=">>", font=("Helvetica", 14), command=update_labels)
    new_button.pack(pady=10)


    # Dodawanie przycisku "Powrót do menu"
    back_button = tk.Button(new_window, text="Powrót do menu", font=("Helvetica", 14),
                            command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.pack(pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def open_window2(bg_color):
    root.withdraw()
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj słówko do listy")
    new_window.geometry("600x400")
    new_window.configure(bg=bg_color)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    tk.Label(new_window,
             text="W tym oknie masz możliwość dodawania nowych słówek do Twojego słownika. Jedyne, co musisz zrobić, to wpisać słowo angielskie po lewej stronie oraz jego polskie tłumaczenie po prawej. Na koniec wciśnij klawisz Dodaj, który przeniesie słówko do słownika.",
             font=("Helvetica", 16), wraplength=400).pack(pady=20)

    # Funkcja do zapisywania rekordu do pliku
    def save_record():
        klucz = entry_key.get()
        wartosc = entry_value.get()
        if klucz and wartosc:
            with open(file_path, 'a', encoding='utf-8') as plik:
                plik.write(f"{klucz}:{wartosc}\n")
            entry_key.delete(0, tk.END)
            entry_value.delete(0, tk.END)
            messagebox.showinfo("Sukces", "Rekord został pomyślnie dodany do słownika.")

    # Tworzenie i stylizacja widgetów
    frame = tk.Frame(master=new_window)
    frame.pack(pady=20, padx=20)

    label_key = tk.Label(master=frame, text="Polskie tłumaczenie:")
    label_key.grid(row=0, column=0, padx=10, pady=5)

    entry_key = tk.Entry(master=frame)
    entry_key.grid(row=0, column=1, padx=10, pady=5)

    label_value = tk.Label(master=frame, text="Angielskie słówko:")
    label_value.grid(row=0, column=2, padx=10, pady=5)

    entry_value = tk.Entry(master=frame)
    entry_value.grid(row=0, column=3, padx=10, pady=5)

    save_button = tk.Button(master=frame, text="Zapisz rekord", command=save_record)
    save_button.grid(row=1, column=0, columnspan=4, pady=20)

    # Dodawanie przycisku "Powrót do menu"
    back_button = tk.Button(new_window, text="Powrót do menu", font=("Helvetica", 14),
                            command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.pack(pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))

def open_window3(bg_color):
    root.withdraw()
    new_window = tk.Toplevel(root)
    new_window.title("Ucz się")
    new_window.geometry("600x400")
    new_window.configure(bg=bg_color)
    new_window.focus_force()  # Ustawienie fokusu na nowe okno

    tk.Label(new_window,
             text="W tym oknie będziesz w stanie sprawdzić swoją wiedzę.",
             font=("Helvetica", 16), wraplength=400).pack(pady=20)

    # Tworzenie etykiety tekstowej
    label = tk.Label(new_window, text='Ile słówek chcesz pobrać do dzisiejszej sesji? Wpisz konkretną liczbę i kliknij przycisk "Rozpocznij naukę"', font=("Helvetica", 14), wraplength=400)
    label.pack(pady=10)

    # Tworzenie pola do wpisywania tekstu
    entry3 = tk.Entry(new_window, font=("Helvetica", 14), width=5, justify='center')
    entry3.pack(pady=10)

    # Dodawanie przycisku "Rozpocznij naukę"
    wykonaj_button = tk.Button(new_window, text="Rozpocznij naukę", font=("Helvetica", 14), command=lambda: save_number(entry3))
    wykonaj_button.pack(pady=10)

    # Dodawanie przycisku "Powrót do menu" i ukrywanie go na początku
    back_button = tk.Button(new_window, text="Powrót do menu", font=("Helvetica", 14),
                            command=lambda: (new_window.destroy(), root.deiconify()))
    back_button.pack(pady=10)

    new_window.protocol("WM_DELETE_WINDOW", lambda: (new_window.destroy(), root.deiconify()))


# Tworzenie głównego okna
root = tk.Tk()
root.title("Wszystko dzięki Easy English!")
root.geometry("600x400")  # Ustawienie rozmiaru okna na 600x400 pikseli
bg_color = 'lightgrey'  # Ustawienie koloru tła
root.configure(bg=bg_color)

# Przechwycenie zdarzenia zamknięcia okna
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Tworzenie menu
menu = tk.Menu(root)
root.config(menu=menu)

# Dodanie menu "Plik"
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Plik", menu=file_menu)
file_menu.add_command(label="Nowy")
file_menu.add_command(label="Otwórz")
file_menu.add_command(label="Zapisz")
file_menu.add_separator()
file_menu.add_command(label="Zamknij", command=confirm_exit)

# Dodanie menu "Pomoc"
help_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="Pomoc", menu=help_menu)
help_menu.add_command(label="O programie")

# Tworzenie ramki na opis
description_frame = tk.Frame(root)
description_frame.pack(pady=20, padx=20)

# Tworzenie pola tekstowego na opis z zawijaniem tekstu
description_label = tk.Label(description_frame,
                             text="Witaj w moim świecie języka angielskiego. Ta aplikacja przygotowana jest dla wszystkich osób, które chciałyby nauczyć się komunikować w tym języku. Spróbuj i przekonaj się, jakie to proste!",
                             font=("Helvetica", 14), wraplength=400, bg='white')
description_label.pack(pady=10, padx=10)

# Tworzenie ramki na przyciski bez obramowania i tła
frame = tk.Frame(root, bg='lightgrey')  # Ustawienie koloru tła na taki sam jak główne okno
frame.pack(pady=20, padx=20)

# Tworzenie przycisków z nowymi nazwami i większą czcionką
button1 = tk.Button(frame, text="Przeglądaj", font=("Helvetica", 16), command=lambda: open_window1(bg_color))
button1.pack(side=tk.LEFT, padx=5)

button2 = tk.Button(frame, text="Dodaj", font=("Helvetica", 16), command=lambda: open_window2(bg_color))
button2.pack(side=tk.LEFT, padx=5)

button3 = tk.Button(frame, text="Ucz się", font=("Helvetica", 16), command=lambda: open_window3(bg_color))
button3.pack(side=tk.LEFT, padx=5)

button4 = tk.Button(frame, text="Zakończ", font=("Helvetica", 16), command=confirm_exit)
button4.pack(side=tk.LEFT, padx=5)

# Uruchomienie głównej pętli aplikacji
root.mainloop()