import customtkinter as ctk
from PIL import Image

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppComboBox
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.App_Entry_Box import App_Entry_Box
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database
from Fresenius_Kabi_Quality_Check.AllClasses.App_Radio_Button import App_Radio_Button

db = Database()
countries = db.get_countries()

def run_quality_check_details(quality_check_page, first_selected_item):
    # Zamknij / ukryj główne okno
    quality_check_page.withdraw()   # albo destroy()

    # Utwórz nowe okno
    quality_check_page_details = AppWindow(banner_text = "Quality check audit", width=1100, height=610, x= 120, y = 25, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")

    print("Oto przekazany słownik:")
    print(first_selected_item)
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
# top frame + tytuły + elementy z first_selected_item
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_top = AppFrame(quality_check_page_details, width = 1000, height = 100)
    frame_quality_check_details_top.place(x=50, y=65)

    label_quality_check_title = App_Label_Title(frame_quality_check_details_top, text="ITEM DETAILS", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=20, y=8)

    label_quality_check_subtitle_1 = App_Label_Title(frame_quality_check_details_top, text="SAP Document number", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_1.place(x=20, y=40)

    label_quality_check_element_1 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_1.place(x=34, y=60)

    label_quality_check_subtitle_2 = App_Label_Title(frame_quality_check_details_top, text="Company code", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_2.place(x=150, y=40)

    label_quality_check_element_2 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_2.place(x=165, y=60)

    label_quality_check_subtitle_3 = App_Label_Title(frame_quality_check_details_top, text="Document date", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_3.place(x=250, y=40)

    label_quality_check_element_3 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_3.place(x=251, y=60)

    label_quality_check_subtitle_4 = App_Label_Title(frame_quality_check_details_top, text="Due date", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_4.place(x=360, y=40)

    label_quality_check_element_4 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_4.place(x=350, y=60)

    label_quality_check_subtitle_5 = App_Label_Title(frame_quality_check_details_top, text="Amount in local currency", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_5.place(x=442, y=40)

    label_quality_check_element_5 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_5.place(x=460, y=60)

    label_quality_check_subtitle_6 = App_Label_Title(frame_quality_check_details_top, text="Currency", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_6.place(x=580, y=40)

    label_quality_check_element_6 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_6.place(x=583, y=60)

    label_quality_check_subtitle_7 = App_Label_Title(frame_quality_check_details_top, text="Amount in EUR", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_7.place(x=650, y=40)

    label_quality_check_element_7 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_7.place(x=657, y=60)

    label_quality_check_subtitle_8 = App_Label_Title(frame_quality_check_details_top, text="Vendor number", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_8.place(x=750, y=40)

    label_quality_check_element_8 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_8.place(x=750, y=60)

    label_quality_check_subtitle_9 = App_Label_Title(frame_quality_check_details_top, text="Vendor type", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_9.place(x=850, y=40)

    label_quality_check_element_9 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_9.place(x=851, y=60)

    line_frame_top = ctk.CTkFrame(frame_quality_check_details_top, height=2, width=895, fg_color="#DDE2E7", corner_radius=0)
    line_frame_top.place(x=25, y=35)


    button_load_items = Button_Brown(quality_check_page_details, text= " Save and Next Item   ► ")
    button_load_items.place(x=450, y=540)


# ---------------------------------------------------------------------------------------------------------
# bottom frame + 16 kontrolek służących do audytowania + bullet pointy do kontrolek
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_bottom = AppFrame(quality_check_page_details, width=1000, height=350)
    frame_quality_check_details_bottom.place(x=50, y=175)

    label_quality_check_title_bottom = App_Label_Title(frame_quality_check_details_bottom, text="AUDIT CONTROLS", font=("Open Sans", 12, "bold"), text_color="#755a44")
    label_quality_check_title_bottom.place(x=20, y=8)

    line_frame_bottom = ctk.CTkFrame(frame_quality_check_details_bottom, height=2, width=895, fg_color="#DDE2E7", corner_radius=0)
    line_frame_bottom.place(x=25, y=35)

    frame_1 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_1.place(x=25, y=50)
    number_1 = App_Label_Title(frame_1, text="1", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_1.place(x=3, y=1)
    number_1_description = App_Label_Title(frame_quality_check_details_bottom, text="Doc. Legal Requirements", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_1_description.place(x=65, y=52)
    radio_result_1 = ctk.IntVar(value=-1)
    radio_ok_1 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_1, value=1)
    radio_ok_1.place(x=240, y=54)
    radio_not_ok_1 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_1, value=0)
    radio_not_ok_1.place(x=310, y=54)


    frame_2 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_2.place(x=25, y=85)
    number_2 = App_Label_Title(frame_2, text="2", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_2.place(x=3, y=1)
    number_2_description = App_Label_Title(frame_quality_check_details_bottom, text="Document Type", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_2_description.place(x=65, y=87)

    frame_3 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_3.place(x=25, y=120)
    number_3 = App_Label_Title(frame_3, text="3", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_3.place(x=3, y=1)
    number_3_description = App_Label_Title(frame_quality_check_details_bottom, text="Vendor", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_3_description.place(x=65, y=122)

    frame_4 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_4.place(x=25, y=155)
    number_4 = App_Label_Title(frame_4, text="4", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_4.place(x=3, y=1)
    number_4_description = App_Label_Title(frame_quality_check_details_bottom, text="Document Date", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_4_description.place(x=65, y=157)

    frame_5 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_5.place(x=25, y=190)
    number_5 = App_Label_Title(frame_5, text="5", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_5.place(x=3, y=1)
    number_5_description = App_Label_Title(frame_quality_check_details_bottom, text="Reference", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_5_description.place(x=65, y=192)

    frame_6 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_6.place(x=25, y=225)
    number_6 = App_Label_Title(frame_6, text="6", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_6.place(x=3, y=1)
    number_6_description = App_Label_Title(frame_quality_check_details_bottom, text="Amounts", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_6_description.place(x=65, y=227)

    frame_7 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_7.place(x=25, y=260)
    number_7 = App_Label_Title(frame_7, text="7", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_7.place(x=3, y=1)
    number_7_description = App_Label_Title(frame_quality_check_details_bottom, text="Currency", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_7_description.place(x=65, y=262)

    frame_8 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_8.place(x=25, y=295)
    number_8 = App_Label_Title(frame_8, text="8", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_8.place(x=3, y=1)
    number_8_description = App_Label_Title(frame_quality_check_details_bottom, text="Payment details", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_8_description.place(x=65, y=297)

    line_frame_middle = ctk.CTkFrame(frame_quality_check_details_bottom, height=200, width=2, fg_color="#E9EDF1", corner_radius=0)
    line_frame_middle.place(x=420, y=50)

    frame_9 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB")
    frame_9.place(x=445, y=50)
    number_9 = App_Label_Title(frame_9, text="9", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_9.place(x=3, y=1)




# ---------------------------------------------------------------------------------------------------------
# zmienne zaciągnięte z first_selected_item służące do wyświetlania informacji na górze okna
# ---------------------------------------------------------------------------------------------------------

    key_value_for_database = first_selected_item["Key_value_for_database"]
    sap_document_number = first_selected_item["Document_number_SAP"]
    company_code = first_selected_item["Company_code"]
    document_date = first_selected_item["Document_date"]
    due_date = first_selected_item["Due_date"]
    amount_in_local_currency = f"{float(first_selected_item['Amount_local']):,.2f}"
    currency = first_selected_item["Currency"]
    amount_in_eur = f"{float(first_selected_item['Amount_EUR']):,.2f}"
    vendor_number = first_selected_item["Vendor_number"]
    vendor_type = first_selected_item["Internal_external_vendor"]

    label_quality_check_element_1.configure(text=sap_document_number)
    label_quality_check_element_2.configure(text=company_code)
    label_quality_check_element_3.configure(text=document_date)
    label_quality_check_element_4.configure(text=due_date)
    label_quality_check_element_5.configure(text=amount_in_local_currency)
    label_quality_check_element_6.configure(text=currency)
    label_quality_check_element_7.configure(text=amount_in_eur)
    label_quality_check_element_8.configure(text=vendor_number)
    label_quality_check_element_9.configure(text=vendor_type)



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