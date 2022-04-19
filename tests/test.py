import requests

person_id = "007d-4bae-bbf9-fb7720e15e59"
check_person = requests.post (f"https://loan-landing-api-test.albank.ru/draft-data/api/Check/CheckPerson/{person_id}", )
print(check_person.text)
print(check_person.status_code)