# hello world

import requests
import json

url = 'https://webhook.site/fd82f8b9-b338-411a-9d2e-75b25d8a2899'

g = requests.get(url)

data = g.json()

money = 0

for i in data:
	if i["eyeColor"] == "green":
		money += float(i["balance"][1:2] + i["balance"][3:])

print(round(money, 2))




# translater API

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

text = input("Введите текст для перевода: ")
payload = "source=ru&target=en&q=" + text

headers = {
    'content-type': "application/x-www-form-urlencoded",
    'accept-encoding': "application/gzip",
    'x-rapidapi-host': "google-translate1.p.rapidapi.com",
    'x-rapidapi-key': "a83fd36110msha150147f0ddc1e1p1b4965jsncd29ef4112cb"
    }

response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
text = response.json()

print(text["data"]["translations"][0]["translatedText"])
