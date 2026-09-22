import customtkinter as ctk


class App_Text_Box(ctk.CTkTextbox):

    DEFAULTS = {
        "width": 270,
        "height": 70,
        "fg_color": "#f1f4f9",
        "text_color": "#666666",
        "border_color": "#d7dbe0",
        "border_width": 1,
        "corner_radius": 8,
        "font": ("Open Sans", 12),
        "wrap": "word"
    }

    def __init__(self, master, max_length=None, **kwargs):
        config = {**self.DEFAULTS, **kwargs}
        super().__init__(master, **config)

        self.max_length = max_length

        if self.max_length:
            self.bind("<KeyRelease>", self._limit_text)

    def _limit_text(self, event=None):
        text = self.get("1.0", "end-1c")

        if len(text) > self.max_length:
            self.delete(f"1.0 + {self.max_length} chars", "end")

    def get_text(self):
        return self.get("1.0", "end-1c")

    def set_text(self, text):
        self.delete("1.0", "end")
        self.insert("1.0", text)

    def clear(self):
        self.delete("1.0", "end")