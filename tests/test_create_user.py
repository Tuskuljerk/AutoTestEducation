import requests

data = {
    "username" : "tuskuljerk",
    "firstName" : "Tuskul",
    "lastName": "Spiridonov",
    "email":"tuskulspiridonov@mail.ru",
    "password":"qweasd123"
}

create_user_response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
print(create_user_response.status_code, create_user_response.text)

print(create_user_response.headers)


