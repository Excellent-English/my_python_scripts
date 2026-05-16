import customtkinter as ctk
from Random_values import Random_values

# Wymiary głównego okna oraz przesunięcie od krawędzi ekranu
root = ctk.CTk(fg_color="#1a1a37")
root.title("Timer")
root.geometry('420x460+600+130')
root.resizable(False,False)

# napis proszący użytkownika o podanie imienia
label_your_name = ctk.CTkLabel(
    root,
    text="Your name:",
    font=ctk.CTkFont(size=18),
    text_color="white"
    # command=new_game_mode
)
label_your_name.place(x= 80, y= 40)

# miejsce do wpisania imienia, entry box zawiera wymuszenie aktywności podczas uruchamiania okna
input_your_name = ctk.CTkEntry(
    root,
    font=ctk.CTkFont(size=16),
    text_color="white",
    fg_color="#1a1a37"
    # command=new_game_mode
)
input_your_name.place(x= 180, y= 40)
root.after(100, lambda: input_your_name.focus())

# przycisk START uruchamiający czas
start_button = ctk.CTkButton(
    root,
    text="START",
    width=210,
    height=100,
    font=ctk.CTkFont(size=25),
    fg_color="#4b55e6",
    hover_color="#4048bc",
    # command=new_game_mode
)
start_button.place(x= 100, y= 100)






# # Powiązanie z oknem (obsłuży Enter z głównej klawiatury i z klawiatury numerycznej)
# vocabulary_learn_page.bind("<Return>", on_enter)
# vocabulary_learn_page.bind("<KP_Enter>", on_enter)

root.mainloop()