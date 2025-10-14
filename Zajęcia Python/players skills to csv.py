import os

import requests

# tworzymy "sesję" przeglądarki
session = requests.Session()

# słownik z danymi do logowania
auth_data = {'ilogin': 'asciutto', 'ipassword': 'harrypotter', }

# logujemy się, otrzymując "token"
auth_url = 'https://sokker.org/start.php?session=xml'
auth_response = session.post(auth_url, data=auth_data)

# otwieramy konkretną stronę
my_players_url = 'https://sokker.org/xml/players-99710.xml'
# trainers_response = requests.get(trainers_url)             # bez sesji otrzymamy stronę informacyjną, a nie dane
players_response = session.get(my_players_url)

# print(trainers_response.status_code)
# print(players_response.text)

season = input("Podaj numer sezonu: ")
round = input("Podaj numer kolejki: ")

import xml.etree.ElementTree as ET
root = ET.fromstring(players_response.text)

if not os.path.exists('C:\\Users\\PSzczubiala\\Downloads\\player.csv'):
    with open('C:\\Users\\PSzczubiala\\Downloads\\player.csv', 'a', encoding='utf-8-sig') as f:
        f.write("Sezon,Kolejka,ID,Name,Surname,skillStamina,skillPace,skillTechnique,skillPassing,skillKeeper,skill Defending,skillPlaymaking,skillScoring\n")

with open('C:\\Users\\PSzczubiala\\Downloads\\player.csv','a', encoding='utf-8-sig') as f:
    # f.write("Sezon,Kolejka,ID,Name,Surname,skillStamina,skillPace,skillTechnique,skillPassing,skillKeeper,skill Defending,skillPlaymaking,skillScoring\n")

    for player in root.findall('player'):
        report = f"{season},{round},{player.find('ID').text},{player.find('name').text},{player.find('surname').text},{player.find('skillStamina').text},{player.find('skillPace').text},{player.find('skillTechnique').text},{player.find('skillPassing').text},{player.find('skillKeeper').text},{player.find('skillDefending').text},{player.find('skillPlaymaking').text},{player.find('skillScoring').text}\n"
        f.write(report)

print("Jest ok, zrobione")