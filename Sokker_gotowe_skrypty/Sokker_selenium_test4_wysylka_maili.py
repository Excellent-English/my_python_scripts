from smtplib import SMTP_SSL
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.chrome.options import Options

# region Standardowe kroki do uruchomienia Sokkera
# Tworzy instancję WebDrivera dla Chrome
driver = webdriver.Chrome()
# chrome_options = Options()
# chrome_options.add_argument('--headless=new')
# chrome_options.add_argument('--window-size=1920,1080')
# driver = webdriver.Chrome(options=chrome_options)

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

sleep(3)
# Przycisk transfery
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[7]'))).click()
# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul[1]/li[7]/a/span[2]'))).click()


#przycisk szukaj w grupie zawodnicy
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[3]/div[2]/div/div[2]/div/div/div/div[3]/a/span/span'))).click()
# WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#__next > main > div.layout__main > div:nth-child(2) > div > div.view-transfers__search-player > div > div > div > div.transfers-search-box__btn > a'))).click()

#wybierz Białoruś oraz wiek maksymalny 21
select_element = driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/form/div[3]/div[3]/div/div/select')
select = Select(select_element)
select.select_by_visible_text("Belarus")
driver.find_element(By.NAME, 'age_max').send_keys('21')

#przycisk wyszukaj otwierajacy liste wszystkich zawodnikow na sprzedaz
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/form/div[6]/div[2]/div/div/button[1]'))).click()
# endregion

# region Pobieranie danych zawodników
players = driver.find_elements(By.XPATH, '/html/body/main/div/div[2]/div[3]/div[2]/div')
liczba_zawodnikow = len(players)

email_body = ""

for i in range(1, liczba_zawodnikow + 1):
    id_xpath = f'/html/body/main/div/div[2]/div[3]/div[2]/div[{i}]/div/div[1]'
    base_xpath = f'/html/body/main/div/div[2]/div[3]/div[2]/div[{i}]/div'

    id_element = driver.find_element(By.XPATH, id_xpath)
    ID = id_element.get_attribute("textContent").strip()

    name = driver.find_element(By.XPATH, f'{base_xpath}/div[2]/div/a').text.strip()
    age_text = driver.find_element(By.XPATH, f'{base_xpath}/div[2]/div').text.strip()
    age = age_text[-2:]
    price = driver.find_element(By.XPATH, f'{base_xpath}/div[3]/strong[3]/span').text.strip()
    end_time = driver.find_element(By.XPATH, f'{base_xpath}/div[3]/strong[4]').text.strip()

    kondycja = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[1]/td[1]/strong').text.strip()
    bramkarz = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[1]/td[2]/strong').text.strip()
    szybkosc = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[2]/td[1]/strong').text.strip()
    obronca = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[2]/td[2]/strong').text.strip()
    technika = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[3]/td[1]/strong').text.strip()
    rozgrywajacy = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[3]/td[2]/strong').text.strip()
    podania = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[4]/td[1]/strong').text.strip()
    strzelec = driver.find_element(By.XPATH, f'{base_xpath}/div[4]/table/tbody/tr[4]/td[2]/strong').text.strip()

    email_body += f"{ID}\t{name}\t\tWiek: {age}\n"
    email_body += f"Aktualna kwota: {price}\n"
    email_body += f"Koniec licytacji: {end_time}\n\n"
    email_body += f"{kondycja} kondycja\t\t{bramkarz} bramkarz\n"
    email_body += f"{szybkosc} szybkość\t\t{obronca} obrońca\n"
    email_body += f"{technika} technika\t\t{rozgrywajacy} rozgrywający\n"
    email_body += f"{podania} podania\t\t{strzelec} strzelec\n"
    email_body += "-" * 80 + "\n"
# endregion

# region Tworzenie maila na podstawie znalezionych informacji

smtp_server = "smtp.iq.pl"
smtp_port = 465
sender_email = "biuro@excellentenglish.pl"
receiver_email = "piotr.szczubiala@fresenius-kabi.com"
password = "Harrypotter1"

msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = "Sokker BY players on sale"

msg.attach(MIMEText(email_body, "plain"))

with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
# endregion