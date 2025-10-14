import os
import requests
from xml.etree import ElementTree

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
                tree = ElementTree.fromstring(xml_response.content)
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
else:
    print('Uwierzytelnianie nie powiodło się.')