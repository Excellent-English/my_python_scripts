# import customtkinter as ctk
#
#
# class AppDropdown(ctk.CTkComboBox):
#     """
#     Ustandaryzowana lista rozwijana aplikacji.
#     """
#
#     DEFAULTS = {
#         "width": 500,
#         "height": 38,
#
#         "corner_radius": 8,
#         "border_width": 1,
#
#         "fg_color": "#ffffff",
#         "border_color": "#d7dbe0",
#         "button_color" : "#D1D5DB",
#         "button_hover_color" : "#BFC5CD",
#
#         "text_color": "#2b2b2b",
#         "dropdown_fg_color": "#ffffff",
#         "dropdown_hover_color": "#f5f5f5",
#         "dropdown_text_color": "#2b2b2b",
#
#         "font": ("Open Sans", 14),
#         "state": "readonly"
#     }
#
#     def __init__(self, master, **kwargs):
#         config = {**self.DEFAULTS, **kwargs}
#         super().__init__(master, **config)


import customtkinter as ctk


class AppComboBox(ctk.CTkComboBox):
    """
    Ustandaryzowany ComboBox aplikacji.
    """

    DEFAULTS = {
        "width": 500,
        "height": 38,

        "corner_radius": 8,
        "border_width": 1,

        "fg_color": "#ffffff",
        "border_color": "#d7dbe0",

        "button_color": "#D1D5DB",
        "button_hover_color": "#BFC5CD",

        "text_color": "#2b2b2b",

        "dropdown_fg_color": "#ffffff",
        "dropdown_hover_color": "#f5f5f5",
        "dropdown_text_color": "#2b2b2b",

        "font": ("Open Sans", 14),

        # Dla ComboBox można wpisywać własne wartości.
        "state": "normal",

        # Pusta lista na start
        "values": []
    }

    def __init__(self, master, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)

    def set_values(self, values):
        """
        Podmiana całej listy pozycji.
        """
        self.configure(values=values)

    def clear(self):
        """
        Czyści pole.
        """
        self.set("")

    def get_value(self):
        """
        Zwraca aktualną wartość.
        """
        return self.get()

    def set_value(self, value):
        """
        Ustawia wartość.
        """
        self.set(value)