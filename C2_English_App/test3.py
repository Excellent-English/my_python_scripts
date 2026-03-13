import customtkinter as ctk

def update_progress():
    try:
        value = float(entry.get())
        if 0 <= value <= 1:
            progress.set(value)   # wartość od 0 do 1
        else:
            print("Wpisz liczbę od 0.0 do 1.0")
    except ValueError:
        print("Nieprawidłowa liczba")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

app = ctk.CTk()
app.title("CustomTkinter Progress Demo")
app.geometry("400x200")

entry = ctk.CTkEntry(app, width=120, placeholder_text="np. 0.6")
entry.pack(pady=15)

button = ctk.CTkButton(app, text="Ustaw", command=update_progress)
button.pack(pady=10)

progress = ctk.CTkProgressBar(app, width=300)
progress.pack(pady=20)
progress.set(0)  # start od 0%

app.mainloop()