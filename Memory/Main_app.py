import customtkinter as ctk
from Random_values import Random_values

# region Wymiary głównego okna oraz przesunięcie od krawędzi ekranu
root = ctk.CTk(fg_color="#1a1a37")
root.title("Pamięć")
root.geometry('420x460+600+130')
root.resizable(False,False)
# endregion

# region Pierwsza losowarka i nadanie wartości current_number oraz moves
number_gen = Random_values()
numbers = number_gen.randomly_choose_numbers()
current_number = 1
moves = 0
# endregion

# region Funkcje do resetu gry, animacji oraz rozpoczęcia nowej gry
def reset_game():
    global current_number
    current_number = 1

    button1.configure(text="")
    button2.configure(text="")
    button3.configure(text="")
    button4.configure(text="")
    button5.configure(text="")
    button6.configure(text="")
    button7.configure(text="")
    button8.configure(text="")
    button9.configure(text="")
    button10.configure(text="")
    button11.configure(text="")
    button12.configure(text="")

    button1.configure(fg_color="#4b55e6")
    button2.configure(fg_color="#4b55e6")
    button3.configure(fg_color="#4b55e6")
    button4.configure(fg_color="#4b55e6")
    button5.configure(fg_color="#4b55e6")
    button6.configure(fg_color="#4b55e6")
    button7.configure(fg_color="#4b55e6")
    button8.configure(fg_color="#4b55e6")
    button9.configure(fg_color="#4b55e6")
    button10.configure(fg_color="#4b55e6")
    button11.configure(fg_color="#4b55e6")
    button12.configure(fg_color="#4b55e6")

def new_game_mode():
    global numbers, current_number, moves
    current_number = 1
    moves = 0
    title_label.configure(text=f"Liczba ruchów: {moves}")

    number_gen = Random_values()
    numbers = number_gen.randomly_choose_numbers()

    button1.hidden_value = numbers["zmienna_1"]
    button2.hidden_value = numbers["zmienna_2"]
    button3.hidden_value = numbers["zmienna_3"]
    button4.hidden_value = numbers["zmienna_4"]
    button5.hidden_value = numbers["zmienna_5"]
    button6.hidden_value = numbers["zmienna_6"]
    button7.hidden_value = numbers["zmienna_7"]
    button8.hidden_value = numbers["zmienna_8"]
    button9.hidden_value = numbers["zmienna_9"]
    button10.hidden_value = numbers["zmienna_10"]
    button11.hidden_value = numbers["zmienna_11"]
    button12.hidden_value = numbers["zmienna_12"]

    reset_game()

def flip_animation(button, new_text, step=0):
    if step < 10:
        button.configure(width=120 - step*10)
        root.after(10, lambda: flip_animation(button, new_text, step + 1))
    elif step == 10:
        button.configure(text=new_text)
        root.after(10, lambda: flip_animation(button, new_text, step + 1))
    elif step < 20:
        button.configure(width=(step-10)*10)
        root.after(10, lambda: flip_animation(button, new_text, step + 1))
    else:
        button.configure(width=120)

# endregion

