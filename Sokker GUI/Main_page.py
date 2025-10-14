import customtkinter as ctk
from PIL import Image, ImageTk
from Start_page import uruchom_aplikacje

    # wymiary głównego okna oraz przesunięcie od krawędzi ekranu
root = ctk.CTk(fg_color="#1a1a37")
root.title("Twój przewodnik po świecie Sokkera!")
root.geometry('400x500+600+130')
root.resizable(False,False)

    # dodanie label dla tytułu
title_label = ctk.CTkLabel(
    root,
    text="Statystyki, raporty\ni wiele innych...",
    font=ctk.CTkFont(size=22),
    text_color="white"
)
title_label.place(x=110, y=30)

    # załadowanie obrazu na stronę główna
image = Image.open("Miedziaki Lubin.png")
bg_image = ctk.CTkImage(light_image=image, dark_image=image, size=(260, 260))

    # dodanie label dla obrazu
label = ctk.CTkLabel(root, image=bg_image, text="")
label.place(x=70, y=110)

    # przycisk "Zaczynamy!" wraz z parametrami i ułożeniem na ekranie
button1 = ctk.CTkButton(
    root,
    text="Zaczynamy!",
    font=ctk.CTkFont(size=16),
    width=160,
    height=50,
    text_color="white",
    fg_color="#4b55e6",
    hover_color="#4048bc",
    command=uruchom_aplikacje)
button1.place(x=120, y=400)


root.mainloop()