from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import requests
import xml.etree.ElementTree as ET
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


class Sokker:

    def __init__(self, login:str, password:str, season_number:int, round_number:int, country_code:str):
        self.login = login
        self.password = password
        self.season = season_number
        self.round = round_number
        self.country_code = country_code
        self.session = None


    def connect_to_sokker_xml(self):

        # Dane logowania
        login_data = {
            'ilogin': self.login,
            'ipassword': self.password
        }

        # URL do uwierzytelniania
        auth_url = 'https://sokker.org/start.php?session=xml'

        # Wysyłanie danych logowania metodą POST
        self.session = requests.Session()
        response = self.session.post(auth_url, data=login_data)

        # Sprawdzanie odpowiedzi
        if 'OK' in response.text:
            print("Uwierzytelnianie zakończone sukcesem.")
            return True
        else:
            print('Uwierzytelnianie nie powiodło się.')
            return False


    def get_season_and_round_xml(self):
        xml_url = 'https://sokker.org/xml/league-1-1-1.xml'

        # Jeśli brak sesji, spróbuj się zalogować
        if self.session is None:
            ok = self.connect_to_sokker_xml()
            if not ok:
                return None

        # Pobierz XML
        response = self.session.get(xml_url)
        if response.status_code != 200:
            print(f"Błąd pobierania XML: {response.status_code}")
            return None


        root = ET.fromstring(response.text)  # Parsujemy XML z tekstu
        info = root.find('info')  # Szukamy sekcji <info>

        season = int(info.find('season').text) if info.find('season') is not None else None
        round_ = int(info.find('round').text) if info.find('round') is not None else None

        self.season = season
        self.round = round_

        return {"season": season, "round": round_}




    def log_in_to_sokker(self):

        try:
            self.driver = webdriver.Chrome()
            self.driver.get('https://sokker.org/pl/')
            self.driver.maximize_window()

            # Akceptacja cookies
            WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div[1]/div/div/div[2]/button/span/span'))
            ).click()

            # Kliknięcie "Zaloguj się"
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//*[@id="__next"]/main/div[1]/div/section[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/a/span/span'))
            ).click()

            # Wpisanie loginu i hasła
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "login"))).send_keys(
                self.login)
            self.driver.find_element(By.NAME, 'password').send_keys(self.password)

            # Kliknięcie przycisku logowania
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div/div/div/div[5]/form/div[3]/div[1]/button'))
            ).click()

            print("✅ Logowanie zakończone sukcesem.")
        except Exception as e:
            print(f"❌ Błąd podczas logowania: {e}")

        sleep(5)





    def go_to_transfer_list(self):
        pass

    def look_through_players(self):
        pass



sokker_object = Sokker("asciutto", "harrypotter",1,1,"PL")

# print(sokker_object.get_season_and_round_xml())  # {'season': 75, 'round': 18}
# print(sokker_object.season)  # 75
# print(sokker_object.round)   # 18

sokker_object.log_in_to_sokker()