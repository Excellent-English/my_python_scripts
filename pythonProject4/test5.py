# root.geometry("600x400")
#
#
# # Utwórz frame o zwiększonych wymiarach
# frame = ctk.CTkFrame(master=root, width=150, height=150)
# frame.pack(pady=20, padx=20)
#
# # Utwórz label wewnątrz frame
# label_dla_tekstu = ctk.CTkLabel(master=frame, text="Pierwszy test")
# label_dla_tekstu.pack(pady=10, padx=10)
#
# # Pobierz tekst z etykiety i przypisz go do zmiennej
# tekst_wewnatrz_label = label_dla_tekstu.cget("text")
#
# # Wydrukuj tekst na początku skryptu
# print(f'To jest tekst na początku skryptu: {tekst_wewnatrz_label}')
#
# tekst_wewnatrz_label = "Drugi test"
# label_dla_tekstu.configure(text=tekst_wewnatrz_label)
#
# print(f'To jest tekst na końcu skryptu: {tekst_wewnatrz_label}')
#
#
# # Dodaj miejsce do wpisywania tekstu (Entry)
# entry = ctk.CTkEntry(master=root)
# entry.pack(pady=10)
#
# # Funkcja do pobrania tekstu z Entry i przypisania go do zmiennej
# def update_label():
#     tekst_wewnatrz_label = entry.get()
#     label_dla_tekstu.configure(text=tekst_wewnatrz_label)
#     print(f'Nowy tekst po drugiej próbie: {tekst_wewnatrz_label}')
#
# # Utwórz przycisk1
# button1 = ctk.CTkButton(master=root, text="Sprawdź", command=update_label)
# button1.pack(pady=10)
#
# # Uruchom aplikację
# root.mainloop()
import customtkinter as ctk

# Utwórz główne okno o określonych wymiarach
root = ctk.CTk()
root.title("Przykładowe GUI")
