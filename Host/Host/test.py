import requests
import json

URL = ('http://127.0.0.1:5000//add_chesse_product')
HEADERS = {'Content-Type': 'application/json',}
data = {
    'name': 'rokfor2223',
    'year': 0.15,
    'quantity': 2
}

#response = requests.get(url=URL)
data_json = json.dumps(data)

response = requests.post(url=URL, data=data_json, headers=HEADERS)


print(response.status_code)
print(response.text)