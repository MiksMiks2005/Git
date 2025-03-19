import requests
city = input("Ievadi pilsētu:")
laikazinas = requests.get(f"https://wttr.in/{city}?m")
print(laikazinas.text)