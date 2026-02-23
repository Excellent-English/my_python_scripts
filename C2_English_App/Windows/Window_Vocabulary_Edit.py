from C2_English_App.AllClasses.App_Window import AppWindow


def run_vocabulary_edit(menu_page):
    # Zamknij / ukryj główne okno
    menu_page.withdraw()

    vocabulary_edit_page = AppWindow(banner_text = "Modify your dictionary")

    vocabulary_edit_page.mainloop()