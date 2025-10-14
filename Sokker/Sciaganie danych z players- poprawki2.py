import requests
import pandas as pd
from lxml import etree

# Dane logowania (lepiej użyć zmiennych środowiskowych)
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
        print('Plik league-685.xml został pobrany.')
    else:
        print('Błąd podczas pobierania pliku XML.')
else:
    print('Uwierzytelnianie nie powiodło się.')

# Przerabianie pliku league-685.xml na Excela i tworzenie listy teamID
try:
    # Parse the XML file
    tree = etree.parse('league-685.xml')
    root = tree.getroot()

    # Extract data
    data = []
    team_ids = []
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
        team_ids.append(teamID)

    # Create a DataFrame
    df = pd.DataFrame(data, columns=['teamID', 'round', 'points', 'wins', 'draws', 'losses', 'goalsScored', 'goalsLost'])

    # Save to Excel (overwrite if exists)
    df.to_excel('C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker test\\league-685.xlsx', index=False)

    print("The XML file has been successfully converted to an Excel table and saved as 'league-685.xlsx'.")
    print("Lista teamID:", team_ids)
except Exception as e:
    print(f'Wystąpił błąd: {e}')

# Pobieranie danych o zawodnikach dla każdego teamID
all_players_data = []

for team_id in team_ids:
    # Pobieranie pliku XML dla każdego zespołu
    xml_url = f'https://sokker.org/xml/players-{team_id}.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        # Parse the XML file
        tree = etree.fromstring(xml_response.content)
        root = tree

        # Extract data
        for player in root.findall('player'):
            player_data = {child.tag: child.text for child in player}
            all_players_data.append(player_data)
        print(f'Dane dla zespołu {team_id} zostały pobrane.')
    else:
        print(f'Błąd podczas pobierania pliku XML dla zespołu {team_id}.')

# Create a DataFrame for players
df_players = pd.DataFrame(all_players_data)

# Convert all columns to numeric, errors='coerce' will convert non-numeric values to NaN
df_players = df_players.apply(pd.to_numeric, errors='coerce')

# Save to Excel (overwrite if exists)
df_players.to_excel('C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker test\\players_all_teams.xlsx', index=False)

print("The XML files have been successfully converted to an Excel table and saved as 'players_all_teams.xlsx'.")
