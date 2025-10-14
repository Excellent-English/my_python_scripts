import customtkinter as ctk

class ClickCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Counter App")

        self.yes_count = 0
        self.no_count = 0

        self.yes_button = ctk.CTkButton(root, text="Tak", command=self.increment_yes)
        self.yes_button.pack(pady=10)

        self.no_button = ctk.CTkButton(root, text="Nie", command=self.increment_no)
        self.no_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(root, text="Tak: 0, Nie: 0")
        self.result_label.pack(pady=10)

        self.progress_bar_canvas = ctk.CTkCanvas(root, width=400, height=30)
        self.progress_bar_canvas.pack(pady=10)

    def increment_yes(self):
        self.yes_count += 1
        self.update_ui()

    def increment_no(self):
        self.no_count += 1
        self.update_ui()

    def update_ui(self):
        total_clicks = self.yes_count + self.no_count
        if total_clicks > 0:
            yes_percentage = (self.yes_count / total_clicks) * 100
            no_percentage = (self.no_count / total_clicks) * 100

            self.progress_bar_canvas.delete("all")
            self.progress_bar_canvas.create_rectangle(0, 0, yes_percentage * 4, 30, fill="green")
            self.progress_bar_canvas.create_rectangle(yes_percentage * 4, 0, 400, 30, fill="red")

            # Dodanie etykiet procentowych
            self.progress_bar_canvas.create_text(yes_percentage * 2, 15, text=f"{yes_percentage:.2f}%", fill="white")
            self.progress_bar_canvas.create_text(yes_percentage * 4 + no_percentage * 2, 15, text=f"{no_percentage:.2f}%", fill="white")

            self.result_label.configure(text=f"Tak: {self.yes_count}, Nie: {self.no_count} ({yes_percentage:.2f}% Tak, {no_percentage:.2f}% Nie)")

if __name__ == "__main__":
    root = ctk.CTk()
    app = ClickCounterApp(root)
    root.mainloop()