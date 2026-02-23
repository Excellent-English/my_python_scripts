from C2_English_App.AllClasses.App_Window import AppWindow


def run_multiple_choice(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_multiple_choice_page = AppWindow(banner_text = "Multiple choice")

    vocabulary_multiple_choice_page.mainloop()