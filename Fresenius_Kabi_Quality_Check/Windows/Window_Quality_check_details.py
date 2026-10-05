import customtkinter as ctk
from PIL import Image
from time import sleep

from Fresenius_Kabi_Quality_Check.AllClasses.Button_Standard import Button_Standard
from Fresenius_Kabi_Quality_Check.AllClasses.App_Window import AppWindow
from Fresenius_Kabi_Quality_Check.AllClasses.App_Frame import AppFrame
from Fresenius_Kabi_Quality_Check.AllClasses.App_Label_Title import App_Label_Title
from Fresenius_Kabi_Quality_Check.AllClasses.App_Dropdown import AppComboBox
from Fresenius_Kabi_Quality_Check.AllClasses.Button_Brown import Button_Brown
from Fresenius_Kabi_Quality_Check.AllClasses.App_Entry_Box import App_Entry_Box
from Fresenius_Kabi_Quality_Check.AllClasses.App_Text_Box import  App_Text_Box
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database import Database
from Fresenius_Kabi_Quality_Check.AllClasses.App_Database_QC import Database_QC
from Fresenius_Kabi_Quality_Check.AllClasses.App_Radio_Button import App_Radio_Button
from Fresenius_Kabi_Quality_Check.AllClasses.Resource_Path import resource_path
from Fresenius_Kabi_Quality_Check.Windows.Window_Administration_Limit import db_admin

db = Database()
db_qc = Database_QC()
countries = db.get_countries()

def run_quality_check_details(quality_check_page,
                              sap_id, admin_role, user_email_address, first_selected_item, total_items, items_not_mine, status_number,
                              country, company_code, qc_status, vendor_type, vendor_number, order_by, refresh_main_window):
    print("OPENING NEW DETAILS WINDOW")

    # Zamknij / ukryj główne okno
    quality_check_page.withdraw()   # albo destroy()

    # Utwórz nowe okno
    quality_check_page_details = AppWindow(banner_text = "Quality check audit", width=1100, height=610, x= 120, y = 25, fg_color="#F6F7F9")

    print(f"SAP ID used in quality_check_details: {sap_id}")
    print(f"Logged user admin rights: {admin_role}")
    print(f"Logged user email address: {user_email_address}")

    sap_id_who_posted_invoice = first_selected_item['User_name']
    print(f"SAP ID who posted invoice: {sap_id_who_posted_invoice}")

    print(f"Oto przekazany słownik: {first_selected_item}")
    print(f"Oto przekazane total items: {total_items}")
    print(f"Oto przekazane items not mine: {items_not_mine}")
    print(f"Oto przekazane status number: {status_number}")
    print(f"Oto przekazane country: {country}")
    print(f"Oto przekazane company code: {company_code}")
    print(f"Oto przekazane qc status: {qc_status}")
    print(f"Oto przekazane vendor type: {vendor_type}")
    print(f"Oto przekazane vendor number: {vendor_number}")
    print(f"Oto przekazane order by: {order_by}")

    comment_dedicated_to_selected_item = first_selected_item['First_comment']
    follow_up_dedicated_to_selected_item = first_selected_item['Second_comment']

    control_statuses = first_selected_item['Controls']
    control_statuses_list = control_statuses.split(",")
    print(control_statuses_list)



# ---------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę return- przycisk powracający do poprzedniego okna
    def return_to_previous_window():
        quality_check_page_details.destroy()

        refresh_main_window()
        # db.get_number_of_items_found_all(
        #     sap_id=sap_id,
        #     country=country,
        #     company_code=company_code,
        #     qc_status=qc_status,
        #     vendor_type=vendor_type,
        #     vendor_number=vendor_number)

        quality_check_page.deiconify()
        quality_check_page.lift()
        quality_check_page.focus_force()

    # 1. Wczytanie obrazu z pliku
    image = Image.open(resource_path("Images/Return_icon.png"))
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


