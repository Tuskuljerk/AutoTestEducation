import requests
from json.decoder import JSONDecodeError

response = requests.get("https://playground.learnqa.ru/api/get_json")

try:
    parsed_response = response.json()
    print(parsed_response)
except:
    print("Response is not JSON")