import customtkinter as ctk


class App_Check_Box(ctk.CTkCheckBox):

    DEFAULTS = {
        # Kolory
        "fg_color": "#C4BDB8",
        "hover_color": "#D8D2CD",
        "border_color": "#C7C1BC",
        "checkmark_color": "white",

        # Tekst
        "text_color": "#333333",
        "text_color_disabled": "#9AA3AF",
        "font": ("Open Sans", 12),

        # Rozmiary
        "width": 20,
        "height": 20,

        # Styl
        "border_width": 2,
        "corner_radius": 5
    }

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)