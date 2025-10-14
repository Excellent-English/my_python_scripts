import time

import requests
import pandas as pd
from bs4 import BeautifulSoup

# URL strony z danymi
url = 'https://www.basketball-reference.com/players/c/curryst01/gamelog/2025/'

# Pobierz zawartość strony
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Znajdź tabelę z danymi
table = soup.find('table', {'id': 'pgl_basic'})

# Konwertuj tabelę HTML na DataFrame
df = pd.read_html(str(table))[0]

# Usuń pierwszy wiersz, który jest nagłówkiem
# df.columns = df.columns.droplevel(0)

# Wyświetl DataFrame
print(df)

input("Naciśnij dowolny klawisz, aby kontynuować...")
