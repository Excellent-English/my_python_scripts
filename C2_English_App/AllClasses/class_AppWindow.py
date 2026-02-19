import customtkinter as ctk
from PIL import Image


class AppWindow(ctk.CTkToplevel):
    """
    Okno aplikacji z domyślną konfiguracją.
    Parametry przekazane w __init__ nadpisują domyślne.
    """

    DEFAULTS = {
        # wymiary dotyczące okna
        "fg_color": "white",
        "title": "The ultimate guide to C2 Proficiency level!",
        "width": 900,
        "height": 530,
        "x": 230,
        "y": 80,
        "resizable": (False, False),
        "focus_force": True,

        # wymiary dotyczące brązowego prostokąta i tytułu
        "banner_height": 75,
        "banner_bg": "#755a44",
        "banner_corner_radius": 0,
        "banner_text": "Welcome page",
        "banner_text_color": "white",
        "banner_font_family": "Open Sans",  # musi być zainstalowany w systemie
        "banner_font_size": 30,
        "banner_font_weight": "normal",     # np. "bold"
        "banner_text_offset_x": 110,        # przesunięcie tekstu w poziomie
        "banner_text_offset_y": 20         # przesunięcie tekstu w pionie
    }


    def __init__(self, **kwargs):
        config = {**self.DEFAULTS, **kwargs}

        # utworzenie okna
        super().__init__(fg_color=config["fg_color"])

        # konfiguracja okna
        self.title(config["title"])
        self.geometry(
            f'{config["width"]}x{config["height"]}+{config["x"]}+{config["y"]}'
        )
        self.resizable(*config["resizable"])

        if config["focus_force"]:
            self.focus_force()



        # --- baner: brązowy prostokąt u góry ---
        self.banner_frame = ctk.CTkFrame(
            self,
            width=config["width"],                 # szerokość = szerokość okna
            height=config["banner_height"],
            fg_color=config["banner_bg"],
            corner_radius=config["banner_corner_radius"],
        )
        # pozycjonowanie banera
        self.banner_frame.place(x=0, y=0)

        # --- tytuł w banerze ---
        self.banner_label = ctk.CTkLabel(
            self.banner_frame,
            text=config["banner_text"],
            font=ctk.CTkFont(
                family=config["banner_font_family"],
                size=config["banner_font_size"],
                weight=config["banner_font_weight"],
            ),
            text_color=config["banner_text_color"],
        )
        self.banner_label.place(
            x=config["banner_text_offset_x"],
            y=config["banner_text_offset_y"]
        )


    def close_the_app(self, main_page):
        from CTkMessagebox import CTkMessagebox
        msg = CTkMessagebox(
            title="Goodbye",
            message="Do you really want to close the application?",
            icon="question",
            option_1="No",
            option_2="Yes",
            button_color="#f1f4f9",
            button_hover_color="#FFFFE5",
            button_text_color="#4d4d4d"
        )
        if msg.get() == "Yes":
            self.destroy()
            main_page.destroy()