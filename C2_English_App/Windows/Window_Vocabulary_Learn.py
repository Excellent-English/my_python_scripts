from C2_English_App.AllClasses.App_Window import AppWindow


def run_vocabulary_learn(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_learn_page = AppWindow(banner_text = "Learn and remember your words")

    vocabulary_learn_page.mainloop()