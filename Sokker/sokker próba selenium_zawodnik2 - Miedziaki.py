from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


# Tworzy instancję WebDrivera dla Chrome
driver = webdriver.Chrome()

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
player_list = []

# Przechodzenie na stronę każdego zawodnika z przerwą 2 sekundy
for player_id in unique_player_ids:
    player_url = f'https://sokker.org/player/PID/{player_id}'
    driver.get(player_url)

    try:
        # Czekaj na pojawienie się elementu i kliknij go, jeśli jest widoczny
        element = WebDriverWait(driver, 2).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[7]/div[2]/div[2]/div[2]/div[2]/button[1]/p')))
        element.click()
    except:
        pass

    skill_player_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/nav/div/div[1]/span')))
    skill_player = skill_player_element.text
    player_list.append(skill_player)

    skill_age_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/strong')))
    skill_age = skill_age_element.text
    player_list.append(skill_age)

    skill_kond_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[1]/strong/span')))
    skill_kond = skill_kond_element.text
    player_list.append(skill_kond)

    skill_szyb_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[1]/strong/span')))
    skill_szyb = skill_szyb_element.text
    player_list.append(skill_szyb)

    skill_tech_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[1]/strong/span')))
    skill_tech = skill_tech_element.text
    player_list.append(skill_tech)

    skill_pod_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[1]/strong/span')))
    skill_pod = skill_pod_element.text
    player_list.append(skill_pod)

    skill_gk_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td[2]/strong/span')))
    skill_gk = skill_gk_element.text
    player_list.append(skill_gk)

    skill_def_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/strong/span')))
    skill_def = skill_def_element.text
    player_list.append(skill_def)

    skill_mid_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[3]/td[2]/strong/span')))
    skill_mid = skill_mid_element.text
    player_list.append(skill_mid)

    skill_att_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/strong/span')))
    skill_att = skill_att_element.text
    player_list.append(skill_att)

    sleep(1)

print(player_list)




# Initialize empty lists for each column
names = []
ids = []
age = []
kon = []
szyb = []
tech = []
pod = []
gk = []
def_ = []
mid = []
att = []

# Iterate through the player list and extract data
for i in range(0, len(player_list), 10):
    name_id = player_list[i].split('[')
    names.append(name_id[0].strip())
    ids.append(int(name_id[-1].strip(' ]')))
    age.append(int(player_list[i+1].strip('[]')))
    kon.append(int(player_list[i+2].strip('[]')))
    szyb.append(int(player_list[i+3].strip('[]')))
    tech.append(int(player_list[i+4].strip('[]')))
    pod.append(int(player_list[i+5].strip('[]')))
    gk.append(int(player_list[i+6].strip('[]')))
    def_.append(int(player_list[i+7].strip('[]')))
    mid.append(int(player_list[i+8].strip('[]')))
    att.append(int(player_list[i+9].strip('[]')))

# Create a DataFrame
df = pd.DataFrame({
    'Name': names,
    'ID': ids,
    'Age': age,
    'Kon': kon,
    'Szyb': szyb,
    'Tech': tech,
    'Pod': pod,
    'GK': gk,
    'DEF': def_,
    'MID': mid,
    'ATT': att
})

# Save the DataFrame to an Excel file
file_path = r'C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker - wyciąganie informacji o zawodnikach\\Dane.xlsx'
df.to_excel(file_path, index=False)

print(f"Data has been successfully saved to {file_path}")