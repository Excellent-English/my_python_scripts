import customtkinter as ctk

class App_Label_Title(ctk.CTkLabel):
    """
    Prosty label aplikacyjny z minimalną liczbą parametrów.
    """

    DEFAULTS = {
        # "width": 250,
        # "height": 30,

        "text": "",
        "fg_color": "white",
        "text_color": "#d7dbe0",

        "corner_radius": 8,
        "font": ("Open Sans", 30),

        "anchor": "w",      # wyrównanie tekstu (w = left)
        "justify": "left",
    }

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)
