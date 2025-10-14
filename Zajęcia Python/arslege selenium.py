from time import sleep
from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# region Podstawowe operacje na stronie internetowej
# Tworzy instancję WebDrivera dla Chrome
driver = webdriver.Chrome()

# Otwiera stronę internetową
driver.get('https://arslege.pl/')

# Maksymalizuje okno przeglądarki
driver.maximize_window()

# Klika na "logowanie" u góry ekranu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > header > div.container_16.clearfix > div.user_menu_holder > nav > ul > li:nth-child(3) > a'))).click()

# Wypełnianie loginu i hasła do strony
driver.find_element(By.NAME, 'email').send_keys('szczubiala@interia.pl')
driver.find_element(By.NAME, 'password').send_keys('gadugg')

# Klika na politykę cookies
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#cookiesPolicy > span > b'))).click()
except TimeoutException:
    pass

# Klika na przycisk "Zaloguj się"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > main > div:nth-child(4) > div > section > form > table > tbody > tr:nth-child(3) > td.form2 > button'))).click()
sleep(3)

# Klika na politykę cookies
try:
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#cookiesPolicy > span > b'))).click()
except TimeoutException:
    pass

# Klika na "Aplikacja adwokacja i radcowska" u dołu ekranu
WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'body > footer > section.container_16.clearfix.footer_content_holder > div:nth-child(3) > ul > li:nth-child(1) > a'))).click()

# Klika na "Rozwiąż" obok testów na egzamin próbny
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#tabs_content > div.active > section:nth-child(2) > div.box_right > div.click'))).click()
# endregion

# region Operacje związane ze zmianą liczby pytań na teście
# Znajdź wszystkie iframe'y
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"🔍 Znaleziono {len(iframes)} iframe'ów.")

found = False

# Iteruj po iframe'ach i szukaj listy rozwijanej
for index, iframe in enumerate(iframes):
    driver.switch_to.default_content()  # wróć do głównego DOM
    driver.switch_to.frame(iframe)
    print(f"➡️ Sprawdzam iframe nr {index}...")

    try:
        # Czekaj na widoczność elementu
        select_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.NAME, 't_questions_cnt')))
        select = Select(select_element)
        select.select_by_visible_text("150")
        print("✅ Wybrano opcję '150'!")
        found = True
        break
    except TimeoutException:
        print(f"❌ Lista nie znaleziona w iframe nr {index} (Timeout)")
    except Exception as e:
        print(f"⚠️ Błąd w iframe nr {index}: {e}")

# Jeśli nie znaleziono
if not found:
    print("⚠️ Nie znaleziono listy rozwijanej w żadnym iframe.")
# endregion

# Kliknięcie na przycisk "Dalej"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#testForm1 > div:nth-child(9) > button'))).click()

# Kliknięcie na przycisk "Rozwiąż"
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#testForm2 > fieldset > div:nth-child(5) > button'))).click()

# Kliknięcie na pierwszą odpowiedź
# Poczekaj na załadowanie odpowiedzi
first_answer = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CLASS_NAME, "answer_text")))
first_answer.click()

sleep(3)