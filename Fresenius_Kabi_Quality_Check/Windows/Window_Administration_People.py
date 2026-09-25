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
users_who_posted = db_admin.get_users_who_posted_but_are_not_visible()
users_with_sap_id_without_email = db_admin.get_users_from_users_with_no_email()
countries_where_new_joiner_is_added = []
countries_where_new_joiner_is_not_added = []


def run_window_administraton_people(adm_page, user_email_address):
    # Zamknij / ukryj główne okno
    adm_page.withdraw()   # albo destroy()
    # ctk.deactivate_automatic_dpi_awareness()

    # Utwórz nowe okno menu
    people_page = AppWindow(banner_text = "People Management", width=1100, height=600, x= 110, y = 30, fg_color="#F6F7F9")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(35, 35))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        people_page.banner_frame,
        image=power_off_icon,
        text="",
        width=35, height=35,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: people_page.close_the_app(adm_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=900, y=5)
    people_page.bind("<Escape>", lambda event: people_page.close_the_app(adm_page))

    logout_subtitle = ctk.CTkLabel(people_page, text="Logout", font= ("Open Sans", 14), text_color = "white", fg_color = "#755a44")
    logout_subtitle.place(x=955, y=12)

# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        people_page.withdraw()
        adm_page.deiconify()
        adm_page.lift()
        adm_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Return_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(20,30))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        people_page.banner_frame,
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
    people_page.protocol("WM_DELETE_WINDOW", disable_close)


# ---------------------------------------------------------------------------------------------------------
# funkcje top
# ---------------------------------------------------------------------------------------------------------

# funkcja użyta do pokazywania kontrolek w zależności od wyboru w pierwszej liście rozwijanej w top_left
    def when_first_selection_changes(choice):

        hide_widgets(
            *[w[0] for w in top_right_widgets],
            *[w[0] for w in middle_left_widgets],
            *[w[0] for w in middle_right_widgets],
            *[w[0] for w in bottom_left_widgets],
            *[w[0] for w in bottom_right_widgets]
        )

        if choice == "Modify user or create a new one":
            show_widgets(*top_right_widgets)

        elif choice == "Add users who posted invoices but are not included in the tables":
            show_widgets(*bottom_left_widgets)

        elif choice == "Update user's profile which has no e-mail address inserted":
            show_widgets(*bottom_right_widgets)


    def show_widgets(*widgets):
        for widget, x, y in widgets:
            widget.place(x=x, y=y)

    def hide_widgets(*widgets):
        for widget in widgets:
            widget.place_forget()


    def check_if_user_exists_top_right():

        typed_email_address_top_right = text_input_top_email_address.get()


        if db_admin.check_if_user_exists(typed_email_address_top_right):
            show_widgets(*middle_left_widgets)
            hide_widgets(*[w[0] for w in middle_right_widgets])
        else:
            show_widgets(*middle_right_widgets)
            hide_widgets(*[w[0] for w in middle_left_widgets])

        if db_admin.is_selected_employee_admin(typed_email_address_top_right):
            label_middle_left_admin_yes_no.configure(text="Yes")
        else:
            label_middle_left_admin_yes_no.configure(text="No")

        sap_id = db_admin.sap_id_for_selected_employee(typed_email_address_top_right)
        if db_admin.is_selected_employee_new_joiner(sap_id):
            label_middle_left_new_joiner_yes_no.configure(text="Yes")
        else:
            label_middle_left_new_joiner_yes_no.configure(text="No")

# utworzenie 2 list rozwijanych z krajami, do których user jest obecnie wpisany
        countries_where_new_joiner_is_added = db_admin.where_user_is_added_as_new_joiner(sap_id)
        dropdown_middle_left_countries_added.set_values(countries_where_new_joiner_is_added)
        dropdown_middle_left_countries_not_added.set_values(countries_where_new_joiner_is_added)

# utworzenie listy rozwijanej z krajami, do których user nie jest jeszcze wpisany
        countries_where_new_joiner_is_not_added = db_admin.get_countries_not_assigned_to_user(sap_id)
        dropdown_middle_left_new_joiner_added_to.set_values(countries_where_new_joiner_is_not_added)
        dropdown_middle_left_new_joiner_added_to.set("---")

        return typed_email_address_top_right, sap_id, countries_where_new_joiner_is_added


