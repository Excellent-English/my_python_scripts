import customtkinter as ctk
from Fresenius_Kabi_Quality_Check.AllClasses.App_ScrollableFrame import AppScrollableFrame


def open_control(name):
    print(f"Wybrano: {name}")


def bind_row_click(widget, control_name):
    """
    Przypina kliknięcie do dowolnej kontrolki.
    """
    widget.bind(
        "<Button-1>",
        lambda event, name=control_name: open_control(name)
    )


app = ctk.CTk()
app.geometry("700x600")

frame_controls = AppScrollableFrame(
    app,
    width=600,
    height=450
)

frame_controls.place(x=50, y=50)

for i in range(20):

    control_name = f"Control {i + 1}"

    # Naprzemienne kolory
    row_color = "#FFFFFF" if i % 2 == 0 else "#F7F7F7"

    item_frame = ctk.CTkFrame(
        frame_controls,
        fg_color=row_color,
        corner_radius=6,
        height=42
    )

    item_frame.grid(
        row=i,
        column=0,
        sticky="ew",
        padx=0,
        pady=0
    )

    item_frame.grid_columnconfigure(1, weight=1)

    # ---------------------------------------------------------
    # STATUS
    # ---------------------------------------------------------

    status_colors = [
        "#22C55E",  # zielony
        "#EAB308",  # żółty
        "#EF4444"   # czerwony
    ]

    status = ctk.CTkLabel(
        item_frame,
        text="●",
        text_color=status_colors[i % 3],
        font=("Arial", 18)
    )

    status.grid(
        row=0,
        column=0,
        padx=(15, 10),
        pady=8
    )

    # ---------------------------------------------------------
    # LABEL
    # ---------------------------------------------------------

    label = ctk.CTkLabel(
        item_frame,
        text=control_name,
        anchor="w",
        text_color="#755A44",
        font=("Open Sans", 13),
        cursor="hand2"
    )

    label.grid(
        row=0,
        column=1,
        sticky="w"
    )

    # ---------------------------------------------------------
    # STRZAŁKA
    # ---------------------------------------------------------

    btn_open = ctk.CTkButton(
        item_frame,
        text="›",
        width=30,
        height=30,
        fg_color="transparent",
        text_color="#755A44",
        hover_color="#ECECEC",
        font=("Open Sans", 18, "bold")
    )

    btn_open.grid(
        row=0,
        column=2,
        padx=(5, 10)
    )

    # ---------------------------------------------------------
    # HOVER DLA CAŁEGO WIERSZA
    # ---------------------------------------------------------

    def row_enter(event, frame=item_frame):
        frame.configure(fg_color="#ECECEC")

    def row_leave(event, frame=item_frame, color=row_color):
        frame.configure(fg_color=color)

    for widget in [item_frame, status, label, btn_open]:
        widget.bind("<Enter>", row_enter)
        widget.bind("<Leave>", row_leave)

    # ---------------------------------------------------------
    # KLIKNIĘCIE CAŁEGO WIERSZA
    # ---------------------------------------------------------

    bind_row_click(item_frame, control_name)
    bind_row_click(status, control_name)
    bind_row_click(label, control_name)
    bind_row_click(btn_open, control_name)

app.mainloop()