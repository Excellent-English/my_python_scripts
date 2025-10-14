import customtkinter as ctk

def on_label_click(event):
    label_text = event.widget.cget('text')
    status_label.configure(text=f"You clicked on {label_text}!")

# Tworzenie głównego okna
root = ctk.CTk()
root.geometry("400x250")
root.title("Interactive Labels")

# Tworzenie ramki, aby umieścić labele obok siebie
frame = ctk.CTkFrame(root)
frame.pack(pady=20)

# Tworzenie trzech labeli
label1 = ctk.CTkLabel(frame, text="Label 1")
label1.grid(row=0, column=0, padx=10)
label1.bind("<Button-1>", on_label_click)

label2 = ctk.CTkLabel(frame, text="Label 2")
label2.grid(row=0, column=1, padx=10)
label2.bind("<Button-1>", on_label_click)

label3 = ctk.CTkLabel(frame, text="Label 3")
label3.grid(row=0, column=2, padx=10)
label3.bind("<Button-1>", on_label_click)

# Tworzenie etykiety statusu, która będzie pokazywać informacje o kliknięciu
status_label = ctk.CTkLabel(root, text="Click on any label above", height=30)
status_label.pack(pady=20, fill="x", padx=20)

# Uruchomienie głównej pętli aplikacji
root.mainloop()