# Funkcja kopiująca bieżący SAP Document number
    def copy_to_clipboard(text):
        quality_check_page_details.clipboard_clear()
        quality_check_page_details.clipboard_append(str(text))
        quality_check_page_details.update_idletasks()

        original_text = label_quality_check_element_1.cget("text")
        label_quality_check_element_1.configure(text="✓ Copied")

        quality_check_page_details.after(1000,lambda: label_quality_check_element_1.configure(text=original_text))


# ---------------------------------------------------------------------------------


# funkcja sprawdzająca dostępność przycisku Save & next

    def check_save_button(event=None):
        can_save = False

        if str(status_number) in ["1", "2"]:
            can_save = (sap_id != sap_id_who_posted_invoice)
        elif str(status_number) == "4":
            can_save = (admin_role == "admin")

        if not can_save:
            button_save_and_next.configure(state="disabled")
            return

        if str(status_number) == "1":
            all_completed = all(
                result.get() in [1, 2]
                for result in [
                    radio_result_1,
                    radio_result_2,
                    radio_result_3,
                    radio_result_4,
                    radio_result_5,
                    radio_result_6,
                    radio_result_7,
                    radio_result_8,
                    radio_result_9,
                    radio_result_10,
                    radio_result_11,
                    radio_result_12,
                    radio_result_13
                ]
            )

            if all_completed:
                button_save_and_next.configure(state="normal")
            else:
                button_save_and_next.configure(state="disabled")

        elif str(status_number) == "2":

            follow_up_text = text_box_follow_up.get("1.0", "end-1c").strip()

            if len(follow_up_text) > 0:
                button_save_and_next.configure(state="normal")
            else:
                button_save_and_next.configure(state="disabled")

        elif str(status_number) == "4":
            button_save_and_next.configure(state="normal")

        else:
            button_save_and_next.configure(state="disabled")


# -------------------------------------------------------------------------------------------------------------------
# funkcja uruchamiana po kliknięciu na jeden z 3 przycisków, sprawia, że okno ponownie otwiera się z nowym rekordem
# -------------------------------------------------------------------------------------------------------------------

    def reload_quality_check_items():

        new_first_selected_item = db.get_first_item_quality_check(
            sap_id=sap_id,
            country=country,
            company_code=company_code,
            qc_status=qc_status,
            vendor_type=vendor_type,
            vendor_number=vendor_number,
            order_by=order_by
        )

        print("NEW ITEM:")
        print(new_first_selected_item)

        if not new_first_selected_item:
            print("No items found for selected criteria")
            quality_check_page_details.destroy()
            quality_check_page.deiconify()
            quality_check_page.lift()
            quality_check_page.focus_force()
            return

        new_status_number = new_first_selected_item["Verified"]

        new_total_items, new_items_not_mine = db.get_number_of_items_found_all(
            sap_id=sap_id,
            country=country,
            company_code=company_code,
            qc_status=qc_status,
            vendor_type=vendor_type,
            vendor_number=vendor_number
        )

        quality_check_page_details.destroy()

        run_quality_check_details(
            quality_check_page=quality_check_page,
            sap_id=sap_id,
            admin_role=admin_role,
            user_email_address=user_email_address,
            first_selected_item=new_first_selected_item,
            total_items=new_total_items,
            items_not_mine=new_items_not_mine,
            status_number=new_status_number,
            country=country,
            company_code=company_code,
            qc_status=qc_status,
            vendor_type=vendor_type,
            vendor_number=vendor_number,
            order_by=order_by,
            refresh_main_window=refresh_main_window
        )


