import customtkinter as ctk

class Button_Brown(ctk.CTkButton):

    """
    Przycisk z domyślnymi właściwościami opartymi na Twojej konfiguracji.
    Parametry przekazane w __init__ nadpisują domyślne.
    """

    DEFAULTS = {
        # Rozmiary
        "width": 160,
        "height": 50,

        # Styl
        "fg_color": "#755a44",
        "hover_color": "#5f4736",
        "text_color": "white",
        "corner_radius": 8,
        "border_width": 1,  # brak obramowania
        "border_color":"#d7dbe0",
        "font": ("Open Sans", 18),
    }


    """
    Co robi poniższa metoda __init__? 
    - bierze domyślne ustawienia,
    - nadpisuje je tym, co podasz przy tworzeniu przycisku,
    - przekazuje wszystko jednym słownikiem do CTkButton.
    """

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)

