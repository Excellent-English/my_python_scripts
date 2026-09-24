import customtkinter as ctk

class App_ScrollableFrame(ctk.CTkScrollableFrame):
    """
    Ustandaryzowany Scrollable Frame aplikacji.
    """

    DEFAULTS = {
        "width": 300,
        "height": 350,
        "fg_color": "#FFFFFF",
        "corner_radius": 0,
        "border_width": 0,
        "scrollbar_fg_color": "#FFFFFF",
        "scrollbar_button_color": "#7D7D82",
        "scrollbar_button_hover_color": "#5F6064"
    }

    STATUS_COLORS = {
        "Completed": "#2EAD4A",
        "In Progress": "#F2A900",
        "Not Started": "#A8ADB3"
    }

    def __init__(self, master, **kwargs):
        settings = self.DEFAULTS.copy()
        settings.update(kwargs)

        super().__init__(
            master,
            **settings
        )

        self.grid_columnconfigure(0, weight=1)

# ========================================================
# GŁÓWNY PANEL
# ========================================================

    def create_main_panel(self):

        self.main_panel = ctk.CTkFrame(
            self,
            fg_color="#FFFFFF",
            border_color="#D9DDE2",
            border_width=1,
            corner_radius=12
        )

        self.main_panel.grid(
            row=0,
            column=0,
            padx=25,
            pady=25,
            sticky="nsew"
        )

        self.main_panel.grid_columnconfigure(0, weight=1)
        self.main_panel.grid_rowconfigure(2, weight=1)

        self.create_header()
        self.create_search_section()
        self.create_items_list()
        self.create_legend()

    # ========================================================
    # NAGŁÓWEK
    # ========================================================

    def create_header(self):

        self.header_frame = ctk.CTkFrame(
            self.main_panel,
            fg_color="transparent"
        )

        self.header_frame.grid(
            row=0,
            column=0,
            padx=18,
            pady=(16, 8),
            sticky="ew"
        )

        self.header_frame.grid_columnconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(
            self.header_frame,
            text=f"Items ({len(self.all_items)})",
            font=("Open Sans", 16, "bold"),
            text_color="#202124",
            anchor="w"
        )

        self.title_label.grid(
            row=0,
            column=0,
            sticky="w"
        )

    # ========================================================
    # WYSZUKIWARKA I FILTR
    # ========================================================

    def create_search_section(self):

        self.search_frame = ctk.CTkFrame(
            self.main_panel,
            fg_color="transparent"
        )

        self.search_frame.grid(
            row=1,
            column=0,
            padx=18,
            pady=(0, 12),
            sticky="ew"
        )

        self.search_frame.grid_columnconfigure(0, weight=1)

        self.search_entry = ctk.CTkEntry(
            self.search_frame,
            height=40,
            placeholder_text="⌕   Search items...",
            font=("Open Sans", 13),
            text_color="#242424",
            placeholder_text_color="#7A7D83",
            fg_color="#FFFFFF",
            border_color="#D9DDE2",
            border_width=1,
            corner_radius=7
        )

        self.search_entry.grid(
            row=0,
            column=0,
            padx=(0, 10),
            sticky="ew"
        )

        self.search_entry.bind(
            "<KeyRelease>",
            self.search_items
        )

        self.filter_button = ctk.CTkButton(
            self.search_frame,
            text="☷",
            width=42,
            height=40,
            corner_radius=7,
            border_width=1,
            border_color="#D9DDE2",
            fg_color="#FFFFFF",
            hover_color="#F1F2F3",
            text_color="#343434",
            font=("Open Sans", 18),
            command=self.change_status_filter
        )

        self.filter_button.grid(
            row=0,
            column=1
        )

    # ========================================================
    # SCROLLABLE FRAME
    # ========================================================

    def create_items_list(self):

        self.items_scrollable_frame = AppScrollableFrame(
            self.main_panel,
            width=520,
            height=500,
            fg_color="#FFFFFF",
            border_width=0,
            corner_radius=0,
            scrollbar_fg_color="#FFFFFF",
            scrollbar_button_color="#7D7D82",
            scrollbar_button_hover_color="#5F6064"
        )

        self.items_scrollable_frame.grid(
            row=2,
            column=0,
            padx=(10, 6),
            pady=0,
            sticky="nsew"
        )

        self.items_scrollable_frame.grid_columnconfigure(
            0,
            weight=1
        )

        self.display_items(self.all_items)

    # ========================================================
    # TWORZENIE WIERSZY
    # ========================================================

    def display_items(self, items):

        for widget in self.items_scrollable_frame.winfo_children():
            widget.destroy()

        for row_number, item in enumerate(items):
            self.create_item_row(
                item=item,
                row_number=row_number
            )

        self.title_label.configure(
            text=f"Items ({len(items)})"
        )

    def create_item_row(self, item, row_number):

        status_color = STATUS_COLORS.get(
            item["status"],
            "#A8ADB3"
        )

        item_frame = ctk.CTkFrame(
            self.items_scrollable_frame,
            height=48,
            corner_radius=4,
            fg_color="#FFFFFF",
            cursor="hand2"
        )

        item_frame.grid(
            row=row_number,
            column=0,
            padx=2,
            pady=0,
            sticky="ew"
        )

        item_frame.grid_propagate(False)

        # Kółko | kod | nazwa | status
        item_frame.grid_columnconfigure(0, minsize=34)
        item_frame.grid_columnconfigure(1, minsize=80)
        item_frame.grid_columnconfigure(2, weight=1)
        item_frame.grid_columnconfigure(3, minsize=95)

        # ----------------------------------------------------
        # KOLOROWE KÓŁKO
        # ----------------------------------------------------

        status_dot = ctk.CTkLabel(
            item_frame,
            text="●",
            width=20,
            text_color=status_color,
            font=("Arial", 18),
            cursor="hand2"
        )

        status_dot.grid(
            row=0,
            column=0,
            padx=(8, 2),
            pady=8
        )

        # ----------------------------------------------------
        # KOD ITEMU
        # ----------------------------------------------------

        code_label = ctk.CTkLabel(
            item_frame,
            text=item["code"],
            font=("Open Sans", 12),
            text_color="#242424",
            anchor="w",
            cursor="hand2"
        )

        code_label.grid(
            row=0,
            column=1,
            padx=(3, 8),
            sticky="w"
        )

        # ----------------------------------------------------
        # NAZWA ITEMU
        # ----------------------------------------------------

        name_label = ctk.CTkLabel(
            item_frame,
            text=item["name"],
            font=("Open Sans", 12),
            text_color="#242424",
            anchor="w",
            cursor="hand2"
        )

        name_label.grid(
            row=0,
            column=2,
            padx=(0, 10),
            sticky="w"
        )

        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        status_label = ctk.CTkLabel(
            item_frame,
            text=item["status"],
            font=("Open Sans", 12),
            text_color=status_color,
            anchor="e",
            cursor="hand2"
        )

        status_label.grid(
            row=0,
            column=3,
            padx=(10, 15),
            sticky="e"
        )

        # ----------------------------------------------------
        # DOLNA LINIA ODDZIELAJĄCA WIERSZE
        # ----------------------------------------------------

        separator = ctk.CTkFrame(
            item_frame,
            height=2,
            corner_radius=0,
            fg_color="#EFEFEF"
        )

        separator.grid(
            row=1,
            column=0,
            columnspan=4,
            sticky="ew"
        )

        # ----------------------------------------------------
        # KLIKNIĘCIE I HOVER CAŁEGO WIERSZA
        # ----------------------------------------------------

        clickable_widgets = [
            item_frame,
            status_dot,
            code_label,
            name_label,
            status_label
        ]

        for widget in clickable_widgets:

            widget.bind(
                "<Button-1>",
                lambda event, selected_item=item:
                    open_item(selected_item)
            )

    # ========================================================
    # WYSZUKIWANIE
    # ========================================================

    def search_items(self, event=None):

        search_text = (
            self.search_entry
            .get()
            .strip()
            .lower()
        )

        filtered_items = []

        for item in self.all_items:

            matches_text = (
                search_text in item["code"].lower()
                or
                search_text in item["name"].lower()
                or
                search_text in item["status"].lower()
            )

            matches_status = (
                self.current_filter is None
                or
                item["status"] == self.current_filter
            )

            if matches_text and matches_status:
                filtered_items.append(item)

        self.display_items(filtered_items)

    # ========================================================
    # FILTROWANIE PO STATUSIE
    # ========================================================

    def change_status_filter(self):

        filters = [
            None,
            "Completed",
            "In Progress",
            "Not Started"
        ]

        current_index = filters.index(
            self.current_filter
        )

        next_index = (
            current_index + 1
        ) % len(filters)

        self.current_filter = filters[next_index]

        button_colors = {
            None: "#343434",
            "Completed": STATUS_COLORS["Completed"],
            "In Progress": STATUS_COLORS["In Progress"],
            "Not Started": STATUS_COLORS["Not Started"]
        }

        self.filter_button.configure(
            text_color=button_colors[self.current_filter]
        )

        self.search_items()

    # ========================================================
    # LEGENDA
    # ========================================================

    def create_legend(self):

        self.legend_frame = ctk.CTkFrame(
            self.main_panel,
            fg_color="transparent",
            height=58
        )

        self.legend_frame.grid(
            row=3,
            column=0,
            padx=18,
            pady=(8, 14),
            sticky="ew"
        )

        self.legend_frame.grid_columnconfigure(0, weight=1)
        self.legend_frame.grid_columnconfigure(1, weight=1)
        self.legend_frame.grid_columnconfigure(2, weight=1)

        self.create_legend_item(
            column=0,
            text="Completed",
            color=STATUS_COLORS["Completed"]
        )

        self.create_legend_item(
            column=1,
            text="In Progress",
            color=STATUS_COLORS["In Progress"]
        )

        self.create_legend_item(
            column=2,
            text="Not Started",
            color=STATUS_COLORS["Not Started"]
        )

    def create_legend_item(self, column, text, color):

        legend_item = ctk.CTkFrame(
            self.legend_frame,
            fg_color="transparent"
        )

        legend_item.grid(
            row=0,
            column=column,
            padx=6,
            pady=8
        )

        dot = ctk.CTkLabel(
            legend_item,
            text="●",
            width=20,
            font=("Arial", 18),
            text_color=color
        )

        dot.grid(
            row=0,
            column=0,
            padx=(0, 4)
        )

        label = ctk.CTkLabel(
            legend_item,
            text=text,
            font=("Open Sans", 12),
            text_color="#3E4044"
        )

        label.grid(
            row=0,
            column=1
        )