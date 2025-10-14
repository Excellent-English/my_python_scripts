import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

# Funkcja do pobierania losowego obrazu z Pixabay na podstawie słowa kluczowego
def fetch_random_image(keyword):
    api_key = "35159665-9140877fb01020f2ff73f08cb"
    url = f"https://pixabay.com/api/?key={api_key}&q={keyword}&image_type=photo"
    response = requests.get(url)
    data = response.json()
    if data['hits']:
        image_url = random.choice(data['hits'])['webformatURL']
        response = requests.get(image_url)
        return Image.open(BytesIO(response.content))
    else:
        return None

# Funkcja do aktualizacji obrazu na przycisku
def update_image():
    keyword = entry.get()
    new_image = fetch_random_image(keyword)
    if new_image:
        resized_image = new_image.resize((200, 200), Image.LANCZOS)
        image = ImageTk.PhotoImage(resized_image)
        button.configure(image=image)
        button.image = image

# Stwórz główne okno
root = ctk.CTk()

# Dodaj entry box na górze okna
entry = ctk.CTkEntry(root, placeholder_text="Wpisz hasło")
entry.pack(pady=10, padx=10)

# Dodaj przycisk "Kliknij" obok entry box
click_button = ctk.CTkButton(root, text="Kliknij", command=update_image)
click_button.pack(pady=10, padx=10)

# Załaduj i zmień rozmiar obrazu
original_image = Image.open("fall-7863868_1920.jpg")
resized_image = original_image.resize((200, 200), Image.LANCZOS)
image = ImageTk.PhotoImage(resized_image)

# Stwórz przycisk z obrazem jako tło
button = ctk.CTkButton(root, image=image, text="", width=200, height=200, fg_color="transparent")
button.pack(pady=20, padx=20)

# Uruchom aplikację
root.mainloop()