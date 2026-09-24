import customtkinter as ctk
import pyodbc
import pandas as pd
from tkinter import messagebox


# --------------------------------------------------
# CustomTkinter Configuration
# --------------------------------------------------

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


# --------------------------------------------------
# Database Connection
# --------------------------------------------------

def get_connection():
    return pyodbc.connect(
        """
        Driver={ODBC Driver 17 for SQL Server};
        Server=tcp:sscciq.database.windows.net,1433;
        Database=SSC CIQ;
        Trusted_Connection=no;
        Authentication=ActiveDirectoryInteractive;
        UID=piotr.szczubiala@fresenius-kabi.com;
        """
    )


# --------------------------------------------------
# Get Record Count
# --------------------------------------------------

def get_record_count():

    try:

        conn = get_connection()

        df = pd.read_sql_query(
            "SELECT * FROM quality_check_database",
            conn
        )

        lbl_count.configure(
            text=f"Number of records: {len(df)}"
        )

        conn.close()

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# --------------------------------------------------
# Add Record
# --------------------------------------------------

def add_record():

    try:

        key_value = entry_key_value.get().strip()

        if key_value == "":

            messagebox.showwarning(
                "Warning",
                "Please enter Key_value_for_database."
            )

            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO quality_check_database
            (
                Key_value_for_database,
                Verified
            )
            VALUES
            (?, ?)
            """,
            key_value,
            0
        )

        conn.commit()
        conn.close()

        messagebox.showinfo(
            "Success",
            f"Record '{key_value}' has been added successfully."
        )

        entry_key_value.delete(0, "end")

    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )


# --------------------------------------------------
# Main Window
# --------------------------------------------------

app = ctk.CTk()
app.title("Quality Check Database Management")
app.geometry("700x450")

# --------------------------------------------------
# Header
# --------------------------------------------------

title_label = ctk.CTkLabel(
    app,
    text="Quality Check Database Management",
    font=("Segoe UI", 24, "bold")
)

title_label.pack(pady=25)

# --------------------------------------------------
# Record Count Section
# --------------------------------------------------

btn_count = ctk.CTkButton(
    app,
    text="Get Record Count",
    command=get_record_count,
    width=250,
    height=40
)

btn_count.pack(pady=10)

lbl_count = ctk.CTkLabel(
    app,
    text="Number of records: -",
    font=("Segoe UI", 16)
)

lbl_count.pack(pady=10)

# --------------------------------------------------
# Add Record Section
# --------------------------------------------------

section_label = ctk.CTkLabel(
    app,
    text="Add Record",
    font=("Segoe UI", 18, "bold")
)

section_label.pack(pady=(30, 10))

entry_key_value = ctk.CTkEntry(
    app,
    width=350,
    placeholder_text="Enter Key_value_for_database"
)

entry_key_value.pack(pady=10)

btn_add = ctk.CTkButton(
    app,
    text="Add Record",
    command=add_record,
    width=250,
    height=40
)

btn_add.pack(pady=10)

# --------------------------------------------------
# Start Application
# --------------------------------------------------

app.mainloop()