# ---------------------------------------------------------------------------------------------------------
# funkcje uruchamiające przyciski "Save & next", "Reject" oraz "Error not valid"
# ---------------------------------------------------------------------------------------------------------

    def proceed_save_and_next_button():

        any_error = any(
            result.get() == 2
            for result in [
                radio_result_1,
                radio_result_2,
                radio_result_3,
                radio_result_4,
                radio_result_5,
                radio_result_6,
                radio_result_7,
                radio_result_8,
                radio_result_9,
                radio_result_10,
                radio_result_11,
                radio_result_12,
                radio_result_13
            ]
        )

        controls_column = ",".join([
            str(radio_result_1.get()),
            str(radio_result_2.get()),
            str(radio_result_3.get()),
            str(radio_result_4.get()),
            str(radio_result_5.get()),
            str(radio_result_6.get()),
            str(radio_result_7.get()),
            str(radio_result_8.get()),
            str(radio_result_9.get()),
            str(radio_result_10.get()),
            str(radio_result_11.get()),
            str(radio_result_12.get()),
            str(radio_result_13.get())
        ])

        if status_number == "1" and not any_error:
            db_qc.change_1_to_3(user_email_address, first_selected_item['Key_value_for_database'], controls_column)
        if status_number == "1" and any_error:
            db_qc.change_1_to_2(user_email_address, first_selected_item['Key_value_for_database'], controls_column)
        if status_number == "2":
            db_qc.change_2_to_4(user_email_address, first_selected_item['Key_value_for_database'])
        if status_number == "4":
            db_qc.change_4_to_5(user_email_address, first_selected_item['Key_value_for_database'])

        reload_quality_check_items()


    def proceed_reject_button():
        db_qc.change_4_to_2(user_email_address, first_selected_item['Key_value_for_database'])
        reload_quality_check_items()

    def proceed_error_not_valid_button():
        db_qc.change_4_to_3(user_email_address, first_selected_item['Key_value_for_database'])
        reload_quality_check_items()



