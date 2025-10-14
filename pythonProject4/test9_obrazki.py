import os
import sys
import customtkinter as ctk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random


# Funkcja do pobierania losowego obrazu z Pixabay na podstawie słowa kluczowego--------------------------------------
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


# Funkcja do aktualizacji obrazów na przyciskach---------------------------------------------------------------------
def update_images():
    keyword = entry.get()
    new_image1 = fetch_random_image(keyword)
    new_image2 = fetch_random_image(keyword)
    new_image3 = fetch_random_image(keyword)

    if new_image1:
        resized_image1 = new_image1.resize((150, 150), Image.LANCZOS)
        image1 = ImageTk.PhotoImage(resized_image1)
        button1.configure(image=image1)
        button1.image = image1

    if new_image2:
        resized_image2 = new_image2.resize((150, 150), Image.LANCZOS)
        image2 = ImageTk.PhotoImage(resized_image2)
        button2.configure(image=image2)
        button2.image = image2

    if new_image3:
        resized_image3 = new_image3.resize((150, 150), Image.LANCZOS)
        image3 = ImageTk.PhotoImage(resized_image3)
        button3.configure(image=image3)
        button3.image = image3


# Wygląd głównego okna------------------------------------------------------------------------------------------------
# Stwórz główne okno
root = ctk.CTk()
root.geometry('600x400')

# Dodaj entry box na górze okna
entry = ctk.CTkEntry(root, placeholder_text="Wpisz hasło")
entry.pack(pady=10, padx=10)

# Dodaj przycisk "Kliknij" obok entry box
click_button = ctk.CTkButton(root, text="Kliknij", command=update_images)
click_button.pack(pady=10, padx=10)

# Załaduj i zmień rozmiar obrazu
original_image = Image.open("fall-7863868_1920.jpg")
resized_image = original_image.resize((150, 150), Image.LANCZOS)
image = ImageTk.PhotoImage(resized_image)


# ramka + 3 przyciski-------------------------------------------------------------------------------------------------
# Stwórz ramkę do przycisków z obrazami
frame = ctk.CTkFrame(root)
frame.pack(pady=20, padx=20)

# Stwórz przyciski z obrazem jako tło i umieść je obok siebie
button1 = ctk.CTkButton(frame, image=image, text="", width=150, height=150, fg_color="transparent")
button1.pack(side="left", padx=10)

button2 = ctk.CTkButton(frame, image=image, text="", width=150, height=150, fg_color="transparent")
button2.pack(side="left", padx=10)

button3 = ctk.CTkButton(frame, image=image, text="", width=150, height=150, fg_color="transparent")
button3.pack(side="left", padx=10)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image_path = resource_path("fall-7863868_1920.jpg")

# Uruchom aplikację--------------------------------------------------------------------------------------------------
root.mainloop()