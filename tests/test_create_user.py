import requests
import pytest
from json import JSONDecodeError
import time


class TestCreateUser:
    def test_create_delete(self):
        data = {
            "username" : "tuskuljerkich",
            "firstName" : "Tuskul",
            "lastName": "Spiridonov",
            "email":"tuskulspiridonov@mail.ru",
            "password":"qweasd123"
        }

        auth_data = {
                "email" : "tuskulspiridonov@mail.ru",
                "password" : "qweasd123"
            }

        create_user_response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        auth_user_response = requests.post("https://playground.learnqa.ru/api/user/login",params=auth_data)

        try:
            parsed_response_text = auth_user_response.json()
            print(parsed_response_text['user_id'])
        except JSONDecodeError:
            print("Response is not JSON")

        token = auth_user_response.headers.get("x-csrf-token")
        auth_sid = auth_user_response.cookies.get("auth_sid")

        userid = requests.get("https://playground.learnqa.ru/api/user/auth", 
        headers={"x-csrf-token": token}, cookies={"auth_sid" : auth_sid})
        print(userid.text)

        useridnum = userid.json()["user_id"]
        print(useridnum)
        delete_user = requests.delete(f"https://playground.learnqa.ru/api/user/{useridnum}", headers={"x-csrf-token": token}, cookies={"auth_sid" : auth_sid})

        assert create_user_response.status_code == 200, f"user is not created"
        assert userid.status_code == 200, "no authorization"
        assert delete_user.status_code == 200, f"user {userid} is not deleted"


