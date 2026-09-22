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
from Fresenius_Kabi_Quality_Check.Windows.Window_Quality_check_details import run_quality_check_details
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database

db = Database()
countries = db.get_countries()
global first_selected_item
global number_of_items_selected_all
global total_items
global items_not_mine

def run_quality_check_menu(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    quality_check_page = AppWindow(banner_text = "Quality check audit", width=1020, height=600, x= 120, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")

    total_items = 0
    items_not_mine = 0
# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        quality_check_page.withdraw()
        menu_page.deiconify()
        menu_page.lift()
        menu_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Return_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20, 30))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        quality_check_page.banner_frame,
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
    menu_page.protocol("WM_DELETE_WINDOW", disable_close)


    def on_country_changed(selected_country):
        company_codes = db.get_company_codes(selected_country)

        dropdown_company_codes.set_values(company_codes)
        dropdown_company_codes.set("")
        when_selection_changes()

    # def load_quality_check():
    #     selected_country = dropdown_countries.get()
    #     selected_company_code = dropdown_company_codes.get()
    #     documents = db.get_sap_documents_based_on_country(selected_country, selected_company_code)
    #
    #     run_quality_check_details(
    #         quality_check_page,
    #         selected_country,
    #         selected_company_code,
    #         documents
    #     )

    def when_selection_changes(*_):
        nonlocal total_items, items_not_mine

        country = dropdown_countries.get()
        company_code = dropdown_company_codes.get()
        qc_status = dropdown_qc_status.get()
        vendor_type = dropdown_vendor_type.get()
        vendor_number = text_input_vendor_number.get().strip()

        print(f"QC Status selected: {qc_status}")

        total_items, items_not_mine = db.get_number_of_items_found_all(
        country = country,
        company_code = company_code,
        qc_status = qc_status,
        vendor_type = vendor_type,
        vendor_number = vendor_number)

        label_number_of_items_found.configure(text = f"Items to audit: {items_not_mine} ({total_items} in total)")


    def load_quality_check_items():
        country = dropdown_countries.get()
        company_code = dropdown_company_codes.get()
        qc_status = dropdown_qc_status.get()
        vendor_type = dropdown_vendor_type.get()
        vendor_number = text_input_vendor_number.get().strip()
        order_by = dropdown_order_by.get()

        first_selected_item = db.get_first_item_quality_check(
        country = country,
        company_code = company_code,
        qc_status = qc_status,
        vendor_type = vendor_type,
        vendor_number = vendor_number,
        order_by = order_by)

        print(country)
        print(company_code)
        print(vendor_number)
        run_quality_check_details(quality_check_page, first_selected_item, total_items, items_not_mine)



# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramki na stronie
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check = AppFrame(quality_check_page, width = 820, height = 470)
    frame_quality_check.place(x=90, y=90)

    label_quality_check_title = App_Label_Title(frame_quality_check, text="Load Quality check items", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=145, y=30)

    label_quality_check_subtitle = App_Label_Title(frame_quality_check, text="Select desired criteria to load items for audit", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_quality_check_subtitle.place(x=145, y=65)

    line_frame_bottom = ctk.CTkFrame(frame_quality_check, height=2, width=700, fg_color="#DDE2E7", corner_radius=0)
    line_frame_bottom.place(x=40, y=120)

    label_quality_check_country = App_Label_Title(frame_quality_check, text="Country", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_country.place(x=35, y=140)

    dropdown_countries = AppComboBox(frame_quality_check, width = 300, values=countries, command=on_country_changed)
    dropdown_countries.place(x=40, y=170)
    dropdown_countries.set("---")
    print(countries)

    label_quality_check_company_code = App_Label_Title(frame_quality_check, text="Company Code", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_company_code.place(x=35, y=220)

    dropdown_company_codes = AppComboBox(frame_quality_check, width = 300, values=["---"], command=when_selection_changes)
    dropdown_company_codes.place(x=40, y=250)

    label_quality_check_qc_status = App_Label_Title(frame_quality_check, text="QC status", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_qc_status.place(x=35, y=300)

    dropdown_qc_status = AppComboBox(frame_quality_check, width = 300, values=["All","Pending Verification","Verification Failed", "Requires confirmation"], command=when_selection_changes)
    dropdown_qc_status.place(x=40, y=330)

    label_quality_check_vendor_type = App_Label_Title(frame_quality_check, text="Vendor type", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_vendor_type.place(x=435, y=140)

    dropdown_vendor_type = AppComboBox(frame_quality_check, width = 300, values=["All","Internal","External"], command=when_selection_changes)
    dropdown_vendor_type.place(x=440, y=170)

    label_quality_check_vendor_number = App_Label_Title(frame_quality_check, text="Vendor number", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_vendor_number.place(x=435, y=220)

    text_input_vendor_number = App_Entry_Box(frame_quality_check, width = 300, fg_color = "white", justify="left")
    text_input_vendor_number.place(x=440, y=250)

    label_quality_check_vendor_type = App_Label_Title(frame_quality_check, text="Order by:", font= ("Open Sans", 14, "bold"), text_color = "#755a44")
    label_quality_check_vendor_type.place(x=435, y=300)

    dropdown_order_by = AppComboBox(frame_quality_check, width = 300, values=["Posting date - oldest first", "User - A to Z", "SAP Document number - lowest to highest", "Due date - oldest first", "EUR Amount - highest to lowest"])
    dropdown_order_by.place(x=440, y=330)

    button_load_items = Button_Brown(frame_quality_check, text= "⟳  Load items", command= load_quality_check_items)
    button_load_items.place(x=300, y=395)

    label_number_of_items_found = App_Label_Title(frame_quality_check, text="Items to audit: 0 (0 in total)", font= ("Open Sans", 14), text_color = "#8B7A6B")
    label_number_of_items_found.place(x=500, y=405)


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
        quality_check_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: quality_check_page.close_the_app(menu_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=880, y=5)
    quality_check_page.bind("<Escape>", lambda event: menu_page.close_the_app(main_page))

    # napis Logout
    logout_subtitle = ctk.CTkLabel(quality_check_page, text="Logout", font= ("Open Sans", 14), text_color = "white", fg_color = "#755a44")
    logout_subtitle.place(x=935, y=12)


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