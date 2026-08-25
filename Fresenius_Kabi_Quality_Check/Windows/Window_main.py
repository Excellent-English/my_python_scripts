import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.Windows.Window_Menu import run_window_menu
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard


# wymiary głównego okna oraz przesunięcie od krawędzi ekranu
main_page = ctk.CTk(fg_color="white")
main_page.title("Verify quality check & proposal items")
main_page.geometry('400x300+600+250')
main_page.resizable(False,False)

# Photo for main page
# 1. Wczytanie obrazu z pliku.
image = Image.open("../Images/kabi_logo.png")
# 2. Utworzenie obiektu CTkImage.
photo_for_main_page = ctk.CTkImage(light_image=image, dark_image=image, size=(280,90))
# 3. Utworzenie Labela, który TEN obraz wyświetla.
label = ctk.CTkLabel(main_page, image=photo_for_main_page, text="")
label.place(x=65, y=50)

# przycisk "Let's get started!" wraz z parametrami i ułożeniem na ekranie
button_start_app= Button_Standard(main_page, text="Let's get started!", command=lambda: run_window_menu(main_page))
button_start_app.place(x=120, y=190)

main_page.mainloop()