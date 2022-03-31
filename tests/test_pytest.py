import pytest
import requests

class TestFirstApi:

    names = [
        ('Tuskul'),
        ('Vitaliy'),
        ("")
    ]

    @pytest.mark.parametrize('name', names)
    
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data )
        assert response.status_code == 200, 'Wrong response code'

        response.__dict__ = response.json()
        assert 'answer' in response.__dict__, "There is no field"

        if len(name) == 0:
            expected_response_text = "Hello, someone"
        else:
            expected_response_text = f"Hello, {name}"

        actual_response_text = response.__dict__['answer']
        assert actual_response_text == expected_response_text, "Actual text in the response is not correct"


