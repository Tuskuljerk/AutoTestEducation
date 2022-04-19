import json

baseUrl = "https://loan-landing-api-test.albank.ru/draft-data/api"
token = "87c33a70cf473d772fa9a7164c104a75da2829ce4dbb4d670b8cc5ce50b4ce24d26fa740f41544153bbbfa4c54bf2c4fbfc8efc296d4686476361d9bea6237d3"
absId = "41876"
phone = "+79963176826"
phone_payload = json.dumps([
  {
      "value": "+79963176826",
      "path": "/dboPhoneNumber",
      "op": "replace"
  }
])

loan_payload = json.dumps({
  "loanAmount": 20000,
  "loanTerm": 84,
  "hasInsurance": True,
  "personCategory": 1,
  "productCategory": 1,
  "loanPurposeType": "None"
})

