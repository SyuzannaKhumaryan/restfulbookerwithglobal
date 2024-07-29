import requests
import pytest
import allure

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature('Booking Feature')
@allure.suite('Ping Tests')
@allure.title('Health Check of Booking Service')
@allure.description('This test checks the health status of the Booking Service by hitting the /ping endpoint.')
@allure.severity('BLOCKER')
def test_health_check():
    with allure.step('Sending GET request to /ping endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/ping')

    with allure.step('Verifying the response status code'):
        assert response.status_code == 201, f'Expected Status Code is 201, but got {response.status_code}'
