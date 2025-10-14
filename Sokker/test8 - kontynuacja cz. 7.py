import os
import requests
from xml.etree import ElementTree as etree
import pandas as pd

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

    # Definiowanie wartości y i zakresów z
    y_values = [1, 2, 3, 4, 5, 6]
    z_ranges = {
        1: range(1, 2),
        2: range(1, 4),
        3: range(1, 10),
        4: range(1, 28),
        5: range(1, 82),
        6: range(1, 163)
    }

    # Ścieżka do zapisu plików
    save_path = r'C:\Users\pszczubiala\OneDrive - Fresenius\Desktop\Private\SK\Sokker test'

    # Lista do przechowywania leagueIDs
    league_IDs = []

    # Pobieranie plików XML, zapisywanie na dysku oraz wyciąganie leagueID
    for y in y_values:
        for z in z_ranges[y]:
            x = 1
            xml_url = f'https://sokker.org/xml/league-{x}-{y}-{z}.xml'
            xml_response = session.get(xml_url)

            if xml_response.status_code == 200:
                file_name = f'league-{x}-{y}-{z}.xml'
                file_path = os.path.join(save_path, file_name)
                with open(file_path, 'wb') as file:
                    file.write(xml_response.content)
                print(f'Plik {file_name} został pobrany i zapisany w {file_path}.')

                # Parsowanie XML i wyciąganie leagueID
                tree = etree.fromstring(xml_response.content)
                league_id_element = tree.find('.//leagueID')
                if league_id_element is not None:
                    league_id = league_id_element.text
                    league_IDs.append(league_id)
                    print(f'Pobrano leagueID: {league_id} z pliku {file_name}')
                else:
                    print(f'Brak elementu leagueID w pliku XML: {xml_url}')
            else:
                print(f'Błąd podczas pobierania pliku XML: {xml_url}')

    # Drukowanie listy league_IDs
    print("Lista league_IDs:")
    print(league_IDs)

    # Pobieranie plików XML na podstawie league_IDs i wyciąganie teamID
    team_IDs = []
    for league_id in league_IDs:
        xml_url = f'https://sokker.org/xml/league-{league_id}.xml'
        xml_response = session.get(xml_url)

        if xml_response.status_code == 200:
            file_name = f'league-{league_id}.xml'
            file_path = os.path.join(save_path, file_name)
            with open(file_path, 'wb') as file:
                file.write(xml_response.content)
            print(f'Plik {file_name} został pobrany i zapisany w {file_path}.')

            # Parsowanie XML i wyciąganie teamID
            tree = etree.fromstring(xml_response.content)
            team_id_elements = tree.findall('.//teamID')
            for team_id_element in team_id_elements:
                team_id = team_id_element.text
                team_IDs.append(team_id)
                print(f'Pobrano teamID: {team_id} z pliku {file_name}')
        else:
            print(f'Błąd podczas pobierania pliku XML: {xml_url}')

    # Drukowanie listy team_IDs
    print("Lista team_IDs:")
    print(team_IDs)

    # Zapisywanie listy team_IDs do pliku Excel
    df_team_ids = pd.DataFrame(team_IDs, columns=['teamID'])
    excel_file_path = os.path.join(save_path, 'team_IDs.xlsx')
    df_team_ids.to_excel(excel_file_path, index=False)
    print(f'Lista team_IDs została zapisana w pliku Excel: {excel_file_path}')
else:
    print('Uwierzytelnianie nie powiodło się.')


# Pobieranie danych o zawodnikach dla każdego teamID
all_players_data = []

for team_id in team_IDs:
    # Pobieranie pliku XML dla każdego zespołu
    xml_url = f'https://sokker.org/xml/players-{team_id}.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        # Parsowanie pliku XML
        tree = etree.fromstring(xml_response.content)
        root = tree

        # Wyciąganie danych
        for player in root.findall('player'):
            player_data = {child.tag: child.text for child in player}
            all_players_data.append(player_data)
        print(f'Dane dla zespołu {team_id} zostały pobrane.')
    else:
        print(f'Błąd podczas pobierania pliku XML dla zespołu {team_id}.')

# Tworzenie DataFrame dla zawodników
df_players = pd.DataFrame(all_players_data)

# Konwersja wszystkich kolumn na numeryczne, errors='coerce' zamieni wartości nienumeryczne na NaN
df_players = df_players.apply(pd.to_numeric, errors='coerce')

# Zapisywanie do pliku Excel (nadpisanie, jeśli istnieje)
df_players.to_excel('C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker test\\players_all_teams.xlsx', index=False)

print("Pliki XML zostały pomyślnie przekonwertowane na tabelę Excel i zapisane jako 'players_all_teams.xlsx'.")