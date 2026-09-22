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

def run_window_administraton_limit(adm_page, user_email_address):
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


    def on_country_changed(selected_country):
        company_codes = db.get_company_codes(selected_country)

        dropdown_company_codes.set_values(company_codes)
        dropdown_company_codes.set("")

        text_input_category_1.delete(0, "end")
        text_input_category_2.delete(0, "end")
        text_input_category_3.delete(0, "end")


    def when_selection_changes_admin(*_):
        global country, company_code, current_monthly_posted_documents, current_amount_limit, current_new_hire_percentage

        country = dropdown_countries.get()
        company_code = dropdown_company_codes.get()

        results = db_admin.get_limits_based_on_selected_country_and_company_code(
        country = country,
        company_code = company_code)

        if results:
            row = results[0]

            text_input_category_1.delete(0, "end")
            text_input_category_1.insert(0, str(row["monthly_posted_documents"]))

            text_input_category_2.delete(0, "end")
            text_input_category_2.insert(0, str(int(row["amount_limit"])))

            text_input_category_3.delete(0, "end")
            text_input_category_3.insert(0, str(row["new_hire_percentage"]))

        current_monthly_posted_documents = str(row["monthly_posted_documents"])
        current_amount_limit = str(int(row["amount_limit"]))
        current_new_hire_percentage = str(row["new_hire_percentage"])

        print(country)
        print(company_code)
        return country, company_code, current_monthly_posted_documents, current_amount_limit, current_new_hire_percentage


# funkcja aktualizująca obecny rekord (zmieniająca go na Inactive i dodająca datę końcową) oraz dodająca zupełnie nowy rekord do tabeli
    def save_changes_button():

        print(country)
        print(company_code)
        print(current_monthly_posted_documents)
        print(current_amount_limit)
        print(current_new_hire_percentage)

        new_monthly_posted_documents = text_input_category_1.get()
        new_amount_limit = float(text_input_category_2.get())
        new_new_hire_percentage = text_input_category_3.get()

        print(new_monthly_posted_documents)
        print(new_amount_limit)
        print(new_new_hire_percentage)

        db_admin.update_row_with_limits(user_email_address, country, company_code, new_monthly_posted_documents, new_amount_limit, new_new_hire_percentage)

        dropdown_countries.set("---")
        dropdown_company_codes.set("---")
        text_input_category_1.delete(0, "end")
        text_input_category_2.delete(0, "end")
        text_input_category_3.delete(0, "end")


# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    label_top_title = App_Label_Title(limit_page, text="Limit Management", font= ("Open Sans", 24, "bold"), text_color = "#755a44", fg_color="#F6F7F9")
    label_top_title.place(x=435, y=90)

    label_top_subtitle = App_Label_Title(limit_page, text="View and configure all thresholds and limits", font= ("Open Sans", 14), text_color = "#8B7A6B", fg_color="#F6F7F9")
    label_top_subtitle.place(x=400, y=120)

# ---------------------------------------------------------------------------------------------------------
# ramki i podpisy do ramek na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    frame_step_1 = AppFrame(limit_page, height= 250)
    frame_step_1.place(x=80, y=170)

    label_step_1_title = App_Label_Title(frame_step_1, text="STEP 1", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_step_1_title.place(x=100, y=20)

    label_step_1_subtitle = App_Label_Title(frame_step_1, text="Choose country and company code", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_1_subtitle.place(x=30, y=50)

    dropdown_countries = AppComboBox(frame_step_1, width = 260, values=countries, command=on_country_changed)
    dropdown_countries.place(x=20, y=100)
    dropdown_countries.set("---")

    dropdown_company_codes = AppComboBox(frame_step_1, width = 260, values=["---"], command=when_selection_changes_admin)
    dropdown_company_codes.place(x=20, y=170)

# ---------------------------------------------------------------------------------------------------------

    frame_step_2 = AppFrame(limit_page, height= 250)
    frame_step_2.place(x=395, y=170)

    label_step_2_title = App_Label_Title(frame_step_2, text="STEP 2", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_step_2_title.place(x=100, y=20)

    label_step_2_subtitle = App_Label_Title(frame_step_2, text="Check and modify any threshold", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_2_subtitle.place(x=43, y=50)

    line_bottom = ctk.CTkFrame(frame_step_2, height=2, width=240, fg_color="#DDE2E7", corner_radius=0)
    line_bottom.place(x=30, y=85)

    label_step_2_category_1 = App_Label_Title(frame_step_2, text="% of posted documents:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_2_category_1.place(x=20, y=100)
    text_input_category_1 = App_Entry_Box(frame_step_2, width = 80, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_category_1.place(x=190, y=98)

    label_step_2_category_2 = App_Label_Title(frame_step_2, text="Amount limit:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_2_category_2.place(x=20, y=140)
    text_input_category_2 = App_Entry_Box(frame_step_2, width = 80, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_category_2.place(x=190, y=138)

    label_step_2_category_3 = App_Label_Title(frame_step_2, text="New hire percentage:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_2_category_3.place(x=20, y=180)
    text_input_category_3 = App_Entry_Box(frame_step_2, width = 80, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_category_3.place(x=190, y=178)


# ---------------------------------------------------------------------------------------------------------

    frame_step_3 = AppFrame(limit_page, height= 250)
    frame_step_3.place(x=710, y=170)

    label_step_3_title = App_Label_Title(frame_step_3, text="STEP 3", font= ("Open Sans", 22, "bold"), text_color = "#755a44")
    label_step_3_title.place(x=100, y=20)

    label_step_3_subtitle = App_Label_Title(frame_step_3, text="Save all the changes", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_step_3_subtitle.place(x=70, y=50)

    button_load_items = Button_Brown(frame_step_3, text= "💾  Save changes", command=save_changes_button)
    button_load_items.place(x=63, y=127)

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    adm_page = ctk.CTk()
    adm_page.withdraw()

    run_window_administraton_limit(adm_page, user_email_address)
    adm_page.mainloop()