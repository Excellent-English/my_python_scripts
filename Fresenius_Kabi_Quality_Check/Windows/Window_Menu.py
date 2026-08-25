import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.Windows.Window_Quality_check_main import run_quality_check_menu


def run_window_menu(main_page):
    # Zamknij / ukryj główne okno
    main_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    menu_page = AppWindow(banner_text = "Main menu", width=800, height=550, x= 310, y = 90, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        menu_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: menu_page.close_the_app(main_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=700, y=5)
    menu_page.bind("<Escape>", lambda event: menu_page.close_the_app(main_page))


    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    menu_page.protocol("WM_DELETE_WINDOW", disable_close)


    line_bottom = ctk.CTkFrame(menu_page, height=2, width=800, fg_color="#DDE2E7", corner_radius=0)
    line_bottom.place(x=0, y=500)


# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    label_top_title = App_Label_Title(menu_page, text="What would you like to do?", font= ("Open Sans", 24, "bold"), text_color = "#755a44", fg_color="#F6F7F9")
    label_top_title.place(x=240, y=90)

    label_top_subtitle = App_Label_Title(menu_page, text="Select an action to continue", font= ("Open Sans", 14), text_color = "#8B7A6B", fg_color="#F6F7F9")
    label_top_subtitle.place(x=300, y=120)

# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check = AppFrame(menu_page)
    frame_quality_check.place(x=100, y=170)

    label_quality_check_title = App_Label_Title(frame_quality_check, text="Quality check", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=110, y=30)

    label_quality_check_title.configure(cursor="hand2")
    label_quality_check_title.bind(
        "<Button-1>",
        lambda event: run_quality_check_menu(menu_page))

    label_quality_check_subtitle = App_Label_Title(frame_quality_check, text="Verify items from\nQuality check", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_quality_check_subtitle.place(x=110, y=65)

# ---------------------------------------------------------------------------------------------------------

    frame_proposal = AppFrame(menu_page)
    frame_proposal.place(x=415, y=170)

    label_proposal_title = App_Label_Title(frame_proposal, text="Proposal", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_proposal_title.place(x=110, y=30)

    label_proposal_subtitle = App_Label_Title(frame_proposal, text="Verify items from\nthe Proposal", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_proposal_subtitle.place(x=110, y=65)

# ---------------------------------------------------------------------------------------------------------

    frame_administration = AppFrame(menu_page)
    frame_administration.place(x=250, y=320)

    label_administration_title = App_Label_Title(frame_administration, text="Administration", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_administration_title.place(x=110, y=30)

    label_administration_subtitle = App_Label_Title(frame_administration, text="Manage users, settings\nand system configuration", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_administration_subtitle.place(x=110, y=65)


# ---------------------------------------------------------------------------------------------------------
# grafiki umieszczone w ramkach na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę quality check
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/quality_check.png")
    # 2. Utworzenie CTkImage
    quality_check_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(80, 80))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    quality_check_btn = ctk.CTkButton(
        frame_quality_check,
        image=quality_check_icon,
        text="",
        width=80,
        height=80,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    quality_check_btn.image = quality_check_icon  # trzymaj referencję!
    quality_check_btn.place(x=10, y=20)

    # Dodanie przycisku zawierającego ikonę proposal
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/proposal.png")
    # 2. Utworzenie CTkImage
    proposal_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(80, 80))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    proposal_btn = ctk.CTkButton(
        frame_proposal,
        image=proposal_icon,
        text="",
        width=80, height=80,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    proposal_btn.image = proposal_icon  # trzymaj referencję!
    proposal_btn.place(x=10, y=20)

    # Dodanie przycisku zawierającego ikonę administration
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/administration.png")
    # 2. Utworzenie CTkImage
    administration_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(80, 80))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    administration_btn = ctk.CTkButton(
        frame_administration,
        image=administration_icon,
        text="",
        width=80, height=80,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    administration_btn.image = administration_icon  # trzymaj referencję!
    administration_btn.place(x=10, y=20)







    # Zaprezentuj okno na ekranie komputera
    menu_page.mainloop()

# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_window_menu(main_page)
