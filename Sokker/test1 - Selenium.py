from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import re


def fetch_ids_from_url(url, login_url):
    # Utwórz przeglądarkę
    driver = webdriver.Chrome()  # Upewnij się, że masz zainstalowany chromedriver

    try:
        # Przejdź do strony logowania
        driver.get(login_url)

        # Dodaj pauzę, aby użytkownik mógł samodzielnie wpisać dane do logowania
        input("Wpisz dane do logowania na stronie, a następnie naciśnij Enter, aby kontynuować...")

        # Przejdź do strony z ID
        driver.get(url)
        content = driver.page_source

        # Znajdź wszystkie ID w tagach <div>
        ids = re.findall(r'<div[^>]*>(\d+)</div>', content)

    finally:
        driver.quit()

    return ids


# Przykład użycia
url = 'https://sokker.org/transferSearch/trainer/0/pg/1/transfer_list/1/sort/end'  # Zamień na rzeczywisty URL strony, z której chcesz pobrać ID
login_url = 'https://sokker.org/pl/app/login/'  # URL strony logowania

ids = fetch_ids_from_url(url, login_url)
print(ids)