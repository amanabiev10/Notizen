import requests

url = 'http://127.0.0.1:8000/api/notes/'

# GET-Anfrage
response = requests.get(url)

# Überprüfen, ob die Anfrage erfolgreich war
if response.status_code == 200:
    # JSON-Antwort anzeigen
    print("Erfolgreiche Antwort:")
    print(response.json())
else:
    print(f"Fehler: {response.status_code}")