# ---------------------------------------------------------------------------------------------------------
# funkcje middle left
# ---------------------------------------------------------------------------------------------------------

    def grant_admin_access():

        typed_email_address_top_right, sap_id, countries_where_new_joiner_is_added = check_if_user_exists_top_right()
        db_admin.grant_admin_access(typed_email_address_top_right)

        updated_admin_rights = db_admin.is_selected_employee_admin(typed_email_address_top_right)
        if updated_admin_rights:
            label_middle_left_admin_yes_no.configure(text="Yes")
        else:
            label_middle_left_admin_yes_no.configure(text="No")


    def revoke_admin_access():

        typed_email_address_top_right, sap_id, countries_where_new_joiner_is_added = check_if_user_exists_top_right()
        db_admin.revoke_admin_access(typed_email_address_top_right)

        updated_admin_rights = db_admin.is_selected_employee_admin(typed_email_address_top_right)
        if updated_admin_rights:
            label_middle_left_admin_yes_no.configure(text="Yes")
        else:
            label_middle_left_admin_yes_no.configure(text="No")


    def add_new_joiner_to_new_country():

        typed_email_address_top_right, sap_id, countries_where_new_joiner_is_added = check_if_user_exists_top_right()
        country_to_add = dropdown_middle_left_new_joiner_added_to.get()

        db_admin.add_new_user_as_new_joiner(country_to_add, sap_id, user_email_address)

# po dodaniu rekordu należy odświeżyć pozostałe listy

        # najnowsza informacja o tym, czy user jest new joinerem
        if db_admin.is_selected_employee_new_joiner(sap_id):
            label_middle_left_new_joiner_yes_no.configure(text="Yes")
        else:
            label_middle_left_new_joiner_yes_no.configure(text="No")

        # odświeżenie 2 list rozwijanych z krajami, do których user jest obecnie wpisany
        countries_where_new_joiner_is_added = db_admin.where_user_is_added_as_new_joiner(sap_id)
        dropdown_middle_left_countries_added.set_values(countries_where_new_joiner_is_added)
        dropdown_middle_left_countries_not_added.set_values(countries_where_new_joiner_is_added)

        # odświeżenie listy rozwijanej z krajami, do których user nie jest jeszcze wpisany
        countries_where_new_joiner_is_not_added = db_admin.get_countries_not_assigned_to_user(sap_id)
        dropdown_middle_left_new_joiner_added_to.set_values(countries_where_new_joiner_is_not_added)
        dropdown_middle_left_new_joiner_added_to.set("---")


# ---------------------------------------------------------------------------------------------------------
# funkcje bottom left
# ---------------------------------------------------------------------------------------------------------

    def add_user_bottom_left():
        selected_sap_id = dropdown_bottom_left_sap_ids.get()
        typed_email_address = text_input_bottom_left_email_address.get()

        db_admin.create_user_who_posted_invoices(selected_sap_id, typed_email_address)

        text_input_bottom_left_email_address.delete(0, "end")

        updated_sap_ids_bottom_left = db_admin.get_users_who_posted_but_are_not_visible()
        dropdown_bottom_left_sap_ids.set_values(updated_sap_ids_bottom_left)
        dropdown_bottom_left_sap_ids.set("choose SAP ID")


# ---------------------------------------------------------------------------------------------------------
# funkcje bottom right
# ---------------------------------------------------------------------------------------------------------

    def update_user_bottom_right():
        selected_sap_id_bottom_right = dropdown_bottom_right_sap_ids.get()
        typed_email_address_bottom_right = text_input_bottom_right_email_address.get()

        db_admin.update_user_with_sap_id_but_no_email(selected_sap_id_bottom_right, typed_email_address_bottom_right)

        text_input_bottom_right_email_address.delete(0, "end")

        updated_sap_ids_bottom_right = db_admin.get_users_from_users_with_no_email()
        dropdown_bottom_right_sap_ids.set_values(updated_sap_ids_bottom_right)
        dropdown_bottom_right_sap_ids.set("choose SAP ID")


