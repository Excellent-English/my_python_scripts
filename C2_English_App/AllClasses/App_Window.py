import customtkinter as ctk
from C2_English_App.AllClasses.Button_Return import Button_Return


class AppWindow(ctk.CTkToplevel):
    """Proste okno z banerem + pasywny return button."""

    def __init__(
        self,
        title: str = "The ultimate guide to C2 Proficiency level!",
        width: int = 900,
        height: int = 530,
        x: int = 230,
        y: int = 80,
        banner_text: str = "Welcome page",
        banner_bg: str = "#755a44",
        fg_color: str = "white",
        focus: bool = True,
        return_pos: tuple[int, int] = (20, 12)
    ):
        super().__init__(fg_color=fg_color)

        # Okno
        self.title(title)
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.resizable(False, False)
        if focus:
            self.focus_force()

        # Baner
        self.banner_frame = ctk.CTkFrame(
            self, width=width, height=75, fg_color=banner_bg, corner_radius=0
        )
        self.banner_frame.place(x=0, y=0)

        # Tytuł w banerze
        self.banner_label = ctk.CTkLabel(
            self.banner_frame,
            text=banner_text,
            font=ctk.CTkFont("Open Sans", 30, "normal"),
            text_color="white",
        )
        self.banner_label.place(x=110, y=20)

        # --- Return button (pasywny) ---
        self.return_button = Button_Return(self.banner_frame)
        rx, ry = return_pos
        self.return_button.place(x=800, y=12)







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