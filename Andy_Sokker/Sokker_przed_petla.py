import re
from time import sleep
import requests
import xml.etree.ElementTree as ET
from selenium.webdriver.common.by import By
from selenium import webdriver

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Player import Player


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

        sleep(2)


    def go_to_transfer_list(self):

        self.log_in_to_sokker()

        # Przycisk transfery
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[7]'))).click()
        sleep(2)

        # przycisk szukaj w grupie zawodnicy
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div/main/div[3]/div[2]/div/div[2]/div/div/div/div[3]/a/span/span'))).click()
        sleep(2)

        # ciasteczka do kliknięcia
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/div[7]/div[2]/div[2]/div[2]/div[2]/button[1]/p'))).click()
        sleep(2)

        # przycisk wyszukaj otwierajacy liste wszystkich zawodnikow na sprzedaz
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/form/div[6]/div[2]/div/div/button[1]'))).click()
        sleep(2)



        # sekcje poniżej wyciągają wszystkie dane o pierwszym zawodniku z listy rozwijanej

    # season & round
        sokker_object = Sokker("asciutto", "harrypotter",1,1,"PL")
        sokker_object.get_season_and_round_xml()
        Season = sokker_object.season
        Round = sokker_object.round

    # ID
        wait = WebDriverWait(self.driver, 15)
        player_ids_links = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='player/PID/']")))

        # Weź pierwszy link i wyciągnij PID z href
        first_href = player_ids_links[0].get_attribute("href") # tutaj cyfra w nawiasie oznacza gracza, którego z kolei ID pobieramy

        # przykładowe href wygląda jak: https://.../player/PID/39995064
        pid_match = re.search(r"/player/PID/(\d{8})", first_href)
        ID = pid_match.group(1) # tu nie zmieniamy jedynki w nawiasie


    # Name
        Name = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[2]/div/a').text.strip()

    # TeamID, CountryID, Matches, Goals, Assists
        xml_url = f"https://sokker.org/xml/player-{ID}.xml"

        # Jeśli brak sesji, spróbuj się zalogować
        if self.session is None:
            ok = self.connect_to_sokker_xml()
            if not ok:
                return None

        # Pobierz XML
        response = self.session.get(xml_url)
        if response.status_code != 200:
            print(f"Błąd pobierania XML ({xml_url}): {response.status_code}")
            return None

        # Parsowanie XML
        root = ET.fromstring(response.text)  # root = <player>

        # Bezpośrednie pobranie wartości
        Team_ID = int(root.find('teamID').text)
        Country_ID = int(root.find('countryID').text)
        Matches = int(root.find('matches').text)
        Goals = int(root.find('goals').text)
        Assists = int(root.find('assists').text)

        # Zapisywanie w obiekcie
        self.team_id = Team_ID
        self.country_id = Country_ID
        self.matches = Matches
        self.goals = Goals
        self.assists = Assists


    # Age
        # Poczekaj na blok zawierający "wiek" (pierwszy zawodnik)
        raw_age_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//div[contains(.,'wiek')])[1]")))
        # Pobierz tekst całego bloku, np. "39995064[Knut Dreher] , wiek 16 wartość: ..."
        text_age = raw_age_element.text
        # Wyciągnij liczbę po słowie "wiek"
        match_age = re.search(r"wiek\s+(\d+)", text_age)
        Age = int(match_age.group(1))  # np. 16

    # Value
        raw_Value = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/strong[1]').text.strip()
        Value = re.sub(r'\D', '', raw_Value) # usuwa wszystko, co nie jest cyfrą

    # Salary
        raw_Salary = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/strong[2]').text.strip()
        Salary = re.sub(r'\D', '', raw_Salary) # usuwa wszystko, co nie jest cyfrą


    # Price
        # Znajdź kwotę dla pierwszego zawodnika (samą wartość z <span>)
        # [1] oznacza pierwszy zawodnik na liście
        raw_price_element = self.driver.find_element(By.XPATH,"(//strong[contains(text(),'Aktualna oferta') or contains(text(),'Wystawiony za')]/span)[1]")

        # Pobierz tekst z <span>, np. "40 000 zł" lub "1 zł"
        text = raw_price_element.text

        # Zabezpieczenie: usuń "zł", niełamliwe spacje itp.
        # \xa0 to niełamliwa spacja (NBSP), która często występuje w HTML
        clean_text = (
            text.replace("zł", "")
            .replace("\xa0", " ")
            .strip())

        # Spróbuj znaleźć liczbę (z ewentualnymi spacjami jako separatorami tysięcy)
        match = re.search(r"\d[\d\s]*", clean_text)
        raw_price2 = match.group()  # np. "40 000"
        Price = raw_price2.replace(" ", "")  # usuń spacje -> "40000"




        EndOfSale = self.driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[3]/strong[4]').text.strip()

        raw_Stamina = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/td[1]/strong/span').text.strip()
        Stamina = re.sub(r'\D', '', raw_Stamina)  # usuwa wszystko, co nie jest cyfrą

        raw_Speed = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[2]/td[1]/strong/span').text.strip()
        Speed = re.sub(r'\D', '', raw_Speed)  # usuwa wszystko, co nie jest cyfrą

        raw_Technique = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[3]/td[1]/strong/span').text.strip()
        Technique = re.sub(r'\D', '', raw_Technique)  # usuwa wszystko, co nie jest cyfrą

        raw_Passing = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[4]/td[1]/strong/span').text.strip()
        Passing = re.sub(r'\D', '', raw_Passing)  # usuwa wszystko, co nie jest cyfrą

        raw_GK = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[1]/td[2]/strong/span').text.strip()
        GK = re.sub(r'\D', '', raw_GK)  # usuwa wszystko, co nie jest cyfrą

        raw_DEF = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[2]/td[2]/strong/span').text.strip()
        DEF = re.sub(r'\D', '', raw_DEF)  # usuwa wszystko, co nie jest cyfrą

        raw_MID = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[3]/td[2]/strong/span').text.strip()
        MID = re.sub(r'\D', '', raw_MID)  # usuwa wszystko, co nie jest cyfrą

        raw_ATT = self.driver.find_element(By.XPATH,'/html/body/main/div/div[2]/div[2]/div[2]/div[1]/div/div[4]/table/tbody/tr[4]/td[2]/strong/span').text.strip()
        ATT = re.sub(r'\D', '', raw_ATT)  # usuwa wszystko, co nie jest cyfrą


        return Season, Round, ID, Name, Team_ID, Age, Country_ID, Salary, Price, Value, EndOfSale, Matches, Goals, Assists, Stamina, Speed, Technique, Passing, GK, DEF, MID, ATT



# sokker_object = Sokker("asciutto", "harrypotter",1,1,"PL")

# print(sokker_object.get_season_and_round_xml())  # {'season': 75, 'round': 18}
# print(sokker_object.season)  # 75
# print(sokker_object.round)   # 18

# sokker_object.log_in_to_sokker()

# player1_to_database = Player()
# Sokker.go_to_transfer_list