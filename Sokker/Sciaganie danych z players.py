#etap sciagania najnowszej wersji pliku players.xml
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
    xml_url = 'https://sokker.org/xml/players-99710.xml'
    xml_response = session.get(xml_url)

    if xml_response.status_code == 200:
        with open('players-99710.xml', 'wb') as file:
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
tree = etree.parse('players-99710.xml')
root = tree.getroot()

# Extract data
data = []
for player in root.findall('player'):
    ID = player.find('ID').text if player.find('ID') is not None else None
    name = player.find('name').text if player.find('name') is not None else None
    surname = player.find('surname').text if player.find('surname') is not None else None
    countryID = player.find('countryID').text if player.find('countryID') is not None else None
    age = player.find('age').text if player.find('age') is not None else None
    height = player.find('height').text if player.find('height') is not None else None
    weight = player.find('weight').text if player.find('weight') is not None else None
    BMI = player.find('BMI').text if player.find('BMI') is not None else None
    teamID = player.find('teamID').text if player.find('teamID') is not None else None
    youthTeamID = player.find('youthTeamID').text if player.find('youthTeamID') is not None else None
    value = player.find('value').text if player.find('value') is not None else None
    wage = player.find('wage').text if player.find('wage') is not None else None
    cards = player.find('cards').text if player.find('cards') is not None else None
    goals = player.find('goals').text if player.find('goals') is not None else None
    assists = player.find('assists').text if player.find('assists') is not None else None
    matches = player.find('matches').text if player.find('matches') is not None else None
    ntCards = player.find('ntCards').text if player.find('ntCards') is not None else None
    ntGoals = player.find('ntGoals').text if player.find('ntGoals') is not None else None
    ntAssists = player.find('ntAssists').text if player.find('ntAssists') is not None else None
    ntMatches = player.find('ntMatches').text if player.find('ntMatches') is not None else None
    injuryDays = player.find('injuryDays').text if player.find('injuryDays') is not None else None
    national = player.find('national').text if player.find('national') is not None else None
    skillForm = player.find('skillForm').text if player.find('skillForm') is not None else None
    skillExperience = player.find('skillExperience').text if player.find('skillExperience') is not None else None
    skillTeamwork = player.find('skillTeamwork').text if player.find('skillTeamwork') is not None else None
    skillDiscipline = player.find('skillDiscipline').text if player.find('skillDiscipline') is not None else None
    transferList = player.find('transferList').text if player.find('transferList') is not None else None
    skillStamina = player.find('skillStamina').text if player.find('skillStamina') is not None else None
    skillPace = player.find('skillPace').text if player.find('skillPace') is not None else None
    skillTechnique = player.find('skillTechnique').text if player.find('skillTechnique') is not None else None
    skillPassing = player.find('skillPassing').text if player.find('skillPassing') is not None else None
    skillKeeper = player.find('skillKeeper').text if player.find('skillKeeper') is not None else None
    skillDefending = player.find('skillDefending').text if player.find('skillDefending') is not None else None
    skillPlaymaking = player.find('skillPlaymaking').text if player.find('skillPlaymaking') is not None else None
    skillScoring = player.find('skillScoring').text if player.find('skillScoring') is not None else None
    trainingPosition = player.find('trainingPosition').text if player.find('trainingPosition') is not None else None
    isInTrainingSlot = player.find('isInTrainingSlot').text if player.find('isInTrainingSlot') is not None else None

    data.append([ID, name, surname, countryID, age, height, weight, BMI, teamID, youthTeamID, value, wage, cards, goals, assists, matches, ntCards, ntGoals, ntAssists, ntMatches, injuryDays, national, skillForm, skillExperience, skillTeamwork, skillDiscipline, transferList, skillStamina, skillPace, skillTechnique, skillPassing, skillKeeper, skillDefending, skillPlaymaking, skillScoring, trainingPosition, isInTrainingSlot])

# Create a DataFrame
df = pd.DataFrame(data, columns=['ID', 'name', 'surname', 'countryID', 'age', 'height', 'weight', 'BMI', 'teamID', 'youthTeamID', 'value', 'wage', 'cards', 'goals', 'assists', 'matches', 'ntCards', 'ntGoals', 'ntAssists', 'ntMatches', 'injuryDays', 'national', 'Form', 'Experience', 'Teamwork', 'Discipline', 'transferList', 'Stamina', 'Pace', 'Technique', 'Passing', 'Keeper', 'Defending', 'Playmaking', 'Scoring', 'trainingPosition', 'isInTrainingSlot'])

# Save to Excel (overwrite if exists)
df.to_excel('C:\\Users\\pszczubiala\\OneDrive - Fresenius\\Desktop\\Private\\SK\\Sokker test\\players-99710.xlsx', index=False)

print("The XML file has been successfully converted to an Excel table and saved as 'players.xlsx'.")

