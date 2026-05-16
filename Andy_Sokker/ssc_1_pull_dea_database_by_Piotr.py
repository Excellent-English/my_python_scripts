from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# open Chrome instance and go to the website
service = Service(ChromeDriverManager().install())
wd = webdriver.Chrome(service=service)

#wd = webdriver.Chrome()

wd.get('https://apps.deadiversion.usdoj.gov/RDA/login.xhtml?jfwid=cvV6CkBE8inccxhHDrJsJtXWWlOFNjTr9NxFbIbd:0#no-back-button')
sleep(1)
wd.maximize_window()

# type email address and password
WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form/fieldset/div/table[2]/tbody/tr[1]/td[2]/input'))).send_keys("USCUSTOMERMASTERSSC@FRESENIUS-KABI.COM")
sleep(1)

WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form/fieldset/div/table[2]/tbody/tr[2]/td[2]/input'))).send_keys("FreSenius010101.")
sleep(1)

# click on Login button
WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form/fieldset/div/div[2]/button[1]/span'))).click()
sleep(2)

# agree to the terms
WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form[1]/fieldset/div/table/tbody/tr[2]/td/div/div[2]/span'))).click()
sleep(2)

# click on Download Registrant Datasets
WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form[1]/fieldset/div/table[2]/tbody/tr[2]/td/button[1]/span'))).click()
sleep(2)

# click on Download Active Controlled Substance Registrant File
WebDriverWait(wd, 30).until(EC.presence_of_element_located(
    (By.XPATH, '/html/body/div[1]/div[2]/form[1]/fieldset/div/table/tbody/tr[2]/td/button/span[2]'))).click()

input("Press 'Enter' to confirm download is complete.")