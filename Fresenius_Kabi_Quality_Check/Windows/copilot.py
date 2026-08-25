import customtkinter as ctk

ctk.set_appearance_mode("light")

# =====================================================
# WINDOW
# =====================================================

app = ctk.CTk()
app.title("AuditMaster Pro")
app.geometry("1400x900")

BROWN = "#6A442B"
BG = "#F7F7F7"

app.configure(fg_color=BG)

# =====================================================
# TOP BAR
# =====================================================

top_bar = ctk.CTkFrame(
    app,
    height=70,
    corner_radius=0,
    fg_color=BROWN
)
top_bar.pack(fill="x")

title_lbl = ctk.CTkLabel(
    top_bar,
    text="AuditMaster Pro",
    font=("Segoe UI", 30, "bold"),
    text_color="white"
)
title_lbl.pack(side="left", padx=20, pady=15)

# =====================================================
# FILTER SECTION
# =====================================================

filter_frame = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
filter_frame.pack(fill="x", padx=20, pady=10)

country_cb = ctk.CTkComboBox(
    filter_frame,
    values=["Poland", "Germany", "Austria"],
    width=250
)
country_cb.set("Poland")
country_cb.grid(row=0, column=0, padx=5)

company_cb = ctk.CTkComboBox(
    filter_frame,
    values=["PL01 - Warsaw"],
    width=250
)
company_cb.set("PL01 - Warsaw")
company_cb.grid(row=0, column=1, padx=5)

load_btn = ctk.CTkButton(
    filter_frame,
    text="Load Items",
    fg_color=BROWN
)
load_btn.grid(row=0, column=2, padx=10)

progress = ctk.CTkProgressBar(
    filter_frame,
    width=250
)
progress.set(0.37)
progress.grid(row=0, column=3, padx=(150,10))

progress_lbl = ctk.CTkLabel(
    filter_frame,
    text="37 / 100 items (37%)"
)
progress_lbl.grid(row=0, column=4)

# =====================================================
# MAIN AREA
# =====================================================

main = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
main.pack(fill="both", expand=True, padx=20, pady=10)

main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=2)

# =====================================================
# LEFT PANEL
# =====================================================

left_panel = ctk.CTkFrame(main)
left_panel.grid(row=0, column=0, sticky="nsew", padx=(0,10))

header = ctk.CTkLabel(
    left_panel,
    text="Items (100)",
    font=("Segoe UI", 18, "bold")
)
header.pack(anchor="w", padx=10, pady=10)

search = ctk.CTkEntry(
    left_panel,
    placeholder_text="Search items..."
)
search.pack(fill="x", padx=10)

items_frame = ctk.CTkScrollableFrame(
    left_panel,
    height=650
)
items_frame.pack(fill="both", expand=True, padx=10, pady=10)

items = [
    ("ITM-0001", "Cash and Cash Equivalents", "Completed"),
    ("ITM-0002", "Accounts Receivable", "Completed"),
    ("ITM-0003", "Inventory Management", "In Progress"),
    ("ITM-0004", "Accounts Payable", "Completed"),
    ("ITM-0005", "Fixed Assets", "Not Started"),
    ("ITM-0006", "Revenue Recognition", "Completed"),
    ("ITM-0007", "Payroll Processing", "In Progress"),
    ("ITM-0008", "Bank Reconciliations", "In Progress"),
    ("ITM-0009", "Tax Compliance", "Not Started"),
]

colors = {
    "Completed": "#28A745",
    "In Progress": "#F0A500",
    "Not Started": "#9E9E9E"
}

for code, name, status in items:

    row = ctk.CTkFrame(
        items_frame,
        fg_color="#EFEAE6" if code == "ITM-0008" else "transparent"
    )
    row.pack(fill="x", pady=2)

    dot = ctk.CTkLabel(
        row,
        text="●",
        text_color=colors[status],
        width=20
    )
    dot.pack(side="left", padx=(5,5))

    code_lbl = ctk.CTkLabel(
        row,
        text=code,
        width=80
    )
    code_lbl.pack(side="left")

    name_lbl = ctk.CTkLabel(
        row,
        text=name,
        width=180,
        anchor="w"
    )
    name_lbl.pack(side="left")

    status_lbl = ctk.CTkLabel(
        row,
        text=status,
        text_color=colors[status]
    )
    status_lbl.pack(side="right", padx=10)

# =====================================================
# RIGHT PANEL
# =====================================================

right_panel = ctk.CTkFrame(main)
right_panel.grid(row=0, column=1, sticky="nsew")

item_title = ctk.CTkLabel(
    right_panel,
    text="ITM-0008   Bank Reconciliations",
    font=("Segoe UI", 28, "bold")
)
item_title.pack(anchor="w", padx=20, pady=15)

mark_all_btn = ctk.CTkButton(
    right_panel,
    text="Mark all as Yes",
    fg_color=BROWN
)
mark_all_btn.pack(anchor="e", padx=20)

controls_frame = ctk.CTkFrame(
    right_panel
)
controls_frame.pack(fill="x", padx=20, pady=15)

controls = [
    "Bank reconciliations are performed within 5 business days",
    "All bank accounts are reconciled monthly",
    "Differences are investigated and resolved",
    "Supporting documentation is complete",
    "Statements are approved",
    "Reports are retained"
]

for i, text in enumerate(controls, start=1):

    row = ctk.CTkFrame(
        controls_frame,
        fg_color="transparent"
    )
    row.pack(fill="x", pady=5)

    number = ctk.CTkLabel(
        row,
        text=str(i),
        width=35
    )
    number.pack(side="left")

    lbl = ctk.CTkLabel(
        row,
        text=text,
        anchor="w"
    )
    lbl.pack(side="left", fill="x", expand=True)

    seg = ctk.CTkSegmentedButton(
        row,
        values=["Yes", "No", "N/A"],
        width=220
    )
    seg.set("Yes")
    seg.pack(side="right", padx=10)

comments = ctk.CTkTextbox(
    right_panel,
    height=120
)
comments.pack(fill="x", padx=20, pady=15)

bottom = ctk.CTkFrame(
    right_panel,
    fg_color="transparent"
)
bottom.pack(fill="x", padx=20, pady=15)

prev_btn = ctk.CTkButton(
    bottom,
    text="Previous Item",
    fg_color="gray50"
)
prev_btn.pack(side="left")

counter = ctk.CTkLabel(
    bottom,
    text="Item 8 of 100"
)
counter.pack(side="left", expand=True)

next_btn = ctk.CTkButton(
    bottom,
    text="Save & Next Item",
    fg_color=BROWN
)
next_btn.pack(side="right")

app.mainloop()