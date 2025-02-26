import requests
response=requests.get("https://www.lu.lv/abc")
print(f"Latvijas Universitātes vietnes statusa kods: {response.status_code}")
print("\nGalvenes:")
for header, value in response.headers.items():
    print(f"{header}:{value}")