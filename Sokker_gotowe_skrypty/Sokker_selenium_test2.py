from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

# region Standardowe kroki do uruchomienia Sokkera
# Tworzy instancję WebDrivera dla Chrome
driver = webdriver.Chrome()

# Otwiera stronę internetową
driver.get('https://sokker.org/pl/')
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div[1]/div/div/div[2]/button/span/span'))).click()

# Maksymalizuje okno przeglądarki
driver.maximize_window()

# Przycisk klikający na "zaloguj się"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#__next > main > div:nth-child(1) > div > section.hero > div.hero__inner > div.hero__footer > div.hero__cta > div.hero__actions-btns > div > div:nth-child(2) > a > span > span'))).click()

# Wypełnianie loginu i hasła do strony
driver.find_element(By.NAME, 'login').send_keys('asciutto')
driver.find_element(By.NAME, 'password').send_keys('harrypotter')

# Klikanie na przycisk do zalogowania się
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div/div/div/div[5]/form/div[3]/div[1]/button'))).click()

# Przycisk transfery
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[7]'))).click()

#przycisk szukaj w grupie zawodnicy
sleep(1)
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[3]/div[2]/div/div[2]/div/div/div/div[3]/a/span/span'))).click()

#przycisk wyszukaj otwierajacy liste wszystkich zawodnikow na sprzedaz
sleep(1)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/form/div[6]/div[2]/div/div/button[1]'))).click()
# endregion

# region Pobieranie danych od zawodnika
# region ID_zawodnika
try:
    player_ID = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[1]')))
    ID_zawodnika = player_ID.get_attribute("textContent").strip()
except TimeoutException:
    print("Timeout error occurred. Skipping this category: player_ID")
# endregion

# region Imie_nazwisko
try:
    name_and_surname = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div/a')))
    imie_nazwisko = name_and_surname.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: name_and_surname")
# endregion

# region Wiek
try:
    age = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[2]/div')))
    full_age = age.text
    wiek = full_age[-2:]
except TimeoutException:
    print("Timeout error occurred. Skipping this category: age")
# endregion

# region Kwota
try:
    amount = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[3]/strong[3]/span')))
    kwota = amount.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: amount")
# endregion

# region Koniec licytacji
try:
    end_time = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[3]/strong[4]')))
    koniec_licytacji = end_time.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: end_time")
# endregion

# region Kondycja
try:
    stamina = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/strong')))
    kondycja = stamina.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: stamina")
# endregion

# region Bramkarz
try:
    gk = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/td[2]/strong')))
    bramkarz = gk.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: goalkeeper")
# endregion

# region Szybkość
try:
    speed = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[2]/td[1]/strong')))
    szybkosc = speed.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: speed")
# endregion

# region Obrońca
try:
    defender = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[2]/td[2]/strong')))
    obronca = defender.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: defender")
# endregion

# region Technika
try:
    tech = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[3]/td[1]/strong')))
    technika = tech.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: technique")
# endregion

# region Rozgrywający
try:
    mid = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[3]/td[2]/strong')))
    rozgrywajacy = mid.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: midfielder")
# endregion

# region Podania
try:
    passes = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[4]/td[1]/strong')))
    podania = passes.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: passes")
# endregion

# region Strzelec
try:
    striker = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div[1]/div/div[4]/table/tbody/tr[4]/td[2]/strong')))
    strzelec = striker.text
except TimeoutException:
    print("Timeout error occurred. Skipping this category: striker")
# endregion
# endregion




print(f"{ID_zawodnika}\t{imie_nazwisko}\t\tWiek: {wiek}")
print(f"Aktualna kwota: {kwota}")
print(f"Koniec licytacji: {koniec_licytacji}")
print()

print(f"{kondycja} kondycja\t\t{bramkarz} bramkarz")
print(f"{szybkosc} szybkość\t\t{obronca} obrońca")
print(f"{technika} technika\t\t{rozgrywajacy} rozgrywający")
print(f"{podania} podania\t\t{strzelec} strzelec")

sleep(5)