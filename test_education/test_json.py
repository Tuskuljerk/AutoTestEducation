import requests
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/api/get_json")

try:
    pardes_response = response.json()
    print(pardes_response)
except:
    print("Response is not JSON")