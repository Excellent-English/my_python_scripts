#etap sciagania najnowszej wersji pliku league.xml
import requests

# Dane logowania
login_data = {
    'ilogin': 'asciutto',
    'ipassword': 'harrypotter'
}

# URL do uwierzytelniania
auth_url = 'https://sokker.org/start.php?session=xml'

# Wysyłanie danych logowania metodą POST
session = requests.Session()
response = session.post(auth_url, data=login_data)

# Sprawdzanie odpowiedzi
if 'OK' in response.text:
    print("Uwierzytelnianie zakończone sukcesem.")

    # Pobieranie pliku XML
    xml_url = 'https://sokker.org/xml/league-685.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        with open('league-685.xml', 'wb') as file:
            file.write(xml_response.content)
        print('Plik transfers.xml został pobrany.')
    else:
        print('Błąd podczas pobierania pliku XML.')
else:
    print('Uwierzytelnianie nie powiodło się.')



# od teraz kod zaczyna przerabiac plik players.xml na Excela

import pandas as pd
from lxml import etree

# Parse the XML file
tree = etree.parse('league-685.xml')
root = tree.getroot()

# Extract data
data = []
for team in root.find('teams').findall('team'):
    teamID = team.find('teamID').text if team.find('teamID') is not None else None
    round = team.find('round').text if team.find('round') is not None else None
    points = team.find('points').text if team.find('points') is not None else None
    wins = team.find('wins').text if team.find('wins') is not None else None
    draws = team.find('draws').text if team.find('draws') is not None else None
    losses = team.find('losses').text if team.find('losses') is not None else None
    goalsScored = team.find('goalsScored').text if team.find('goalsScored') is not None else None
    goalsLost = team.find('goalsLost').text if team.find('goalsLost') is not None else None


    data.append([teamID, round, points, wins, draws, losses, goalsScored, goalsLost])

# Create a DataFrame
df = pd.DataFrame(data, columns=['teamID', 'round', 'points' , 'wins', 'draws', 'losses', 'goalsScored' , 'goalsLost'])

# Save to Excel (overwrite if exists)
df.to_excel('C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker test\\league-685.xlsx', index=False)

print("The XML file has been successfully converted to an Excel table and saved as 'league-685.xlsx'.")

