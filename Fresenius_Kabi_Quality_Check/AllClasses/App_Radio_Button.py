import customtkinter as ctk


class App_Radio_Button(ctk.CTkRadioButton):

    DEFAULTS = {
        # Kolory
        "fg_color": "#C4BDB8",          # zaznaczony punkt
        "hover_color": "#D8D2CD",
        "border_color": "#C7C1BC",

        # Tekst
        "text_color": "#333333",
        "font": ("Open Sans", 12),

        # Rozmiary
        "radiobutton_width": 20,
        "radiobutton_height": 20,

        # Styl
        "border_width_checked": 6,
        "border_width_unchecked": 2,

        # Odstęp między kółkiem a tekstem
        "text_color_disabled": "#9aa3af"
    }

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)