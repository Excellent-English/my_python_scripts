import customtkinter as ctk


class AppFrame(ctk.CTkFrame):
    """
    Prosta ramka aplikacyjna z minimalną liczbą parametrów.
    """

    DEFAULTS = {
        "width": 350,
        "height": 80,

        # "fg_color": "#f1f4f9",
        "fg_color": "white",
        "border_color": "#d7dbe0",
        "border_width": 1,
        "corner_radius": 8,


        # "max_width": 320,
        # "anchor":"center",
        # "justify":"center",

    }

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)