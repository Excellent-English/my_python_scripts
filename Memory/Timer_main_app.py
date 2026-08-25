import customtkinter as ctk
import time
from Timer_database import Database

start_time = None
target = 10
my_database = Database()

# Wymiary głównego okna oraz przesunięcie od krawędzi ekranu
root = ctk.CTk(fg_color="#1a1a37")
root.title("Timer")
root.geometry('420x460+600+130')
root.resizable(False,False)

def start_game():
    global start_time

    name = input_your_name.get().strip()
    if not name:
        label_how_to_end_game.configure(text="Podaj imię!")
        return

    start_time = time.time()
    start_button.configure(state="disabled")
    label_how_to_end_game.configure(text="Naciśnij Enter, aby zakończyć grę.")
    print(start_time)

def end_game():
    global target
    end_time = time.time()
    start_button.configure(state="normal")
    label_how_to_end_game.configure(text="")
    print(end_time)
    result_in_app = end_time - start_time
    print(f'Twój czas to: {result_in_app}.')
    result_to_database = abs(result_in_app - target)
    print(f'Wynik zapisany do bazy to: {result_to_database}.')

    label_your_result_is.configure(text="Twój wynik to:")
    label_your_result.configure(text=f'{result_in_app:.3f} s')
    #my_database.add_result(input_your_name.get(), result_to_database)

    # 1) Zapis + LP rekordu
    lp = my_database.add_result(input_your_name.get(), result_to_database)

    # 2) Miejsce w rankingu
    place = my_database.get_place(lp)
    total = my_database.count_results()

    label_your_place.configure(text=f"Miejsce: {place}/{total}")



# Ustawienie Entera jako domyślnego przycisku do uruchamiania funkcji change_word() lub check_answer()
def on_enter(event=None):
    is_enabled = str(start_button.cget("state")) == "normal"
    if is_enabled:
        start_game()
    else:
        end_game()

# Powiązanie z oknem (obsłuży Enter z głównej klawiatury i z klawiatury numerycznej)
root.bind("<Return>", on_enter)
root.bind("<KP_Enter>", on_enter)




# napis proszący użytkownika o podanie imienia
label_your_name = ctk.CTkLabel(
    root,
    text="Twoje imię:",
    font=ctk.CTkFont(size=18),
    text_color="white"
)
label_your_name.place(x= 80, y= 40)

# miejsce do wpisania imienia, entry box zawiera wymuszenie aktywności podczas uruchamiania okna
input_your_name = ctk.CTkEntry(
    root,
    font=ctk.CTkFont(size=16),
    text_color="white",
    fg_color="#1a1a37"
)
input_your_name.place(x= 190, y= 40)
root.after(100, lambda: input_your_name.focus())

# przycisk START uruchamiający czas
start_button = ctk.CTkButton(
    root,
    text="START",
    width=210,
    height=100,
    font=ctk.CTkFont(size=30),
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=start_game
)
start_button.place(x= 100, y= 100)

# napis informujący o możliwości zakończenia gry
label_how_to_end_game = ctk.CTkLabel(
    root,
    text="",
    font=ctk.CTkFont(size=12),
    text_color="white"
)
label_how_to_end_game.place(x= 113, y= 205)

# napis nad wynikiem użytkownika
label_your_result_is = ctk.CTkLabel(
    root,
    text="",
    font=ctk.CTkFont(size=16),
    text_color="white"
)
label_your_result_is.place(x= 150, y= 275)

# napis informujący o wyniku użytkownika
label_your_result = ctk.CTkLabel(
    root,
    text="",
    font=ctk.CTkFont(size=30),
    text_color="white"
)
label_your_result.place(x= 150, y= 320)

# informacja o zajętym miejscu
label_your_place = ctk.CTkLabel(root, text="", font=ctk.CTkFont(size=16), text_color="white")
label_your_place.place(x=150, y=370)



root.mainloop()