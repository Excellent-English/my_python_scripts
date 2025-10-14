import pandas as pd

# Lista URL dla każdego miesiąca
urls = [
    'https://www.basketball-reference.com/leagues/NBA_2025_games-october.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-november.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-december.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-january.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-february.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-march.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-april.html',
    'https://www.basketball-reference.com/leagues/NBA_2025_games-may.html'
]

# Lista do przechowywania wszystkich DataFrame
all_data = []

# Iteracja przez każdy URL i dodanie tabeli do listy
for url in urls:
    try:
        # Pobranie tabeli z URL
        tables = pd.read_html(url)

        # Wybranie pierwszej tabeli
        df = tables[0]

        # Konwersja kolumny z datami na format daty
        df['Date'] = pd.to_datetime(df['Date'], format='%a, %b %d, %Y').dt.date

        # Dodanie DataFrame do listy
        all_data.append(df)

    except Exception as e:
        # Wyświetlenie komunikatu o błędzie
        print(f"Nie udało się pobrać danych dla URL {url}: {e}")

# Połączenie wszystkich DataFrame w jeden
combined_df = pd.concat(all_data, ignore_index=True)

# Zapisanie połączonych danych do pliku Excel z automatycznym dopasowaniem szerokości kolumn
with pd.ExcelWriter('nba_games_2025_combined.xlsx', engine='xlsxwriter') as writer:
    combined_df.to_excel(writer, index=False, sheet_name='NBA Games 2025')

    # Pobranie workbook i worksheet
    workbook = writer.book
    worksheet = writer.sheets['NBA Games 2025']

    # Automatyczne dopasowanie szerokości kolumn
    for idx, col in enumerate(combined_df.columns):
        max_len = max(combined_df[col].astype(str).map(len).max(), len(col))
        worksheet.set_column(idx, idx, max_len)

# Wyświetlenie komunikatu o sukcesie
print(
    "Wszystkie dostępne tabele zostały zapisane do wspólnego raportu w pliku 'nba_games_2025_combined.xlsx'.")
