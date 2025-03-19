import requests
pilseta = input("Ievadi pilsētu:")

laikazinas = requests.get(f"https://wttr.in/{pilseta}?format=j1")
data = laikazinas.json()
print(data)