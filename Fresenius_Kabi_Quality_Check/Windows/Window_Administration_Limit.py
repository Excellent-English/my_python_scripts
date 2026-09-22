import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title


def run_window_administraton_limit(adm_page):
    # Zamknij / ukryj główne okno
    adm_page.withdraw()   # albo destroy()
    # ctk.deactivate_automatic_dpi_awareness()

    # Utwórz nowe okno menu
    limit_page = AppWindow(banner_text = "Limit Management", width=1100, height=600, x= 110, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        limit_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: limit_page.close_the_app(adm_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=900, y=5)
    limit_page.bind("<Escape>", lambda event: limit_page.close_the_app(adm_page))

    logout_subtitle = ctk.CTkLabel(limit_page, text="Logout", font= ("Open Sans", 14), text_color = "white", fg_color = "#755a44")
    logout_subtitle.place(x=955, y=12)

# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        limit_page.withdraw()
        adm_page.deiconify()
        adm_page.lift()
        adm_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Return_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20,30))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        limit_page.banner_frame,
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
    limit_page.protocol("WM_DELETE_WINDOW", disable_close)


    line_bottom = ctk.CTkFrame(limit_page, height=2, width=1100, fg_color="#DDE2E7", corner_radius=0)
    line_bottom.place(x=0, y=500)


# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    label_top_title = App_Label_Title(limit_page, text="Administration", font= ("Open Sans", 24, "bold"), text_color = "#755a44", fg_color="#F6F7F9")
    label_top_title.place(x=450, y=90)

    label_top_subtitle = App_Label_Title(limit_page, text="Manage users, limits and reporting settings for the system", font= ("Open Sans", 14), text_color = "#8B7A6B", fg_color="#F6F7F9")
    label_top_subtitle.place(x=350, y=120)

# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check = AppFrame(limit_page, height= 250)
    frame_quality_check.place(x=80, y=170)

    label_quality_check_title = App_Label_Title(frame_quality_check, text="People Management", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=40, y=130)

    # label_quality_check_title.configure(cursor="hand2")
    # label_quality_check_title.bind(
    #     "<Button-1>",
    #     lambda event: run_quality_check_menu(menu_page))

    label_quality_check_subtitle = App_Label_Title(frame_quality_check, text="Manage users, access rights\nand organization structure", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_quality_check_subtitle.place(x=55, y=180)

# ---------------------------------------------------------------------------------------------------------

    frame_proposal = AppFrame(limit_page, height= 250)
    frame_proposal.place(x=395, y=170)

    label_proposal_title = App_Label_Title(frame_proposal, text="Limit management", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_proposal_title.place(x=50, y=130)

    label_proposal_subtitle = App_Label_Title(frame_proposal, text="View and configure\nall tresholds and limits", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_proposal_subtitle.place(x=75, y=180)

# ---------------------------------------------------------------------------------------------------------

    frame_administration = AppFrame(limit_page, height= 250)
    frame_administration.place(x=710, y=170)

    label_administration_title = App_Label_Title(frame_administration, text="Reporting", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_administration_title.place(x=90, y=130)

    label_administration_subtitle = App_Label_Title(frame_administration, text="Generate and view reports,\nmetrics and audit activity", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_administration_subtitle.place(x=60, y=180)


# ---------------------------------------------------------------------------------------------------------
# grafiki umieszczone w ramkach na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę quality check
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/People management.png")
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
    quality_check_btn.place(x=90, y=15)

    # Dodanie przycisku zawierającego ikonę proposal
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Limit management.png")
    # 2. Utworzenie CTkImage
    proposal_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(100, 100))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    proposal_btn = ctk.CTkButton(
        frame_proposal,
        image=proposal_icon,
        text="",
        width=100, height=100,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    proposal_btn.image = proposal_icon  # trzymaj referencję!
    proposal_btn.place(x=90, y=15)

    # Dodanie przycisku zawierającego ikonę administration
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Reporting.png")
    # 2. Utworzenie CTkImage
    administration_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(100, 100))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    administration_btn = ctk.CTkButton(
        frame_administration,
        image=administration_icon,
        text="",
        width=100, height=100,
        fg_color="white",
        hover=False,
        border_width=0,
        command=None
    )
    administration_btn.image = administration_icon  # trzymaj referencję!
    administration_btn.place(x=90, y=15)


    # funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    adm_page = ctk.CTk()
    adm_page.withdraw()

    run_window_administraton_limit(adm_page)
    adm_page.mainloop()