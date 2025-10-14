import requests
import json

url = 'https://sokker.org/start.php?session=xml'
data = {
    'ilogin': 'asciutto',
    'ipassword': 'harrypotter'
}
headers = {'Content-Type': 'application/json'}


response = requests.post('https://sokker.org/xml/', data=json.dumps(data), headers=headers)
print(response.text)