# ---------------------------------------------------------------------------------------------------------
# frame top_left
# ---------------------------------------------------------------------------------------------------------

    frame_top_left = AppFrame(people_page, height=70, width=495)
    frame_top_left.place(x=50, y=75)

    dropdown_first_selection = AppComboBox(frame_top_left, width = 450, command=when_first_selection_changes, values=("Modify user or create a new one", "Add users who posted invoices but are not included in the tables", "Update user's profile which has no e-mail address inserted"))
    dropdown_first_selection.place(x=20, y=15)
    dropdown_first_selection.set("What would you like to do?")


# ---------------------------------------------------------------------------------------------------------
# frame top_right
# ---------------------------------------------------------------------------------------------------------

    frame_top_right = AppFrame(people_page, height= 70, width= 495)
    frame_top_right.place(x=550, y=75)

    text_input_top_email_address = App_Entry_Box(frame_top_right, placeholder_text="--- enter full e-mail address ---", width = 300, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_top_email_address.place(x=20, y=15)

    button_check_user = Button_Brown(frame_top_right, text= "Check user   ✔", command=check_if_user_exists_top_right, height= 35, width=135, font= ("Open Sans", 16))
    button_check_user.place(x=330, y=15)

# ---------------------------------------------------------------------------------------------------------
# frame middle left part
# ---------------------------------------------------------------------------------------------------------

    frame_middle = AppFrame(people_page, height= 280, width= 1000)
    frame_middle.place(x=50, y=155)

    label_left_title = App_Label_Title(frame_middle, text="User exists", font= ("Open Sans", 18, "bold"), text_color = "#755a44")
    label_left_title.place(x=180, y=15)
    line_middle_left = ctk.CTkFrame(frame_middle, height=2, width=150, fg_color="#DDE2E7", corner_radius=0)
    line_middle_left.place(x=160, y=45)

    label_middle_left_is_admin = App_Label_Title(frame_middle, text="Admin?", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_is_admin.place(x=10, y=70)
    label_middle_left_admin_yes_no = App_Label_Title(frame_middle, text="Yes", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_admin_yes_no.place(x=110, y=70)
    button_middle_left_grant = Button_Brown(frame_middle, text= "Grant access", command=grant_admin_access, height= 35, width=135, font= ("Open Sans", 16))
    button_middle_left_grant.place(x=180, y=68)
    button_middle_left_remove = Button_Brown(frame_middle, text= "Revoke access", command=revoke_admin_access, height= 35, width=135, font= ("Open Sans", 16))
    button_middle_left_remove.place(x=330, y=68)

    label_middle_left_is_new_joiner = App_Label_Title(frame_middle, text="New joiner?", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_is_new_joiner.place(x=10, y=120)
    label_middle_left_new_joiner_yes_no = App_Label_Title(frame_middle, text="Yes", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_new_joiner_yes_no.place(x=110, y=120)
    label_middle_left_countries_added = App_Label_Title(frame_middle, text="Countries added:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_countries_added.place(x=178, y=120)
    dropdown_middle_left_countries_added = AppComboBox(frame_middle, width = 160, values=countries_where_new_joiner_is_added)
    dropdown_middle_left_countries_added.place(x=302, y=116)
    dropdown_middle_left_countries_added.set("---")

    label_middle_left_choose_country_to_add = App_Label_Title(frame_middle, text="Add as new joiner to:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_choose_country_to_add.place(x=10, y=170)
    dropdown_middle_left_new_joiner_added_to = AppComboBox(frame_middle, width = 160, values=countries_where_new_joiner_is_not_added)
    dropdown_middle_left_new_joiner_added_to.place(x=180, y=166)
    dropdown_middle_left_new_joiner_added_to.set("---")
    button_middle_left_add_nj = Button_Brown(frame_middle, text= "Add", command=add_new_joiner_to_new_country, height= 35, width=100, font= ("Open Sans", 16))
    button_middle_left_add_nj.place(x=360, y=166)

    label_middle_left_choose_country_to_remove = App_Label_Title(frame_middle, text="Remove new joiner from:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_left_choose_country_to_remove.place(x=10, y=220)
    dropdown_middle_left_countries_not_added = AppComboBox(frame_middle, width = 160, values=countries_where_new_joiner_is_added)
    dropdown_middle_left_countries_not_added.place(x=180, y=216)
    dropdown_middle_left_countries_not_added.set("---")
    button_middle_left_remove_nj = Button_Brown(frame_middle, text= "Remove", height= 35, width=100, font= ("Open Sans", 16))
    button_middle_left_remove_nj.place(x=360, y=216)


# linia pomiędzy 2 opcjami

    line_middle = ctk.CTkFrame(frame_middle, height=220, width=2, fg_color="#DDE2E7", corner_radius=0)
    line_middle.place(x=498, y=30)

# ---------------------------------------------------------------------------------------------------------
# frame middle right part
# ---------------------------------------------------------------------------------------------------------

    label_middle_right_title = App_Label_Title(frame_middle, text="User does not exist", font= ("Open Sans", 18, "bold"), text_color = "#755a44")
    label_middle_right_title.place(x=670, y=15)
    line_middle_right = ctk.CTkFrame(frame_middle, height=2, width=225, fg_color="#DDE2E7", corner_radius=0)
    line_middle_right.place(x=650, y=45)

    label_middle_right_sap_id = App_Label_Title(frame_middle, text="SAP ID:", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_right_sap_id.place(x=530, y=70)
    text_input_middle_right_sap_id = App_Entry_Box(frame_middle, placeholder_text="--- enter SAP ID ---", width = 200, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_middle_right_sap_id.place(x=670, y=67)

    label_middle_right_admin_rights = App_Label_Title(frame_middle, text="Grant admin rights?", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_right_admin_rights.place(x=530, y=120)
    dropdown_middle_right_admin_rights = AppComboBox(frame_middle, width = 125, values=("Yes","No"))
    dropdown_middle_right_admin_rights.place(x=675, y=116)
    dropdown_middle_right_admin_rights.set("---")

    label_middle_right_new_joiner = App_Label_Title(frame_middle, text="New joiner?", font= ("Open Sans", 14), text_color = "#8B7A6B", justify="center")
    label_middle_right_new_joiner.place(x=530, y=170)
    dropdown_middle_right_new_joiner = AppComboBox(frame_middle, width = 125, values=("Yes","No"))
    dropdown_middle_right_new_joiner.place(x=675, y=166)
    dropdown_middle_right_new_joiner.set("---")

    dropdown_middle_right_new_joiner_country = AppComboBox(frame_middle, width = 160, values=("Germany","France Vial"))
    dropdown_middle_right_new_joiner_country.place(x=810, y=166)
    dropdown_middle_right_new_joiner_country.set("Choose country")

    button_create_user = Button_Brown(frame_middle, text= "Create user", height= 35, width=135, font= ("Open Sans", 16))
    button_create_user.place(x=675, y=225)


# ---------------------------------------------------------------------------------------------------------
# frame bottom_left
# ---------------------------------------------------------------------------------------------------------

    frame_bottom_left = AppFrame(people_page, height= 120, width= 495)
    frame_bottom_left.place(x=50, y=445)

    label_bottom_left_title = App_Label_Title(frame_bottom_left, text="Users who posted invoices but are not added to the 'Users' table", font= ("Open Sans", 14), text_color = "#755a44")
    label_bottom_left_title.place(x=25, y=5)

    dropdown_bottom_left_sap_ids = AppComboBox(frame_bottom_left, values=users_who_posted, width = 150, height=30)
    dropdown_bottom_left_sap_ids.place(x=90, y=35)
    dropdown_bottom_left_sap_ids.set("choose SAP ID")

    text_input_bottom_left_email_address = App_Entry_Box(frame_bottom_left, placeholder_text="--- enter full e-mail address ---", width = 300, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_bottom_left_email_address.place(x=20, y=72)

    button_update_user_left = Button_Brown(frame_bottom_left, text= "Add user", command=add_user_bottom_left, height= 35, width=135, font= ("Open Sans", 16))
    button_update_user_left.place(x=340, y=50)

# ---------------------------------------------------------------------------------------------------------
# frame bottom_right
# ---------------------------------------------------------------------------------------------------------

    frame_bottom_right = AppFrame(people_page, height= 120, width= 495)
    frame_bottom_right.place(x=550, y=445)

    label_bottom_right_title = App_Label_Title(frame_bottom_right, text="Users with no e-mail address in the 'Users' table", font= ("Open Sans", 14), text_color = "#755a44")
    label_bottom_right_title.place(x=80, y=5)

    dropdown_bottom_right_sap_ids = AppComboBox(frame_bottom_right, width = 150, height=30, values=users_with_sap_id_without_email)
    dropdown_bottom_right_sap_ids.place(x=90, y=35)
    dropdown_bottom_right_sap_ids.set("choose SAP ID")

    text_input_bottom_right_email_address = App_Entry_Box(frame_bottom_right, placeholder_text="--- enter full e-mail address ---", width = 300, height= 35, fg_color = "white", justify="left", font= ("Open Sans", 14))
    text_input_bottom_right_email_address.place(x=20, y=72)

    button_update_user_right = Button_Brown(frame_bottom_right, text= "Update user", command=update_user_bottom_right, height= 35, width=135, font= ("Open Sans", 16))
    button_update_user_right.place(x=340, y=50)


# ---------------------------------------------------------------------------------------------------------
# konfiguracja widoczności kontrolek z poszczególnych obszarów
# ---------------------------------------------------------------------------------------------------------

    top_right_widgets = [
        (text_input_top_email_address, 20, 15),
        (button_check_user, 330, 15)
    ]

    middle_left_widgets = [
        (label_left_title, 180, 15),
        (line_middle_left, 160, 45),

        (label_middle_left_is_admin, 10, 70),
        (label_middle_left_admin_yes_no, 110, 70),
        (button_middle_left_grant, 180, 68),
        (button_middle_left_remove, 330, 68),

        (label_middle_left_is_new_joiner, 10, 120),
        (label_middle_left_new_joiner_yes_no, 110, 120),
        (label_middle_left_countries_added, 178, 120),
        (dropdown_middle_left_countries_added, 302, 116),

        (label_middle_left_choose_country_to_add, 10, 170),
        (dropdown_middle_left_new_joiner_added_to, 180, 166),
        (button_middle_left_add_nj, 360, 166),

        (label_middle_left_choose_country_to_remove, 10, 220),
        (dropdown_middle_left_countries_not_added, 180, 216),
        (button_middle_left_remove_nj, 360, 216),
    ]

    middle_right_widgets = [
        (label_middle_right_title, 670, 15),
        (line_middle_right, 650, 45),

        (label_middle_right_sap_id, 530, 70),
        (text_input_middle_right_sap_id, 670, 67),

        (label_middle_right_admin_rights, 530, 120),
        (dropdown_middle_right_admin_rights, 675, 116),

        (label_middle_right_new_joiner, 530, 170),
        (dropdown_middle_right_new_joiner, 675, 166),

        (dropdown_middle_right_new_joiner_country, 810, 166),
        (button_create_user, 675, 225)
    ]

    bottom_left_widgets = [
        (label_bottom_left_title, 25, 5),
        (dropdown_bottom_left_sap_ids, 90, 35),
        (text_input_bottom_left_email_address, 20, 72),
        (button_update_user_left, 340, 50)
    ]

    bottom_right_widgets = [
        (label_bottom_right_title, 80, 5),
        (dropdown_bottom_right_sap_ids, 90, 35),
        (text_input_bottom_right_email_address, 20, 72),
        (button_update_user_right, 340, 50)
    ]

    hide_widgets(
        *[w[0] for w in top_right_widgets],
        *[w[0] for w in middle_left_widgets],
        *[w[0] for w in middle_right_widgets],
        *[w[0] for w in bottom_left_widgets],
        *[w[0] for w in bottom_right_widgets]
    )

# ---------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    adm_page = ctk.CTk()
    adm_page.withdraw()

    run_window_administraton_people(adm_page, user_email_address=None)
    adm_page.mainloop()