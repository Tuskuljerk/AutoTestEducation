from urllib import response
#import pytest
import requests
from json.decoder import JSONDecodeError

payload = {"name" : "Tuskul"}
response = requests.get("https://playground.learnqa.ru/api/hello/", params=payload)
responseToGetRedirect = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True) 

try:
    parsed_response_text = response.json()
    print(parsed_response_text['answer'])
except JSONDecodeError:
    print("Response is not JSON")


auth_data = {
            "email" : "tuskulspiridonov@mail.ru",
            "password" : "qweasd123"
        }

login_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
print(login_response.headers)
