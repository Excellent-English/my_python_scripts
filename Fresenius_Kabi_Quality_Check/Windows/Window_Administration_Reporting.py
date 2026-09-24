import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database_Admin import Database_Admin
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppComboBox
from Fresenius_Kabi_Quality_Check.AllClasses.App_Entry_Box import App_Entry_Box

global country, company_code, current_monthly_posted_documents, current_amount_limit, current_new_hire_percentage

db = Database()
db_admin = Database_Admin()
countries = db.get_countries()

def run_window_administraton_reporting(adm_page, user_email_address):
    # Zamknij / ukryj główne okno
    adm_page.withdraw()   # albo destroy()
    # ctk.deactivate_automatic_dpi_awareness()

    # Utwórz nowe okno menu
    reporting_page = AppWindow(banner_text = "Reporting", width=1100, height=600, x= 110, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        reporting_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: reporting_page.close_the_app(adm_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=900, y=5)
    reporting_page.bind("<Escape>", lambda event: reporting_page.close_the_app(adm_page))

    logout_subtitle = ctk.CTkLabel(reporting_page, text="Logout", font= ("Open Sans", 14), text_color = "white", fg_color = "#755a44")
    logout_subtitle.place(x=955, y=12)

# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        reporting_page.withdraw()
        adm_page.deiconify()
        adm_page.lift()
        adm_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Return_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20,30))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        reporting_page.banner_frame,
        image=power_off_icon,
        text="",
        width=20, height=30,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: return_to_previous_window()
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=50, y=7)

# ---------------------------------------------------------------------------------

    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    reporting_page.protocol("WM_DELETE_WINDOW", disable_close)


    line_bottom = ctk.CTkFrame(reporting_page, height=2, width=1100, fg_color="#DDE2E7", corner_radius=0)
    line_bottom.place(x=0, y=500)











# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_step_1 = AppFrame(reporting_page, height= 250)
    frame_step_1.place(x=80, y=170)

    label_step_1_title = App_Label_Title(frame_step_1, text="STEP 1", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_step_1_title.place(x=100, y=20)

    label_step_1_subtitle = App_Label_Title(frame_step_1, text="Choose country and company code", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_1_subtitle.place(x=30, y=50)

    dropdown_countries = AppComboBox(frame_step_1, width = 260, values=countries)
    dropdown_countries.place(x=20, y=100)
    dropdown_countries.set("---")

    dropdown_company_codes = AppComboBox(frame_step_1, width = 260, values=["---"])
    dropdown_company_codes.place(x=20, y=170)


# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    adm_page = ctk.CTk()
    adm_page.withdraw()

    run_window_administraton_reporting(adm_page, user_email_address)
    adm_page.mainloop()