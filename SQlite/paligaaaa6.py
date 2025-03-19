
import requests
for n in range(3):
    laikazinas = requests.get(f"https://api.chucknorris.io/jokes/random?format=j1")
    data = laikazinas.json()
    joks=data['value']
    print(joks)