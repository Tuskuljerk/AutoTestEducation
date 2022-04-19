import pytest
import requests

class TestAuth:
    def test_auth_user(self):
        auth_data = {
            "email" : "tuskulspiridonov@mail.ru",
            "password" : "qweasd123"
        }

        assert "auth_sid" in login_response.cookies, "There is no auth cookie in the response"
        assert "x-csrf-token" in login_response.headers, "There is no auth header in the response"
        assert "user_id" in login_response.json(), "There is no userId in the response"

        login_response = requests.post("https://playground.learnqa.ru/api/user/login", data=auth_data)
        print(login_response.headers)

        auth_sid = login_response.cookies.get("auth_sid")
        token = login_response.headers.get("x-csrf-token")
        user_id_from_auth_method = login_response.json()["user_id"]


        get_userid_response = requests.get("https://playground.learnqa.ru/api/user/auth",
            headers={"x-csrf-token" : token},
            cookies={"auth_sid" : auth_sid},
        )

        assert "user_id" in get_userid_response.json(), "There is no userid in second response"
        userId_from_check_method = get_userid_response.json()["user_id"]

        assert user_id_from_auth_method == userId_from_check_method, "User Id from auth method is not equal userId from check method"
        