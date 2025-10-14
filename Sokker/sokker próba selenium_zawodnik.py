from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tworzy instancję WebDrivera dla Chrome
driver = webdriver.Chrome()

try:
    # Otwiera stronę internetową
    driver.get('https://sokker.org/pl/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div[1]/div/div/div[2]/button/span/span'))).click()

    # Maksymalizuje okno przeglądarki
    driver.maximize_window()

    # Przycisk klikający na "zaloguj się"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[1]/div/section[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/a/span/span'))).click()

    # Wypełnianie loginu i hasła do strony
    driver.find_element(By.NAME, 'login').send_keys('asciutto')
    driver.find_element(By.NAME, 'password').send_keys('harrypotter')

    # Klikanie na przycisk do zalogowania się
    login_button = driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div[2]/div/div/div/div[5]/form/div[3]/div[1]/button')
    login_button.send_keys(webdriver.Keys.ENTER)

    # Przycisk zawodnicy
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[2]'))).click()

    # Znajdowanie wszystkich linków zawierających "player/PID/"
    links = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[href*="player/PID/"]')))

    # Wyciąganie ID zawodników z linków
    player_ids = [link.get_attribute('href').split('player/PID/')[1] for link in links]

    # Usuwanie duplikatów
    unique_player_ids = list(set(player_ids))

    # Wyświetlanie listy unikalnych ID zawodników
    print("Unique Player IDs:", unique_player_ids)

    # Lista do przechowywania wartości skill_kond
    skill_kond_list = []

    # Przechodzenie na stronę każdego zawodnika z przerwą 2 sekundy
    for player_id in unique_player_ids:
        player_url = f'https://sokker.org/player/PID/{player_id}'
        driver.get(player_url)

    # Wyciąganie wartości tekstowej z elementu HTML związanego z kondycją
        skill_kond_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/strong/span')))
        skill_kond = skill_kond_element.text
        skill_kond_list.append(skill_kond)

    # Wyświetlanie listy wartości skill_kond
    print("Lista wartości skill_kond:", skill_kond_list)
    # Przekształcenie listy na zawierającą tylko wartości liczbowe
    numeric_values = []
    for value in skill_kond_list:
        stripped_value = value.strip('[]')
        if stripped_value.isdigit():
            numeric_values.append(int(stripped_value))
    print(numeric_values)

finally:
    # Zamknięcie przeglądarki
    driver.quit()
