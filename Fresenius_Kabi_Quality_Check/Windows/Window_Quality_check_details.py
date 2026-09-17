import customtkinter as ctk
from PIL import Image
from click import command

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppComboBox
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.App_Entry_Box import App_Entry_Box
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database
from Fresenius_Kabi_Quality_Check.Windows import Window_Quality_check_main

db = Database()
countries = db.get_countries()

def run_quality_check_details(quality_check_page):
    # Zamknij / ukryj główne okno
    quality_check_page.withdraw()   # albo destroy()

    # Utwórz nowe okno
    quality_check_page_details = AppWindow(banner_text = "Quality check audit", width=1100, height=600, x= 120, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")

# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        quality_check_page_details.withdraw()
        quality_check_page.deiconify()
        quality_check_page.lift()
        quality_check_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Return_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20, 30))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        quality_check_page_details.banner_frame,
        image=power_off_icon,
        text="",
        width=20, height=30,
        fg_color="transparent",
        hover_color="#755a44",
        command=lambda: return_to_previous_window()
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=50, y=7)

# ---------------------------------------------------------------------------------

    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    quality_check_page_details.protocol("WM_DELETE_WINDOW", disable_close)


# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramki na stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_top = AppFrame(quality_check_page_details, width = 1000, height = 100)
    frame_quality_check_details_top.place(x=50, y=65)

    label_quality_check_title = App_Label_Title(frame_quality_check_details_top, text="ITEM DETAILS", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=20, y=8)

    label_quality_check_subtitle_1 = App_Label_Title(frame_quality_check_details_top, text="SAP Document number", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_1.place(x=20, y=40)

    label_quality_check_element_1 = App_Label_Title(frame_quality_check_details_top, text="SAP-001-1234", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_1.place(x=23, y=60)

    label_quality_check_subtitle_2 = App_Label_Title(frame_quality_check_details_top, text="Company code", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_2.place(x=150, y=40)

    label_quality_check_element_2 = App_Label_Title(frame_quality_check_details_top, text="PL201B", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_2.place(x=158, y=60)

    label_quality_check_subtitle_3 = App_Label_Title(frame_quality_check_details_top, text="Document date", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_3.place(x=250, y=40)

    label_quality_check_element_3 = App_Label_Title(frame_quality_check_details_top, text="2025-05-30", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_3.place(x=251, y=60)

    label_quality_check_subtitle_4 = App_Label_Title(frame_quality_check_details_top, text="Due date", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_4.place(x=360, y=40)

    label_quality_check_element_4 = App_Label_Title(frame_quality_check_details_top, text="2026-09-09", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_4.place(x=350, y=60)

    label_quality_check_subtitle_5 = App_Label_Title(frame_quality_check_details_top, text="Amount in local currency", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_5.place(x=445, y=40)

    label_quality_check_element_5 = App_Label_Title(frame_quality_check_details_top, text="75,678", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_5.place(x=474, y=60)

    label_quality_check_subtitle_6 = App_Label_Title(frame_quality_check_details_top, text="Currency", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_6.place(x=580, y=40)

    label_quality_check_element_6 = App_Label_Title(frame_quality_check_details_top, text="SEK", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_6.place(x=583, y=60)

    label_quality_check_subtitle_7 = App_Label_Title(frame_quality_check_details_top, text="Amount in EUR", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_7.place(x=650, y=40)

    label_quality_check_element_7 = App_Label_Title(frame_quality_check_details_top, text="44,643", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_7.place(x=663, y=60)

    label_quality_check_subtitle_8 = App_Label_Title(frame_quality_check_details_top, text="Vendor number", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_8.place(x=750, y=40)

    label_quality_check_element_8 = App_Label_Title(frame_quality_check_details_top, text="00432567335", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_8.place(x=748, y=60)

    label_quality_check_subtitle_9 = App_Label_Title(frame_quality_check_details_top, text="Vendor type", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_9.place(x=850, y=40)

    label_quality_check_element_9 = App_Label_Title(frame_quality_check_details_top, text="External", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_9.place(x=851, y=60)

    line_frame_top = ctk.CTkFrame(frame_quality_check_details_top, height=2, width=895, fg_color="#DDE2E7", corner_radius=0)
    line_frame_top.place(x=25, y=35)


    frame_quality_check_details_bottom = AppFrame(quality_check_page_details, width = 1000, height = 340)
    frame_quality_check_details_bottom.place(x=50, y=175)



    button_load_items = Button_Brown(quality_check_page_details, text= " Save and Next Item   ► ")
    button_load_items.place(x=450, y=530)


# ---------------------------------------------------------------------------------------------------------
# grafiki umieszczone w ramkach na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        quality_check_page_details.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: quality_check_page.close_the_app(quality_check_page_details)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=880, y=5)
    quality_check_page.bind("<Escape>", lambda event: quality_check_page_details.close_the_app(main_page))

    # napis Logout
    logout_subtitle = ctk.CTkLabel(quality_check_page_details, text="Logout", font= ("Open Sans", 14), text_color = "white", fg_color = "#755a44")
    logout_subtitle.place(x=935, y=12)


    # Zaprezentuj okno na ekranie komputera
    quality_check_page_details.mainloop()

# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_quality_check_details(main_page)