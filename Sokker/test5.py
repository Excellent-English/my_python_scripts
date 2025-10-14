import tkinter as tk

# Funkcja do uruchomienia nowego okna z efektem przejścia
def open_new_window():
    def fade_out():
        alpha = root.attributes("-alpha")
        if alpha > 0:
            alpha -= 0.1
            root.attributes("-alpha", alpha)
            root.after(50, fade_out)
        else:
            show_new_window()

    def show_new_window():
        new_window = tk.Toplevel(root)
        new_window.title("Nowe Okno")
        new_window.geometry("400x200")  # Ustawienie rozmiaru nowego okna na taki sam jak początkowe okno

        # Funkcja do powrotu do poprzedniego okna
        def go_back():
            new_window.destroy()
            root.attributes("-alpha", 1)

        # Funkcja do zakończenia programu po kliknięciu "X"
        def on_closing():
            root.destroy()

        new_window.protocol("WM_DELETE_WINDOW", on_closing)

        # Utwórz pole tekstowe w nowym oknie
        text_field = tk.Entry(new_window)
        text_field.pack(expand=True, fill=tk.BOTH)

        # Utwórz przyciski w nowym oknie
        dobrze_button = tk.Button(new_window, text="Dobrze", command=lambda: print("Przycisk Dobrze został naciśnięty"), bg="lightgreen")
        powrot_button = tk.Button(new_window, text="Powrót", command=go_back, bg="lightcoral")

        # Umieść przyciski w nowym oknie
        dobrze_button.pack(expand=True, fill=tk.BOTH)
        powrot_button.pack(expand=True, fill=tk.BOTH)

    fade_out()

# Utwórz główne okno
root = tk.Tk()
root.title("Wszystko dzięki Easy English!")

# Znacznie powiększ rozmiar okna
root.geometry("800x600")

# Funkcja do zakończenia programu po kliknięciu "X"
def on_closing():
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Zdefiniuj akcje przycisków
def start_action():
    print("Przycisk Start został naciśnięty")
    open_new_window()

def stop_action():
    print("Przycisk Stop został naciśnięty")

def pause_action():
    print("Przycisk Pauza została naciśnięta")

def end_action():
    print("Przycisk Koniec został naciśnięty")
    root.destroy()

# Utwórz przyciski
start_button = tk.Button(root, text="Start", command=start_action, bg="lightblue")
stop_button = tk.Button(root, text="Stop", command=stop_action, bg="lightyellow")
pause_button = tk.Button(root, text="Pauza", command=pause_action, bg="lightpink")
end_button = tk.Button(root, text="Koniec", command=end_action, bg="lightgray")

# Umieść przyciski w oknie w 2 rzędach po 2 przyciski w rzędzie
start_button.grid(row=0, column=0, sticky="nsew")
stop_button.grid(row=0, column=1, sticky="nsew")
pause_button.grid(row=1, column=0, sticky="nsew")
end_button.grid(row=1, column=1, sticky="nsew")

# Ustawienie proporcji kolumn i wierszy dla głównego okna
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

# Uruchom aplikację
root.mainloop()
