from time import sleep
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re

player_id = input("Wprowadź ID zawodnika, którego chcesz sprawdzić: ")

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

player_url = f'https://sokker.org/player/PID/{player_id}'
driver.get(player_url)


try:
    name_and_surname = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/a')))
except TimeoutException:
    print("Timeout error occurred. Skipping this category: name_and_surname")

try:
    age = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/strong')))
except TimeoutException:
    print("Timeout error occurred. Skipping this category: age")






print(name_and_surname.text)
print(age.text)




#
# # Lista do przechowywania wszystkich unikalnych ID zawodników
# all_player_ids = set()
#
# # Funkcja do wczytywania IDs z pliku i zwracania ich jako lista
# def read_ids_from_file(file_name):
#     with open(file_name, 'r') as file:
#         ids = file.read().splitlines()
#     return ids
#
# # Wczytaj IDs z pliku Belarus.txt i zapisz je w liście o nazwie all_player_ids
# # all_player_ids = read_ids_from_file('Belarus.txt')
# all_player_ids = read_ids_from_file('C:\\Users\\PSzczubiala\\Desktop\\SK\\Sokker - wyciąganie informacji o zawodnikach\\BY\\Belarus.txt')
# print(all_player_ids)
#
# # Wyświetlanie listy unikalnych ID zawodników
# print("Unique Player IDs:", list(all_player_ids))
# print("Liczba zawodników do odszukania: ", len(all_player_ids))
#
# # Lista do przechowywania wartości zawodników
# player_list = []
# sleep(3)
#
#
# # Przechodzenie na stronę każdego zawodnika
# for index, player_id in enumerate(all_player_ids):
#     player_url = f'https://sokker.org/player/PID/{player_id}'
#     driver.get(player_url)
#     print(f'Aktualnie przetwarzam zawodnika: {index + 1} / {len(all_player_ids)}')
#
#     try:
#         # Czekaj na pojawienie się elementu i kliknij go, jeśli jest widoczny
#         element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[2]/div[2]/div[2]/button[1]/p')))
#         element.click()
#     except:
#         pass
#
#     # Zbierz informację o poszczególnych polach, zaczynając od imienia, nazwiska i ID:
#     try:
#         skill_player_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/nav/div/div[1]/span')))
#         skill_player = skill_player_element.text
#         player_list.append(skill_player)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_player")
#
#     try:
#         skill_age_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/strong')))
#         skill_age = skill_age_element.text
#         player_list.append(skill_age)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_age")
#
#     # Zbierz informacje o 8 skillach zawodników
#     try:
#         skill_kond_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(1) > td:nth-child(1) > strong > span')))
#         skill_kond = skill_kond_element.text
#         player_list.append(skill_kond)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_kond")
#
#     try:
#         skill_szyb_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(2) > td:nth-child(1) > strong > span')))
#         skill_szyb = skill_szyb_element.text
#         player_list.append(skill_szyb)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_szyb")
#
#     try:
#         skill_tech_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(3) > td:nth-child(1) > strong > span')))
#         skill_tech = skill_tech_element.text
#         player_list.append(skill_tech)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_tech")
#
#     try:
#         skill_pod_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(4) > td:nth-child(1) > strong > span')))
#         skill_pod = skill_pod_element.text
#         player_list.append(skill_pod)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_pod")
#
#     try:
#         skill_gk_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(1) > td:nth-child(2) > strong > span')))
#         skill_gk = skill_gk_element.text
#         player_list.append(skill_gk)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_gk")
#
#     try:
#         skill_def_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(2) > td:nth-child(2) > strong > span')))
#         skill_def = skill_def_element.text
#         player_list.append(skill_def)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_def")
#
#     try:
#         skill_mid_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(3) > td:nth-child(2) > strong > span')))
#         skill_mid = skill_mid_element.text
#         player_list.append(skill_mid)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_mid")
#
#     try:
#         skill_att_element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#body-player > main > div > div.l-main__inner > div.row > div:nth-child(1) > div:nth-child(1) > div.panel-body.hidden-xs > table > tbody > tr:nth-child(4) > td:nth-child(2) > strong > span')))
#         skill_att = skill_att_element.text
#         player_list.append(skill_att)
#     except TimeoutException:
#         print("Timeout error occurred. Skipping this category: skill_att")
#
#     sleep(0.3)
#
# print(player_list)
#
#
#
# # Procedura związana z wyciągnięciem elementów listy player_list do pliku Excela, wraz z obrobieniem wartości
# # Initialize empty lists for each column
# names = []
# ids = []
# age = []
# kon = []
# szyb = []
# tech = []
# pod = []
# gk = []
# def_ = []
# mid = []
# att = []
#
#
# # Iterate through the player list and extract data
# for i in range(0, len(player_list), 10):
#     # Rozdziel nazwę i ID gracza
#     name_id = player_list[i].split('[')
#     names.append(name_id[0].strip())  # Dodaj nazwę gracza do listy names
#     ids.append(int(re.search(r'\d+', name_id[-1]).group()))  # Dodaj ID gracza do listy ids
#
#     # Dodaj wiek gracza do listy age
#     age.append(int(re.search(r'\d+', player_list[i + 1]).group()))
#
#     # Dodaj różne atrybuty gracza do odpowiednich list
#     kon.append(int(re.search(r'\d+', player_list[i + 2]).group()))
#     szyb.append(int(re.search(r'\d+', player_list[i + 3]).group()))
#     tech.append(int(re.search(r'\d+', player_list[i + 4]).group()))
#     pod.append(int(re.search(r'\d+', player_list[i + 5]).group()))
#     gk.append(int(re.search(r'\d+', player_list[i + 6]).group()))
#     def_.append(int(re.search(r'\d+', player_list[i + 7]).group()))
#     mid.append(int(re.search(r'\d+', player_list[i + 8]).group()))
#     att.append(int(re.search(r'\d+', player_list[i + 9]).group()))
#
#
# # # Iterate through the player list and extract data
# # for i in range(0, len(player_list), 10):
# #     # Rozdziel nazwę i ID gracza
# #     name_id = player_list[i].split('[')
# #     names.append(name_id[0].strip())  # Dodaj nazwę gracza do listy names
# #     ids.append(int(name_id[-1].strip(' ]')))  # Dodaj ID gracza do listy ids
# #     # Dodaj wiek gracza do listy age
# #     age.append(int(player_list[i + 1].strip('[]')))
# #     # Dodaj różne atrybuty gracza do odpowiednich list
# #     kon.append(int(player_list[i + 2].strip('[]')))
# #     szyb.append(int(player_list[i + 3].strip('[]')))
# #     tech.append(int(player_list[i + 4].strip('[]')))
# #     pod.append(int(player_list[i + 5].strip('[]')))
# #     gk.append(int(player_list[i + 6].strip('[]')))
# #     def_.append(int(player_list[i + 7].strip('[]')))
# #     mid.append(int(player_list[i + 8].strip('[]')))
# #     att.append(int(player_list[i + 9].strip('[]')))
#
# # Create a DataFrame
# df = pd.DataFrame({
#     'Name': names,
#     'ID': ids,
#     'Age': age,
#     'Kon': kon,
#     'Szyb': szyb,
#     'Tech': tech,
#     'Pod': pod,
#     'GK': gk,
#     'DEF': def_,
#     'MID': mid,
#     'ATT': att
# })
#
# # Save the DataFrame to an Excel file
# file_path = r'C:\\Users\\PSzczubiala\\Desktop\\SK\\Sokker - wyciąganie informacji o zawodnikach\\Belarus U-21.xlsx'
# df.to_excel(file_path, index=False)
#
# print(f"Data has been successfully saved to {file_path}")