# region Funkcje działające po kliknięciu na przyciski
def button1_click():
    global current_number, moves
    if current_number == button1.hidden_value:
        flip_animation(button1, str(button1.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button1.configure(fg_color="#5bc46b")
    else:
        button1.configure(text=str(button1.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button2_click():
    global current_number, moves
    if current_number == button2.hidden_value:
        flip_animation(button2, str(button2.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button2.configure(fg_color="#5bc46b")
    else:
        button2.configure(text=str(button2.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button3_click():
    global current_number, moves
    if current_number == button3.hidden_value:
        flip_animation(button3, str(button3.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button3.configure(fg_color="#5bc46b")
    else:
        button3.configure(text=str(button3.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button4_click():
    global current_number, moves
    if current_number == button4.hidden_value:
        flip_animation(button4, str(button4.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button4.configure(fg_color="#5bc46b")
    else:
        button4.configure(text=str(button4.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button5_click():
    global current_number, moves
    if current_number == button5.hidden_value:
        flip_animation(button5, str(button5.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button5.configure(fg_color="#5bc46b")
    else:
        button5.configure(text=str(button5.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button6_click():
    global current_number, moves
    if current_number == button6.hidden_value:
        flip_animation(button6, str(button6.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button6.configure(fg_color="#5bc46b")
    else:
        button6.configure(text=str(button6.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button7_click():
    global current_number, moves
    if current_number == button7.hidden_value:
        flip_animation(button7, str(button7.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button7.configure(fg_color="#5bc46b")
    else:
        button7.configure(text=str(button7.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button8_click():
    global current_number, moves
    if current_number == button8.hidden_value:
        flip_animation(button8, str(button8.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button8.configure(fg_color="#5bc46b")
    else:
        button8.configure(text=str(button8.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button9_click():
    global current_number, moves
    if current_number == button9.hidden_value:
        flip_animation(button9, str(button9.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button9.configure(fg_color="#5bc46b")
    else:
        button9.configure(text=str(button9.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button10_click():
    global current_number, moves
    if current_number == button10.hidden_value:
        flip_animation(button10, str(button10.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button10.configure(fg_color="#5bc46b")
    else:
        button10.configure(text=str(button10.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button11_click():
    global current_number, moves
    if current_number == button11.hidden_value:
        flip_animation(button11, str(button11.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button11.configure(fg_color="#5bc46b")
    else:
        button11.configure(text=str(button11.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")

def button12_click():
    global current_number, moves
    if current_number == button12.hidden_value:
        flip_animation(button12, str(button12.hidden_value))
        current_number += 1
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
        button12.configure(fg_color="#5bc46b")
    else:
        button12.configure(text=str(button12.hidden_value))
        root.after(1000, reset_game)
        moves += 1
        title_label.configure(text=f"Liczba ruchów: {moves}")
# endregion

# region Opis przycisków
button1 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button1_click
    )
button1.hidden_value = numbers["zmienna_1"]

button2 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button2_click
    )
button2.hidden_value = numbers["zmienna_2"]

button3 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button3_click
    )
button3.hidden_value = numbers["zmienna_3"]

button4 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button4_click
    )
button4.hidden_value = numbers["zmienna_4"]

button5 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button5_click
    )
button5.hidden_value = numbers["zmienna_5"]

button6 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button6_click
    )
button6.hidden_value = numbers["zmienna_6"]

button7 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button7_click
    )
button7.hidden_value = numbers["zmienna_7"]

button8 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button8_click
    )
button8.hidden_value = numbers["zmienna_8"]

button9 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button9_click
    )
button9.hidden_value = numbers["zmienna_9"]

button10 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button10_click
    )
button10.hidden_value = numbers["zmienna_10"]

button11 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button11_click
    )
button11.hidden_value = numbers["zmienna_11"]

button12 = ctk.CTkButton(
    root,
    text="",
    font=ctk.CTkFont(size=22),
    width=120,
    height=70,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=button12_click
    )
button12.hidden_value = numbers["zmienna_12"]

# --- PRZYCISK NOWA GRA ---
newgame_button = ctk.CTkButton(
    root,
    text="Nowa gra",
    width=380,
    height=50,
    font=ctk.CTkFont(size=18),
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=new_game_mode
)

# endregion

# region Umiejscowienie przycisków na planszy
button1.place(x=20, y=40)
button2.place(x=150, y=40)
button3.place(x=280, y=40)
button4.place(x=20, y=120)
button5.place(x=150, y=120)
button6.place(x=280, y=120)
button7.place(x=20, y=200)
button8.place(x=150, y=200)
button9.place(x=280, y=200)
button10.place(x=20, y=280)
button11.place(x=150, y=280)
button12.place(x=280, y=280)

newgame_button.place(x=20, y=370)

# endregion

# region Pole tekstowe z liczbą ruchów
title_label = ctk.CTkLabel(
    root,
    text=f"Liczba ruchów: {moves}",
    font=ctk.CTkFont(size=12),
    text_color="grey"
)
title_label.place(x=290, y=7)
# endregion

root.mainloop()


# CORRECT_COLOR = "#5bc46b"
# WRONG_COLOR = "#d9534f"
# DEFAULT_COLOR = "#4b55e6"
# HOVER_COLOR = "#4048bc"