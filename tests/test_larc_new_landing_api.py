from email.mime import application
from urllib import response
import requests
import json
import pytest
import data.new_landing_data as data



def get_loan_data_payload(person_id):
  loan_data_payload = json.dumps({
    "personId": person_id,
    "loanLimit": 20000,
    "loanTerm": 84,
    "loanRate": 23,
    "loanCost": 20000,
    "monthlyPayment": 483,
    "productCategory": 1,
    "status": 0,
    "step": 1,
    "createdOn": "Wed, 13 Apr 2022 06:10:42 GMT"
  })
  return loan_data_payload

def get_loan_validate_data(application_id):
  validate_data_payload = json.dumps({
    "applicationId": application_id,
    "creditSum": 20000,
    "personCategory": 1,
    "productCategory": 1
  })
  return application_id


def test_get_authorization_id():
  global authorization_id
  global auth_headers

  response = requests.get(f"{data.baseUrl}/Auth/GetAuthorizationIdByToken", params={"token":data.token})
  authorization_id = response.json()['authorizationId']
  auth_headers = {'accept': 'application/json, text/plain, */*',"authorizationId" : authorization_id,'content-type': 'application/json'}

  assert response.status_code == 200, "Cant get Authorization ID"



def test_get_loan_product_api():
  response = requests.get(f"{data.baseUrl}/Loan/GetLoanProducts", params={"Source":"AebOnline"},
  headers=auth_headers)
  print(response.status_code, "Loan Products GOT")
  assert response.status_code == 200, "Cant get loan products"



def test_set_abs_id():
  response = requests.get(f"{data.baseUrl}/Test/SetAbsId", params={"AbsId": data.absId})
  print(response.status_code, "Abs ID set success")
  #authorization_id = set_absId.json()['authorizationId']
  assert response.status_code == 200, "Cant set AbsId"



def test_get_person_id():
  response = requests.get(f"{data.baseUrl}/Person/GetPersonByAuthorizationId/{authorization_id}", headers=auth_headers)

  global person_id
  person_id = response.json()['id']
  print( "Person id is = ", person_id)
  print(response.json()["lastName"])

  assert response.status_code == 200, "cant get person id by authorizationId"



def test_patch_phone():
  response = requests.patch(f"{data.baseUrl}/api/Person/{person_id}",
  headers=auth_headers, data = data.phone_payload)

  print(response.status_code)
  print(response.json()['dboPhoneNumber'])

  parsed_phone = response.json()['dboPhoneNumber']
  assert parsed_phone == data.phone, "phone is not equal"

  

def test_get_active_apllications():
  response = requests.get(f"{data.baseUrl}/Application/GetActiveApplicationsList/{authorization_id}",
  headers=auth_headers)

  assert response.status_code == 200, "cant get list of applications"

def test_check_debt_person():
  response =requests.post(f"{data.baseUrl}/Check/CheckPerson/{person_id}", headers=auth_headers)
  print(response.text, response.status_code)
 
  assert response.status_code == 200, "cant get debt results"

def test_modify_loan_term():
  response = requests.post (f"{data.baseUrl}/Loan/CalculateLoanPayments",
  headers= auth_headers, data=data.loan_payload)
  print(response.status_code)
  
  assert response.status_code == 200, "Cant post loan data"

def test_application_create():
  response = requests.post(f"{data.baseUrl}i/Application",
  headers=auth_headers, data=get_loan_data_payload(person_id))

  print(response.text)
  global application_id
  application_id = response.json()['id']

  assert response.status_code == 200, "Cant post loan data to application"

def test_validate_loan():
  response = requests.post(f"{data.baseUrl}/Loan/ValidateLoanLimit",
  headers=auth_headers, data = get_loan_validate_data(application_id))

  assert response.status_code == 200, "Not validated loan"

def test_send_sms():
  response = requests.get(f"{data.baseUrl}/Sms/SendSms?{application_id}", headers=auth_headers)

  assert response.status_code == 200, "Cant get sms"

def test_change_office():
  payload = json.dumps([
    {
      "value": "db5a7cb6-db06-461c-b78b-bafce951fcef",
      "path": "/officeId",
      "op": "replace"
    }
  ])
  response = requests.patch(f"{data.baseUrl}/Application/{application_id}",
  headers= auth_headers, data = payload)
  if response.status_code == 200:
    print("OfficeID Changed")
  else: print("OfficeID did not changed")

  assert response.status_code == 200, "Cant change OfficeID"

def test_change_address():
  payload = json.dumps([
    {
      "value": "Россия, 677027, Саха /Якутия/ Респ, г. Якутск, ул Каландаришвили, дом 8, кв 36",
      "path": "/addressReg",
      "op": "replace"
    },
    {
      "value": "Россия, 677027, Саха /Якутия/ Респ, г. Якутск, ул Каландаришвили, дом 8, кв 36",
      "path": "/addressAct",
      "op": "replace"
    }
  ])
  response = requests.patch(f"{data.baseUrl}/Person/{person_id}", headers=auth_headers, data=payload)
  if response.status_code == 200:
    print("Address Changed")
  else: print("Address did not changed")

  assert response.status_code == 200, "Cant change address reg"

def test_set_goal():
  payload = json.dumps([
    {
      "value": "фыв",
      "path": "/productGoalByHuman",
      "op": "replace"
    },
    {
      "value": 3,
      "path": "/step",
      "op": "replace"
    }
  ])

  response = requests.patch(f"{data.baseUrl}/Application/{application_id}", headers=auth_headers, data=payload)
  
  assert response.status_code == 200, "Cant set goal to application"


def test_set_second_phone():
  payload = json.dumps([
    {
      "value": 0,
      "path": "/contactType",
      "op": "replace"
    },
    {
      "value": "ывфасвафы",
      "path": "/fio",
      "op": "replace"
    },
    {
      "value": "+7 (111) 111-11-11",
      "path": "/phone",
      "op": "replace"
    }
  ])
  response = requests.patch(f"{data.baseUrl}/ContactPersonSecond/fb9fd066-d7e5-4b39-a1ea-3b6948d77299")
  assert response.status_code == 200, "Cant set second phone"



def test_application_is_ready():
  response = requests.post(f"{data.baseUrl}/Application/ApplicationIsReady/{authorization_id}",
  headers=auth_headers)
  assert response.status_code == 200, "Cant set application ready"

