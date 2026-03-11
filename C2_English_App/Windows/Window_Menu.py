import customtkinter as ctk
from PIL import Image
from C2_English_App.AllClasses.Button_Standard import Button_Standard
from C2_English_App.AllClasses.App_Window import AppWindow
from C2_English_App.AllClasses.App_Label_Title import App_Label_Title
from C2_English_App.Windows.Window_UOE_Multiple_Choice import run_multiple_choice
from C2_English_App.Windows.Window_UOE_Prepositions import run_prepositions
from C2_English_App.Windows.Window_UOE_Transformations import run_tranformations
from C2_English_App.Windows.Window_UOE__Word_Formation import run_word_formation
from C2_English_App.Windows.Window_Vocabulary_Edit import run_vocabulary_edit
from C2_English_App.Windows.Window_Vocabulary_Learn import run_vocabulary_learn
from C2_English_App.Windows.Window_Vocabulary_Listen import run_vocabulary_listen
from C2_English_App.Windows.Window_Vocabulary_Review import run_vocabulary_review


def run_window_menu(main_page):
    # Zamknij / ukryj główne okno
    main_page.withdraw()   # albo destroy()

    # Utwórz nowe okno menu
    menu_page = AppWindow(banner_text = "Welcome page")
    # Gdyby była potrzeba zmiany tytułu w kolejnych oknach:
    # menu_page = AppWindow(title="Inny tytuł okna")


    # Dodanie przycisku zawierającego ikonę power off- przycisk zamyka aplikację
    # 1. Wczytanie obrazu z pliku
    image = Image.open("../Images/Power_off_icon.png")
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
    menu_page.bind("<Escape>", lambda event: menu_page.close_the_app(main_page))


    # zablokuj zamknięcie okna za pomocą "X"
    def disable_close():
        pass
    menu_page.protocol("WM_DELETE_WINDOW", disable_close)

    # ---------------------------------------------------------------------------------------
    # ułożenie 10 przycisków na stronie z menu głównym wraz z tytułami
    # ---------------------------------------------------------------------------------------

    # dodanie tytułu dla sekcji Vocabulary
    vocabulary_label = App_Label_Title(menu_page, text="Vocabulary")
    vocabulary_label.place(x=370, y=100)

    # przyciski vocabulary
    button_menu_page_review = Button_Standard(menu_page, text="Review", command=lambda: run_vocabulary_review(menu_page))
    button_menu_page_review.place(x=110, y=150)
    button_menu_page_learn = Button_Standard(menu_page, text="Learn", command=lambda: run_vocabulary_learn(menu_page))
    button_menu_page_learn.place(x=280, y=150)
    button_menu_page_listen = Button_Standard(menu_page, text="Listen", command=lambda: run_vocabulary_listen(menu_page))
    button_menu_page_listen.place(x=450, y=150)
    button_menu_page_edit = Button_Standard(menu_page, text="Edit", command=lambda: run_vocabulary_edit(menu_page))
    button_menu_page_edit.place(x=620, y=150)


    # dodanie tytułu dla sekcji Use of English
    use_of_english_label = App_Label_Title(menu_page, text="Use of English")
    use_of_english_label.place(x=350, y=230)

    # przyciski Use of English
    button_menu_page_word_formation = Button_Standard(menu_page, text="Word formation", command=lambda: run_word_formation(menu_page))
    button_menu_page_word_formation.place(x=110, y=280)
    button_menu_page_transformations = Button_Standard(menu_page, text="Transformations", command=lambda: run_tranformations(menu_page))
    button_menu_page_transformations.place(x=280, y=280)
    button_menu_page_prepositions = Button_Standard(menu_page, text="Prepositions", command=lambda: run_prepositions(menu_page))
    button_menu_page_prepositions.place(x=450, y=280)
    button_menu_page_multiple_choice = Button_Standard(menu_page, text="Multiple choice", command=lambda: run_multiple_choice(menu_page))
    button_menu_page_multiple_choice.place(x=620, y=280)


    # dodanie tytułu dla sekcji Fun facts
    fun_facts_label = App_Label_Title(menu_page, text="Fun facts")
    fun_facts_label.place(x=380, y=360)

    # przyciski fun facts
    button_menu_page_fun_facts_vocabulary = Button_Standard(menu_page, text="Vocabulary")
    button_menu_page_fun_facts_vocabulary.place(x=280, y=410)
    button_menu_page_fun_facts_grammar = Button_Standard(menu_page, text="Grammar")
    button_menu_page_fun_facts_grammar.place(x=450, y=410)


    # Zaprezentuj okno na ekranie komputera
    menu_page.mainloop()






# funkcja do uruchomienia okna dla testów, później do usunięcia

if __name__ == "__main__":
    main_page = ctk.CTk()
    main_page.withdraw()

    run_window_menu(main_page)
