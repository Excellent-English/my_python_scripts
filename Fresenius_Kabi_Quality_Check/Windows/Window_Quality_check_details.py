import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppDropdown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown

def run_quality_check_details(quality_check_page):
    # Zamknij / ukryj główne okno
    quality_check_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    quality_check_details_page = AppWindow(banner_text = "Quality check details", width=1200, height=600, x= 30, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        quality_check_details_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: quality_check_details_page.close_the_app(quality_check_details_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=700, y=5)
    quality_check_details_page.bind("<Escape>", lambda event: quality_check_details_page.close_the_app(main_page))


    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    quality_check_details_page.protocol("WM_DELETE_WINDOW", disable_close)



# ---------------------------------------------------------------------------------------------------------
# ramka po lewej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_left = AppFrame(quality_check_details_page, width = 350, height = 430)
    frame_quality_check_details_left.place(x=30, y=140)

    label_quality_check_title = App_Label_Title(frame_quality_check_details_left, text="Main title", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=30, y=30)

    label_quality_check_subtitle = App_Label_Title(frame_quality_check_details_left, text="Subtitle", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_quality_check_subtitle.place(x=30, y=65)

    line_frame_bottom = ctk.CTkFrame(quality_check_details_page, height=2, width=500, fg_color="#DDE2E7", corner_radius=0)
    line_frame_bottom.place(x=600, y=70)

    label_quality_check_country = App_Label_Title(quality_check_details_page, text="Country", font= ("Open Sans", 14), text_color = "#755a44", fg_color = "#F6F7F9")
    label_quality_check_country.place(x=30, y=60)

    dropdown_countries = AppDropdown(quality_check_details_page, values=["Poland", "Germany", "France"], width = 200)
    dropdown_countries.place(x=30, y=88)

    label_quality_check_company_code = App_Label_Title(quality_check_details_page, text="Company Code", font= ("Open Sans", 14), text_color = "#755a44", fg_color = "#F6F7F9")
    label_quality_check_company_code.place(x=260, y=60)

    dropdown_company_codes = AppDropdown(quality_check_details_page, values=["0001", "0055", "207B"], width = 200)
    dropdown_company_codes.place(x=260, y=88)

    button_load_items = Button_Brown(quality_check_details_page, text= "Load items")
    button_load_items.place(x=480, y=77)

# ---------------------------------------------------------------------------------------------------------
# ramka po prawej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_right = AppFrame(quality_check_details_page, width = 750, height = 430)
    frame_quality_check_details_right.place(x=400, y=140)







    # Zaprezentuj okno na ekranie komputera
    quality_check_details_page.mainloop()

# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_quality_check_details(main_page)
