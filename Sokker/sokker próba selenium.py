from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://sokker.org/pl/')
time.sleep(2)

driver.maximize_window()
time.sleep(1)

#przycisk akceptujacy ciasteczka
driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div[1]/div/div/div[2]/button/span/span').click()
time.sleep(2)

#przycisk klikajacy na "zaloguj sie"
driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/section[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/a/span/span').click()
time.sleep(2)

#wypelnianie loginu i hasla do strony
driver.find_element(By.NAME, 'login').send_keys('asciutto')
driver.find_element(By.NAME, 'password').send_keys('harrypotter')

#klikanie na przycisk do zalogowania sie
login_button = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div/div[2]/div/div/div/div[5]/form/div[3]/div[1]/button')
login_button.send_keys(webdriver.Keys.ENTER)

#przycisk transfery
time.sleep(5)
driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div/div/div[2]/div/div[2]/div[1]/div[1]/ul/li[7]').click()

#przycisk szukaj w grupie zawodnicy
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div/main/div[3]/div[2]/div/div[2]/div/div/div/div[3]/a').click()

#przycisk akceptujacy ciasteczka
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[7]/div[2]/div[2]/div[2]/div[2]/button[1]/p').click()

#przycisk wyszukaj otwierajacy liste wszystkich zawodnikow na sprzedaz
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/main/div/div[2]/div[2]/div[2]/form/div[6]/div[2]/div/div/button[1]').click()


time.sleep(5)