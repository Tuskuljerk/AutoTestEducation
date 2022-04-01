import requests
import pytest
import json


token = "87c33a70cf473d772fa9a7164c104a75da2829ce4dbb4d670b8cc5ce50b4ce24d26fa740f41544153bbbfa4c54bf2c4fbfc8efc296d4686476361d9bea6237d3"
absId = "41876"

phone = "+79963176826s"

phone_payload = json.dumps([
  {
    "value": "+79963176826",
    "path": "/dboPhoneNumber",
    "op": "replace"
  }
])

get_authorization_id = requests.get("https://loan-landing-api-test.albank.ru/draft-data/api/Auth/GetAuthorizationIdByToken", params={"token":token})


authorization_id = get_authorization_id.json()['authorizationId']
auth_headers = {'accept': 'application/json, text/plain, */*',"authorizationId" : authorization_id,'content-type': 'application/json'}


get_loan_products = requests.get("https://loan-landing-api-test.albank.ru/draft-data/api/Loan/GetLoanProducts", params={"Source":"AebOnline"},
headers=auth_headers)
print(get_loan_products.status_code, "Loan Products GOT")


set_absId = requests.get("https://loan-landing-api-test.albank.ru/draft-data/api/Test/SetAbsId", params={"AbsId": absId})
print(set_absId.status_code, "Abs ID set success")

authorization_id = set_absId.json()['authorizationId']

get_person_by_auth_id = requests.get(f"https://loan-landing-api-test.albank.ru/draft-data/api/Person/GetPersonByAuthorizationId/{authorization_id}", headers=auth_headers)

person_id = get_person_by_auth_id.json()['id']
print( "Person id is = ", person_id)
print(get_person_by_auth_id.status_code, f"Person was got by {authorization_id}")
print(get_person_by_auth_id.json()["lastName"])


patch_phone_request = requests.patch(f"https://loan-landing-api-test.albank.ru/draft-data/api/Person/{person_id}",
headers=auth_headers, data = phone_payload)

print(patch_phone_request.status_code)
print(patch_phone_request.json()['dboPhoneNumber'])