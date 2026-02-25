
import customtkinter as ctk


class App_Entry_Box(ctk.CTkEntry):
    """
    Minimalny, spójny z resztą aplikacji TextBox (wielowierszowy).
    Parametry przekazane w __init__ nadpisują domyślne.
    """

    DEFAULTS = {
        # Rozmiar
        "width": 300,
        "height": 40,

        # Styl (spójny z AppButton/AppFrame)
        "fg_color": "#f1f4f9",
        "text_color": "#4d4d4d",
        "border_color": "#d7dbe0",
        "border_width": 1,
        "corner_radius": 8,
        "font": ("Open Sans", 18),

        # Zawijanie linii (word/char/none)
        # "wrap": "word",

        # Wyrównanie tekstu
        "justify": "center"

    }


    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)


    def get_text(self):
        return self.get()
