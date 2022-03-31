import requests
import pytest
from json.decoder import JSONDecodeError


auth_data = {
    "email" : "tuskulspiridonov@mail.ru",
    "password" : "qweasd123"
    }

login_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)

#print(login_response.status_code, login_response.text)


try:
    parsed_response_text = login_response.json()
    #print(parsed_response_text['user_id'])
except JSONDecodeError:
    print("Response is not JSON")

token = login_response.headers.get("x-csrf-token")
auth_sid = login_response.cookies.get("auth_sid")

userid = requests.get("https://playground.learnqa.ru/api/user/auth", 
headers={"x-csrf-token": token}, cookies={"auth_sid" : auth_sid})

useridnum = userid.json()['user_id']
#print(userid.status_code, useridnum)


delete_user = requests.delete(f"https://playground.learnqa.ru/api/user/{useridnum}", headers={"x-csrf-token": token}, cookies={"auth_sid" : auth_sid})
print(delete_user.status_code)
