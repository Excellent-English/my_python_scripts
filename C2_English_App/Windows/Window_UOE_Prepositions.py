from C2_English_App.AllClasses.App_Window import AppWindow


def run_prepositions(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_prepositions_page = AppWindow(banner_text = "Prepositions")

    vocabulary_prepositions_page.mainloop()