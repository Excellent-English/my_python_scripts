import customtkinter as ctk
from PIL import Image
import win32api
from Fresenius_Kabi_Quality_Check.Windows.Window_Menu import run_window_menu
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database
from Fresenius_Kabi_Quality_Check.AllClasses.Resource_Path import resource_path
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title


# Pobranie adresu e-mail zalogowanego użytkownika
user_email_address = win32api.GetUserNameEx(8)
print(f"E-mail address of the user: {user_email_address}")
# Pobranie SAP ID i roli administratora
db = Database()
sap_id, admin_role, user_email_address = db.get_sap_id_based_on_email_address(user_email_address)

if sap_id is None:
    print("User not found")


# wymiary głównego okna oraz przesunięcie od krawędzi ekranu
main_page = ctk.CTk(fg_color="white")
main_page.title("Verify quality check & proposal items")
main_page.geometry('400x300+600+250')
main_page.resizable(False,False)

# Photo for main page
# 1. Wczytanie obrazu z pliku.
image = Image.open(resource_path("Images/kabi_logo.png"))
# image = Image.open("../Images/kabi_logo.png")
# 2. Utworzenie obiektu CTkImage.
photo_for_main_page = ctk.CTkImage(light_image=image, dark_image=image, size=(280,90))
# 3. Utworzenie Labela, który TEN obraz wyświetla.
label = ctk.CTkLabel(main_page, image=photo_for_main_page, text="")
label.place(x=65, y=50)

# label pokazujący komunikat w razie nieznalezienia usera w bazie
system_warning = App_Label_Title(main_page, text="", font= ("Open Sans", 14), text_color = "#A94442")
system_warning.place(x=90, y=250)

# przycisk "Let's get started!" wraz z parametrami i ułożeniem na ekranie
button_start_app= Button_Standard(main_page, text="Let's get started!", command=lambda: run_window_menu(main_page, user_email_address, sap_id, admin_role))
button_start_app.place(x=120, y=190)

# wyłączenie przycisku i pojawienie się komunikatu, gdy SAP ID nie został znaleziony
if sap_id is None:
    button_start_app.configure(state="disabled")
    system_warning.configure(text="Your account has not been found.\nPlease contact the administrator.")
else:
    button_start_app.configure(state="normal")

main_page.mainloop()