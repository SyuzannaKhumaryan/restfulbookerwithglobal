import pytest
import requests
import allure

my_token = 0


@allure.feature('Booking Feature')
@allure.suite('Token Creation Tests')
@allure.title('Create Booking Token')
@allure.description('This test creates an authentication token by providing valid credentials.')
@allure.severity('BLOCKER')
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking_token():
    body = {
        "username": "admin",
        "password": "password123"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send POST request to /auth endpoint to create token'):
        response = requests.post(
            'https://restful-booker.herokuapp.com/auth',
            headers=headers,
            json=body
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    with allure.step('Check if the response contains a token'):
        assert 'token' in response.json(), 'Token not found in response'

    with allure.step('Verify the token is not empty'):
        assert len(response.json().get('token')) > 0, 'Token length is 0'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)



    global my_token
    my_token = response.json().get('token')