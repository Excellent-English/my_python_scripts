import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppDropdown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown


def run_quality_check_menu(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    quality_check_page = AppWindow(banner_text = "Quality check audit", width=800, height=550, x= 310, y = 90, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        quality_check_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: quality_check_page.close_the_app(menu_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=700, y=5)
    quality_check_page.bind("<Escape>", lambda event: menu_page.close_the_app(main_page))


    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    menu_page.protocol("WM_DELETE_WINDOW", disable_close)


    line_bottom = ctk.CTkFrame(quality_check_page, height=2, width=800, fg_color="#DDE2E7", corner_radius=0)
    line_bottom.place(x=0, y=500)


# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramki na stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check = AppFrame(quality_check_page, width = 600, height = 380)
    frame_quality_check.place(x=90, y=100)

    label_quality_check_title = App_Label_Title(frame_quality_check, text="Load Quality check items", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=145, y=30)

    label_quality_check_subtitle = App_Label_Title(frame_quality_check, text="Select country and company code to load items for audit", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_quality_check_subtitle.place(x=145, y=65)

    line_frame_bottom = ctk.CTkFrame(frame_quality_check, height=2, width=500, fg_color="#DDE2E7", corner_radius=0)
    line_frame_bottom.place(x=40, y=120)

    label_quality_check_country = App_Label_Title(frame_quality_check, text="Country", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_country.place(x=35, y=140)

    dropdown_countries = AppDropdown(frame_quality_check, values=["Poland", "Germany", "France"])
    dropdown_countries.place(x=40, y=170)

    label_quality_check_company_code = App_Label_Title(frame_quality_check, text="Company Code", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_company_code.place(x=35, y=220)

    dropdown_company_codes = AppDropdown(frame_quality_check, values=["0001", "0055", "207B"])
    dropdown_company_codes.place(x=40, y=250)

    button_load_items = Button_Brown(frame_quality_check, text= "Load items")
    button_load_items.place(x=200, y=310)


    # ---------------------------------------------------------------------------------------------------------
# grafiki umieszczone w ramkach na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę quality check
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/quality_check.png")
    # 2. Utworzenie CTkImage
    quality_check_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(100, 100))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    quality_check_btn = ctk.CTkButton(
        frame_quality_check,
        image=quality_check_icon,
        text="",
        width=100,
        height=100,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    quality_check_btn.image = quality_check_icon  # trzymaj referencję!
    quality_check_btn.place(x=20, y=10)





    # Zaprezentuj okno na ekranie komputera
    quality_check_page.mainloop()

# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_quality_check_menu(main_page)
