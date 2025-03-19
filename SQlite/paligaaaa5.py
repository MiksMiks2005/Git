import requests
pilseta = input("Ievadi pilsētu:")

laikazinas = requests.get(f"https://api.chucknorris.io/jokes/random{pilseta}?format=j1")
data = laikazinas.json()
temperatura= data['current_condition'][0]['temp_C']
spiediens = data['current_condition'][0]['pressure']
print(f"pilsēta:{pilseta},Temperatūra: {temperatura}, Spiediens: {spiediens}")