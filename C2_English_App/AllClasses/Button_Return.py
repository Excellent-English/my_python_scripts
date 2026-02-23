from traceback import print_tb

import customtkinter as ctk
from PIL import Image
from pathlib import Path

import C2_English_App


class Button_Return(ctk.CTkButton):
    """
    Przycisk-ikona z przezroczystym tłem (widoczna tylko grafika).
    Hover wyłączony, więc nie ma potrzeby ustawiania hover_color.
    """

    ICON_PATH = Path(__file__).parent / "../Images/Return_icon.png"
    ICON_SIZE = (50, 50)

    def __init__(self, master, command=None):
        # 1) Załaduj ikonę i utwórz CTkImage
        self._default_go_back = None
        image = Image.open(self.ICON_PATH)
        self._ctk_image = ctk.CTkImage(
            light_image=image,
            dark_image=image,          # ew. podmień na inną ikonę dla dark mode
            size=self.ICON_SIZE
        )

        # 2) Zainicjalizuj przycisk bez tła i bez hovera
        super().__init__(
            master,
            image=self._ctk_image,
            text="",
            command=command,
            fg_color="#755a44",
            bg_color="#755a44",
            border_width=0,
            corner_radius=0,
            hover=False,               # <-- kluczowe, nie ustawiamy hover_color
            width=0,                   # rozmiar kontroluje ikona
            height=0
        )