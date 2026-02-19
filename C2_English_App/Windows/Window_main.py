import customtkinter as ctk
from PIL import Image

from C2_English_App.Windows.Window_menu import run_window_menu
from C2_English_App.AllClasses.class_AppButton import AppButton


# wymiary głównego okna oraz przesunięcie od krawędzi ekranu
main_page = ctk.CTk(fg_color="white")
main_page.title("The ultimate guide to C2 Proficiency level!")
main_page.geometry('400x300+600+250')
main_page.resizable(False,False)

# Photo for main page
# 1. Wczytanie obrazu z pliku.
image = Image.open("../Images/Photo for title page.png")
# 2. Utworzenie obiektu CTkImage.
photo_for_main_page = ctk.CTkImage(light_image=image, dark_image=image, size=(280,140))
# 3. Utworzenie Labela, który TEN obraz wyświetla.
label = ctk.CTkLabel(main_page, image=photo_for_main_page, text="")
label.place(x=65, y=30)

# przycisk "Let's get started!" wraz z parametrami i ułożeniem na ekranie
button_start_app= AppButton(main_page, text="Let's get started!", command=lambda: run_window_menu(main_page))
button_start_app.place(x=120, y=200)

main_page.mainloop()