import customtkinter as ctk
from PIL import Image
from CTkMessagebox import CTkMessagebox
from class_AppButton import AppButton
from class_AppWindow import AppWindow

def run_window_menu(main_page):
    # Zamknij / ukryj główne okno
    main_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    menu_page = AppWindow(banner_text = "Welcome page")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("Power_off_icon.png")
    # 2. Utworzenie CTkImage
    power_off_icon = ctk.CTkImage(light_image=image, dark_image=image, size=(50, 50))
    # 3. Przycisk z ikoną (bez tekstu) osadzony na banerze
    power_btn = ctk.CTkButton(
        menu_page.banner_frame,
        image=power_off_icon,
        text="",
        width=50, height=50,
        fg_color="transparent",
        hover_color="#755a44",
        command= lambda: menu_page.close_the_app(main_page)
    )
    power_btn.image = power_off_icon  # trzymaj referencję!
    power_btn.place(x=800, y=12)


    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    menu_page.protocol("WM_DELETE_WINDOW", disable_close)

    # ---------------------------------------------------------------------------------------
    # ułożenie 10 przycisków na stronie z menu głównym wraz z tytułami
    # ---------------------------------------------------------------------------------------

    # przyciski vocabulary
    button_menu_page_review = AppButton(menu_page, text="Review")
    button_menu_page_review.place(x=110, y=150)
    button_menu_page_learn = AppButton(menu_page, text="Learn")
    button_menu_page_learn.place(x=280, y=150)
    button_menu_page_listen = AppButton(menu_page, text="Listen")
    button_menu_page_listen.place(x=450, y=150)
    button_menu_page_edit = AppButton(menu_page, text="Edit")
    button_menu_page_edit.place(x=620, y=150)

    # dodanie tytułu dla sekcji Vocabulary
    vocabulary_label = ctk.CTkLabel(
        menu_page,
        text="Vocabulary",
        font=ctk.CTkFont(
            family="Open Sans",
            size=30,
            weight="normal"
            ),
        text_color="#d7dbe0"
    )
    vocabulary_label.place(x=370, y=100)

    # przyciski Use of English
    button_menu_page_word_formation = AppButton(menu_page, text="Word formation")
    button_menu_page_word_formation.place(x=110, y=280)
    button_menu_page_transformations = AppButton(menu_page, text="Transformations")
    button_menu_page_transformations.place(x=280, y=280)
    button_menu_page_prepositions = AppButton(menu_page, text="Prepositions")
    button_menu_page_prepositions.place(x=450, y=280)
    button_menu_page_multiple_choice = AppButton(menu_page, text="Multiple choice")
    button_menu_page_multiple_choice.place(x=620, y=280)

    # dodanie tytułu dla sekcji Use of English
    use_of_english_label = ctk.CTkLabel(
        menu_page,
        text="Use of English",
        font=ctk.CTkFont(
            family="Open Sans",
            size=30,
            weight="normal"
            ),
        text_color="#d7dbe0"
    )
    use_of_english_label.place(x=350, y=230)

    # przyciski fun facts
    button_menu_page_fun_facts_vocabulary = AppButton(menu_page, text="Vocabulary")
    button_menu_page_fun_facts_vocabulary.place(x=280, y=410)
    button_menu_page_fun_facts_grammar = AppButton(menu_page, text="Grammar")
    button_menu_page_fun_facts_grammar.place(x=450, y=410)

    # dodanie tytułu dla sekcji Fun facts
    fun_facts_label = ctk.CTkLabel(
        menu_page,
        text="Fun facts",
        font=ctk.CTkFont(
            family="Open Sans",
            size=30,
            weight="normal"
            ),
        text_color="#d7dbe0"
    )
    fun_facts_label.place(x=380, y=360)



    # Zaprezentuj okno na ekranie komputera
    menu_page.mainloop()






# to na dole jest tylko na próby, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_window_menu(main_page)
