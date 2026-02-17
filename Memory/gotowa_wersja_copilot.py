
import customtkinter as ctk
from Random_values import Random_values

# --- konfiguracja okna ---
root = ctk.CTk(fg_color="#1a1a37")
root.title("Czy potrafisz zapamiętać cały układ?")
root.geometry('420x460+600+130')
root.resizable(False, False)

# --- losowanie liczb (TYLKO RAZ!) ---
rng = Random_values()
numbers = rng.randomly_choose_numbers()

# --- bieżąca szukana liczba ---
current_number = 1

# --- lista przycisków ---
buttons = []

# --- kolory animacji ---
CORRECT_COLOR = "#5bc46b"
WRONG_COLOR = "#d9534f"
DEFAULT_COLOR = "#4b55e6"
HOVER_COLOR = "#4048bc"


# --- animacja poprawnego kliknięcia ---
def animate_correct(btn, value):
    btn.configure(fg_color=CORRECT_COLOR)

    root.after(80, lambda: btn.configure(fg_color="#7ddc8a"))
    root.after(160, lambda: btn.configure(fg_color=CORRECT_COLOR))
    root.after(240, lambda: btn.configure(text=str(value)))


# --- obsługa kliknięcia ---
def on_button_click(idx):
    global current_number

    value = numbers[f"zmienna_{idx}"]

    # POPRAWNA ODPOWIEDŹ
    if value == current_number:
        animate_correct(buttons[idx - 1], value)
        current_number += 1

        if current_number > 12:
            print("WYGRAŁEŚ!")

    # ZŁA ODPOWIEDŹ
    else:
        # pokaż błędną wartość na 1 sekundę
        buttons[idx - 1].configure(text=str(value), fg_color=WRONG_COLOR)

        def reset_after_delay():
            for b in buttons:
                b.configure(text="", fg_color=DEFAULT_COLOR)
            global current_number
            current_number = 1

        # po sekundzie reset
        root.after(1000, reset_after_delay)


# --- RESET GRY / NOWA GRA ---
def new_game():
    global numbers, current_number

    current_number = 1
    numbers = rng.randomly_choose_numbers()

    for b in buttons:
        b.configure(text="", fg_color=DEFAULT_COLOR)

    newgame_button.configure(fg_color="#7aa7ff")
    root.after(150, lambda: newgame_button.configure(fg_color="#4b55e6"))


# --- tworzenie 12 przycisków ---
positions = [
    (20, 40), (150, 40), (280, 40),
    (20, 120), (150, 120), (280, 120),
    (20, 200), (150, 200), (280, 200),
    (20, 280), (150, 280), (280, 280)
]

for i in range(1, 13):
    btn = ctk.CTkButton(
        root,
        text="",
        width=120,
        height=70,
        fg_color=DEFAULT_COLOR,
        hover_color=HOVER_COLOR,
        font=ctk.CTkFont(size=22),
        command=lambda x=i: on_button_click(x)
    )
    btn.place(x=positions[i - 1][0], y=positions[i - 1][1])
    buttons.append(btn)


# --- PRZYCISK NOWA GRA ---
newgame_button = ctk.CTkButton(
    root,
    text="Nowa gra",
    width=380,
    height=50,
    font=ctk.CTkFont(size=18),
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=new_game
)

newgame_button.place(x=20, y=370)

root.mainloop()
