import requests
response= requests.get('https://catfact.ninja/fact')
data = response.json()
print(f'nejaušs fakts par kaķiem: {data['fact']}')