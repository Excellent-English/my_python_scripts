import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Quality Check")
        self.geometry("900x600")

        # przykładowe dane
        self.items = [
            {"Document_number_SAP": "4500012345", "User_name": "Piotr", "Verified": "Yes"},
            {"Document_number_SAP": "4500012346", "User_name": "Anna", "Verified": "No"},
            {"Document_number_SAP": "4500012347", "User_name": "Lukasz", "Verified": "Yes"},
            {"Document_number_SAP": "4500012348", "User_name": "Mateusz", "Verified": "No"},
            {"Document_number_SAP": "4500012349", "User_name": "Magda", "Verified": "Yes"}
        ]

        self.create_scrollable_frame()

    def create_scrollable_frame(self):

        scrollable_frame = ctk.CTkScrollableFrame(
            self,
            width=800,
            height=500
        )
        scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Nagłówki
        ctk.CTkLabel(
            scrollable_frame,
            text="SAP Document",
            font=("Open Sans", 14, "bold")
        ).grid(row=0, column=0, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(
            scrollable_frame,
            text="User",
            font=("Open Sans", 14, "bold")
        ).grid(row=0, column=1, padx=10, pady=10, sticky="w")

        ctk.CTkLabel(
            scrollable_frame,
            text="Verified",
            font=("Open Sans", 14, "bold")
        ).grid(row=0, column=2, padx=10, pady=10, sticky="w")

        # Dane
        for row, item in enumerate(self.items, start=1):

            ctk.CTkLabel(
                scrollable_frame,
                text=item["Document_number_SAP"]
            ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

            ctk.CTkLabel(
                scrollable_frame,
                text=item["User_name"]
            ).grid(row=row, column=1, padx=10, pady=5, sticky="w")

            color = "#00A651" if item["Verified"] == "Yes" else "#D32F2F"

            ctk.CTkLabel(
                scrollable_frame,
                text=item["Verified"],
                text_color=color
            ).grid(row=row, column=2, padx=10, pady=5, sticky="w")


if __name__ == "__main__":
    app = App()
    app.mainloop()