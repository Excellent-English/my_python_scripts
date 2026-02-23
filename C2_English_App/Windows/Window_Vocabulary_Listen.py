from C2_English_App.AllClasses.App_Window import AppWindow


def run_vocabulary_listen(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_listen_page = AppWindow(banner_text = "Listen to your words")

    vocabulary_listen_page.mainloop()