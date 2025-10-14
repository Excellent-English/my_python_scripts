import requests
import xml.etree.ElementTree as ET

# URL XML z danymi
url = 'http://online.sokker.org/xmlinfo.php'

# Pobierz zawartość strony
response = requests.get(url)
xml_data = response.content

# Przetwórz dane XML
root = ET.fromstring(xml_data)

# Przykład: Wyciągnij i wydrukuj informacje o zawodnikach
for player in root.findall('.//player'):
    name = player.find('name').text
    age = player.find('age').text
    position = player.find('position').text
    print(f'Name: {name}, Age: {age}, Position: {position}')
