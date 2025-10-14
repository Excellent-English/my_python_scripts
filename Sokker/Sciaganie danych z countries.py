#etap sciagania najnowszej wersji pliku countries.xml
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
    xml_url = 'https://sokker.org/xml/countries.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        with open('countries.xml', 'wb') as file:
            file.write(xml_response.content)
        print('Plik transfers.xml został pobrany.')
    else:
        print('Błąd podczas pobierania pliku XML.')
else:
    print('Uwierzytelnianie nie powiodło się.')




# od teraz kod zaczyna przerabiac plik countries.xml na Excela

import pandas as pd
from lxml import etree

# Parse the XML file
tree = etree.parse('countries.xml')
root = tree.getroot()

# Extract data
data = []
for country in root.findall('country'):
    country_id = country.find('countryID').text if country.find('countryID') is not None else None
    name = country.find('name').text if country.find('name') is not None else None
    currency = country.find('currencyName').text if country.find('currencyName') is not None else None
    data.append([country_id, name, currency])

# Create a DataFrame
df = pd.DataFrame(data, columns=['Country ID', 'Name', 'Currency name'])

# Save to Excel
df.to_excel('countries.xlsx', index=False)

print("The XML file has been successfully converted to an Excel table and saved as 'countries.xlsx'.")
