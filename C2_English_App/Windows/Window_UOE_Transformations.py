from C2_English_App.AllClasses.App_Window import AppWindow


def run_tranformations(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_transformations_page = AppWindow(banner_text = "Transformations")

    vocabulary_transformations_page.mainloop()