from C2_English_App.AllClasses.App_Window import AppWindow


def run_word_formation(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_word_formation_page = AppWindow(banner_text = "Word formation")

    vocabulary_word_formation_page.mainloop()