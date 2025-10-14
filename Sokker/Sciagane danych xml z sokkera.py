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
    xml_url = 'https://sokker.org/xml/player-39685475.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        with open('player-39685475.xml', 'wb') as file:
            file.write(xml_response.content)
        print('Plik transfers.xml został pobrany.')
    else:
        print('Błąd podczas pobierania pliku XML.')
else:
    print('Uwierzytelnianie nie powiodło się.')