# ---------------------------------------------------------------------------------------------------------
# top frame + tytuły + elementy z first_selected_item
# ---------------------------------------------------------------------------------------------------------

    frame_quality_check_details_top = AppFrame(quality_check_page_details, width = 1000, height = 100)
    frame_quality_check_details_top.place(x=50, y=65)

    label_number_of_items_found = App_Label_Title(frame_quality_check_details_top, text=f"Items to audit: {items_not_mine} ({total_items} in total)", font= ("Open Sans", 12), text_color = "#8B7A6B")
    label_number_of_items_found.place(x=750, y=8)
    label_number_of_items_found.configure(text=f"Items to audit: {items_not_mine} ({total_items} in total)")

    label_quality_check_title = App_Label_Title(frame_quality_check_details_top, text="ITEM DETAILS", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_title.place(x=20, y=8)

    label_quality_check_subtitle_1 = App_Label_Title(frame_quality_check_details_top, text="SAP Document number", font= ("Open Sans", 10), text_color = "#8B7A6B")
    label_quality_check_subtitle_1.place(x=20, y=40)

    label_quality_check_element_1 = App_Label_Title(frame_quality_check_details_top, text="", font= ("Open Sans", 12, "bold"), text_color = "#755a44")
    label_quality_check_element_1.place(x=34, y=60)
    label_quality_check_element_1.configure(cursor="hand2")

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


# -------------------------------------------------------------------------------------------------------------------
# domyślne ustawienia związane z 3 przyciskami u dołu ekranu
# -------------------------------------------------------------------------------------------------------------------

# ustawienie buttona save and next + konfiguracja normal/disable

    button_save_and_next = Button_Brown(quality_check_page_details, text= " Save and Next Item   ► ", command=proceed_save_and_next_button)
    button_save_and_next.place(x=380, y=540)

# ustawienie przycisku "Reject"

    button_reject = Button_Standard(quality_check_page_details, text="Reject", command=proceed_reject_button, fg_color="#A94442", hover_color="#8B3837", text_color="white")
    button_reject.place(x=650, y=540)

    if (str(status_number) in ["1", "2"] or (str(status_number) == "4" and admin_role != "admin")):
        button_reject.configure(state="disabled")
    else:
        button_reject.configure(state="normal")

# ustawienie przycisku "Error not valid"

    button_error_not_valid = Button_Standard(quality_check_page_details, text= "Error not valid", command=proceed_error_not_valid_button)
    button_error_not_valid.place(x=820, y=540)

    if (str(status_number) in ["1", "2"] or (str(status_number) == "4" and admin_role != "admin")):
        button_error_not_valid.configure(state="disabled")
    else:
        button_error_not_valid.configure(state="normal")


# -------------------------------------------------------------------------------------------------------------------
# bottom frame + 13 kontrolek służących do audytowania + bullet pointy do kontrolek + text inputy do komentarzy
# -------------------------------------------------------------------------------------------------------------------

    frame_quality_check_details_bottom = AppFrame(quality_check_page_details, width=1000, height=350)
    frame_quality_check_details_bottom.place(x=50, y=175)

    label_quality_check_title_bottom = App_Label_Title(frame_quality_check_details_bottom, text="AUDIT CONTROLS", font=("Open Sans", 12, "bold"), text_color="#755a44")
    label_quality_check_title_bottom.place(x=20, y=8)

    line_frame_bottom = ctk.CTkFrame(frame_quality_check_details_bottom, height=2, width=895, fg_color="#DDE2E7", corner_radius=0)
    line_frame_bottom.place(x=25, y=35)

    frame_1 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_1.place(x=25, y=50)
    number_1 = App_Label_Title(frame_1, text="1", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_1.place(relx=0.5, rely=0.5, anchor="center")
    number_1_description = App_Label_Title(frame_quality_check_details_bottom, text="Doc. Legal Requirements", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_1_description.place(x=65, y=52)
    radio_result_1 = ctk.IntVar(value=-1)
    radio_ok_1 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_1, value=1, command=check_save_button)
    radio_ok_1.place(x=240, y=54)
    radio_not_ok_1 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_1, value=2, command=check_save_button)
    radio_not_ok_1.place(x=310, y=54)

    frame_2 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_2.place(x=25, y=85)
    number_2 = App_Label_Title(frame_2, text="2", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_2.place(relx=0.5, rely=0.5, anchor="center")
    number_2_description = App_Label_Title(frame_quality_check_details_bottom, text="Document Type", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_2_description.place(x=65, y=87)
    radio_result_2 = ctk.IntVar(value=-1)
    radio_ok_2 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_2, value=1, command=check_save_button)
    radio_ok_2.place(x=240, y=89)
    radio_not_ok_2 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_2, value=2, command=check_save_button)
    radio_not_ok_2.place(x=310, y=89)

    frame_3 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_3.place(x=25, y=120)
    number_3 = App_Label_Title(frame_3, text="3", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_3.place(relx=0.5, rely=0.5, anchor="center")
    number_3_description = App_Label_Title(frame_quality_check_details_bottom, text="Vendor", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_3_description.place(x=65, y=122)
    radio_result_3 = ctk.IntVar(value=-1)
    radio_ok_3 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_3, value=1, command=check_save_button)
    radio_ok_3.place(x=240, y=124)
    radio_not_ok_3 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_3, value=2, command=check_save_button)
    radio_not_ok_3.place(x=310, y=124)

    frame_4 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_4.place(x=25, y=155)
    number_4 = App_Label_Title(frame_4, text="4", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_4.place(relx=0.5, rely=0.5, anchor="center")
    number_4_description = App_Label_Title(frame_quality_check_details_bottom, text="Document Date", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_4_description.place(x=65, y=157)
    radio_result_4 = ctk.IntVar(value=-1)
    radio_ok_4 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_4, value=1, command=check_save_button)
    radio_ok_4.place(x=240, y=159)
    radio_not_ok_4 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_4, value=2, command=check_save_button)
    radio_not_ok_4.place(x=310, y=159)

    frame_5 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_5.place(x=25, y=190)
    number_5 = App_Label_Title(frame_5, text="5", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_5.place(relx=0.5, rely=0.5, anchor="center")
    number_5_description = App_Label_Title(frame_quality_check_details_bottom, text="Reference", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_5_description.place(x=65, y=192)
    radio_result_5 = ctk.IntVar(value=-1)
    radio_ok_5 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_5, value=1, command=check_save_button)
    radio_ok_5.place(x=240, y=194)
    radio_not_ok_5 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_5, value=2, command=check_save_button)
    radio_not_ok_5.place(x=310, y=194)

    frame_6 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_6.place(x=25, y=225)
    number_6 = App_Label_Title(frame_6, text="6", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_6.place(relx=0.5, rely=0.5, anchor="center")
    number_6_description = App_Label_Title(frame_quality_check_details_bottom, text="Amounts", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_6_description.place(x=65, y=227)
    radio_result_6 = ctk.IntVar(value=-1)
    radio_ok_6 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_6, value=1, command=check_save_button)
    radio_ok_6.place(x=240, y=229)
    radio_not_ok_6 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_6, value=2, command=check_save_button)
    radio_not_ok_6.place(x=310, y=229)

    frame_7 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_7.place(x=25, y=260)
    number_7 = App_Label_Title(frame_7, text="7", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_7.place(relx=0.5, rely=0.5, anchor="center")
    number_7_description = App_Label_Title(frame_quality_check_details_bottom, text="Currency", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_7_description.place(x=65, y=262)
    radio_result_7 = ctk.IntVar(value=-1)
    radio_ok_7 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_7, value=1, command=check_save_button)
    radio_ok_7.place(x=240, y=264)
    radio_not_ok_7 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_7, value=2, command=check_save_button)
    radio_not_ok_7.place(x=310, y=264)

    frame_8 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_8.place(x=25, y=295)
    number_8 = App_Label_Title(frame_8, text="8", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_8.place(relx=0.5, rely=0.5, anchor="center")
    number_8_description = App_Label_Title(frame_quality_check_details_bottom, text="Payment details", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_8_description.place(x=65, y=297)
    radio_result_8 = ctk.IntVar(value=-1)
    radio_ok_8 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_8, value=1, command=check_save_button)
    radio_ok_8.place(x=240, y=299)
    radio_not_ok_8 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_8, value=2, command=check_save_button)
    radio_not_ok_8.place(x=310, y=299)




    line_frame_middle = ctk.CTkFrame(frame_quality_check_details_bottom, height=175, width=2, fg_color="#E9EDF1", corner_radius=0)
    line_frame_middle.place(x=420, y=50)

    frame_9 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_9.place(x=445, y=50)
    number_9 = App_Label_Title(frame_9, text="9", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_9.place(relx=0.5, rely=0.5, anchor="center")
    number_9_description = App_Label_Title(frame_quality_check_details_bottom, text="Payment Terms", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_9_description.place(x=485, y=52)
    radio_result_9 = ctk.IntVar(value=-1)
    radio_ok_9 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_9, value=1, command=check_save_button)
    radio_ok_9.place(x=660, y=54)
    radio_not_ok_9 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_9, value=2, command=check_save_button)
    radio_not_ok_9.place(x=730, y=54)

    frame_10 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_10.place(x=445, y=85)
    number_10 = App_Label_Title(frame_10, text="10", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_10.place(relx=0.5, rely=0.5, anchor="center")
    number_10_description = App_Label_Title(frame_quality_check_details_bottom, text="Text fields", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_10_description.place(x=485, y=87)
    radio_result_10 = ctk.IntVar(value=-1)
    radio_ok_10 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_10, value=1, command=check_save_button)
    radio_ok_10.place(x=660, y=89)
    radio_not_ok_10 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_10, value=2, command=check_save_button)
    radio_not_ok_10.place(x=730, y=89)

    frame_11 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_11.place(x=445, y=120)
    number_11 = App_Label_Title(frame_11, text="11", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_11.place(relx=0.5, rely=0.5, anchor="center")
    number_11_description = App_Label_Title(frame_quality_check_details_bottom, text="PO/NonPO Coding", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_11_description.place(x=485, y=122)
    radio_result_11 = ctk.IntVar(value=-1)
    radio_ok_11 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_11, value=1, command=check_save_button)
    radio_ok_11.place(x=660, y=124)
    radio_not_ok_11 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_11, value=2, command=check_save_button)
    radio_not_ok_11.place(x=730, y=124)

    frame_12 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_12.place(x=445, y=155)
    number_12 = App_Label_Title(frame_12, text="12", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_12.place(relx=0.5, rely=0.5, anchor="center")
    number_12_description = App_Label_Title(frame_quality_check_details_bottom, text="Tax Data", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_12_description.place(x=485, y=157)
    radio_result_12 = ctk.IntVar(value=-1)
    radio_ok_12 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_12, value=1, command=check_save_button)
    radio_ok_12.place(x=660, y=159)
    radio_not_ok_12 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_12, value=2, command=check_save_button)
    radio_not_ok_12.place(x=730, y=159)

    frame_13 = AppFrame(frame_quality_check_details_bottom, width=32, height=32, fg_color = "#E4DFDB", corner_radius=5)
    frame_13.place(x=445, y=190)
    number_13 = App_Label_Title(frame_13, text="13", font=("Open Sans", 13, "bold"), text_color="#755a44", fg_color = "transparent")
    number_13.place(relx=0.5, rely=0.5, anchor="center")
    number_13_description = App_Label_Title(frame_quality_check_details_bottom, text="Documentation", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    number_13_description.place(x=485, y=192)
    radio_result_13 = ctk.IntVar(value=-1)
    radio_ok_13 = App_Radio_Button(frame_quality_check_details_bottom, text="OK", variable=radio_result_13, value=1, command=check_save_button)
    radio_ok_13.place(x=660, y=194)
    radio_not_ok_13 = App_Radio_Button(frame_quality_check_details_bottom, text="NOT OK", variable=radio_result_13, value=2, command=check_save_button)
    radio_not_ok_13.place(x=730, y=194)


# ustawienie normal/disable dla wszystkich radio buttons
    all_radio_buttons = [
        radio_ok_1, radio_not_ok_1,
        radio_ok_2, radio_not_ok_2,
        radio_ok_3, radio_not_ok_3,
        radio_ok_4, radio_not_ok_4,
        radio_ok_5, radio_not_ok_5,
        radio_ok_6, radio_not_ok_6,
        radio_ok_7, radio_not_ok_7,
        radio_ok_8, radio_not_ok_8,
        radio_ok_9, radio_not_ok_9,
        radio_ok_10, radio_not_ok_10,
        radio_ok_11, radio_not_ok_11,
        radio_ok_12, radio_not_ok_12,
        radio_ok_13, radio_not_ok_13
    ]

    state = "disabled" if str(status_number) in ["2", "4"] else "normal"

    for radio in all_radio_buttons:
        radio.configure(state=state)


# ustawienie wartości odpowiadających first_selected_item na początku, kiedy wyświetla się okno aplikacji
    radio_variables = [
        radio_result_1,
        radio_result_2,
        radio_result_3,
        radio_result_4,
        radio_result_5,
        radio_result_6,
        radio_result_7,
        radio_result_8,
        radio_result_9,
        radio_result_10,
        radio_result_11,
        radio_result_12,
        radio_result_13
    ]

    for i, status in enumerate(control_statuses_list):
        radio_variables[i].set(int(status))

# -----------------------------------------------------------------------------------
# pola na dole okna aplikacji: comment i follow up
# -----------------------------------------------------------------------------------

    text_box_comment = App_Text_Box(frame_quality_check_details_bottom, width = 270, height = 85, fg_color = "white", max_length=170)
    text_box_comment.place(x=445, y=250)
    text_box_comment._textbox.configure(pady = 12)

    text_box_comment.set_text(comment_dedicated_to_selected_item)

    label_comment = App_Label_Title(frame_quality_check_details_bottom, text="Comment:", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    label_comment.place(x=485, y=235)

    if ((str(status_number) == "1" and sap_id == sap_id_who_posted_invoice)
            or (str(status_number) == "2")
            or (str(status_number) == "4" and admin_role != "admin")):
        text_box_comment.configure(state="disabled", fg_color="#E5E5E5", text_color="#808080")
        label_comment.configure(text_color="#9AA3AD")
    else:
        text_box_comment.configure(state="normal", fg_color="white", text_color="black")
        label_comment.configure(text_color="#755A44")

    # if str(status_number) in ["2", "4"]:
    #     text_box_comment.configure(state="disabled",fg_color="#E5E5E5", text_color="#808080")
    #     label_comment.configure(text_color="#9AA3AD")
    # else:
    #     text_box_comment.configure(state="normal")

    text_box_follow_up = App_Text_Box(frame_quality_check_details_bottom, width = 270, height = 85, fg_color = "white", max_length=170)
    text_box_follow_up.place(x=720, y=250)
    text_box_follow_up._textbox.configure(pady = 12)

    text_box_follow_up.set_text(follow_up_dedicated_to_selected_item)

    label_follow_up = App_Label_Title(frame_quality_check_details_bottom, text="Follow up:", font=("Open Sans", 13), text_color="#755a44", fg_color = "transparent")
    label_follow_up.place(x=765, y=235)

    if (str(status_number) == "1"
            or
            (str(status_number) == "2" and sap_id == sap_id_who_posted_invoice)
            or
            (str(status_number) == "4" and admin_role != "admin")):
        text_box_follow_up.configure(state="disabled", fg_color="#E5E5E5", text_color="#808080")
        label_follow_up.configure(text_color="#9AA3AD")
    else:
        text_box_follow_up.configure(state="normal", fg_color="white", text_color="black")
        label_follow_up.configure(text_color="#755A44")

    # if str(status_number) in ["1"]:
    #     text_box_follow_up.configure(state="disabled",fg_color="#E5E5E5", text_color="#808080")
    #     label_follow_up.configure(text_color="#9AA3AD")
    # else:
    #     text_box_follow_up.configure(state="normal")

    text_box_follow_up.bind("<KeyRelease>", check_save_button)
    check_save_button()



    print(repr(comment_dedicated_to_selected_item))
    print(repr(follow_up_dedicated_to_selected_item))


# ---------------------------------------------------------------------------------------------------------
# zmienne zaciągnięte z first_selected_item służące do wyświetlania informacji na górze okna
# ---------------------------------------------------------------------------------------------------------

    key_value_for_database = first_selected_item["Key_value_for_database"]
    sap_document_number = first_selected_item["Document_number_SAP"]
    display_company_code = first_selected_item["Company_code"]
    document_date = first_selected_item["Document_date"]
    due_date = first_selected_item["Due_date"]
    amount_in_local_currency = f"{float(first_selected_item['Amount_local']):,.2f}"
    currency = first_selected_item["Currency"]
    amount_in_eur = f"{float(first_selected_item['Amount_EUR']):,.2f}"
    display_vendor_number = first_selected_item["Vendor_number"]
    display_vendor_type = first_selected_item["Internal_external_vendor"]

    label_quality_check_element_1.configure(text=sap_document_number)
    label_quality_check_element_1.bind("<Button-1>",lambda event: copy_to_clipboard(sap_document_number))

    label_quality_check_element_2.configure(text=display_company_code)
    label_quality_check_element_3.configure(text=document_date)
    label_quality_check_element_4.configure(text=due_date)
    label_quality_check_element_5.configure(text=amount_in_local_currency)
    label_quality_check_element_6.configure(text=currency)
    label_quality_check_element_7.configure(text=amount_in_eur)
    label_quality_check_element_8.configure(text=display_vendor_number)
    label_quality_check_element_9.configure(text=display_vendor_type)



# ---------------------------------------------------------------------------------------------------------
# grafiki umieszczone w ramkach na głównej stronie
# ---------------------------------------------------------------------------------------------------------

    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open(resource_path("Images/Power_off_icon.png"))
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


# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    test_first_selected_item = {
        "Key_value_for_database": 1,
        "Document_number_SAP": "5100001234",
        "Company_code": "1000",
        "Document_date": "2026-09-28",
        "Due_date": "2026-10-28",
        "Amount_local": 100000,
        "Currency": "PLN",
        "Amount_EUR": 23500,
        "Vendor_number": "0000123456",
        "Internal_external_vendor": "External"
    }

    run_quality_check_details(
        quality_check_page=main_page,
        sap_id="TEST_USER",
        first_selected_item=test_first_selected_item,
        total_items=10,
        items_not_mine=4,
        status_number=1,
        country="Poland",
        company_code="1000",
        qc_status="Open",
        vendor_type="External",
        vendor_number="0000123456",
        order_by="Document_number_SAP"
    )