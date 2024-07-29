import pytest
import requests
import allure

import test_1_create_token
import test_2_create_booking


@allure.feature('Booking Feature')
@allure.suite('Booking Update Tests')
@allure.title('Patch Booking Details')
@allure.description('This test partially updates the booking details and verifies the changes.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression
def test_patch_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Cookie': f'token={test_1_create_token.my_token}'}

    with allure.step('Send PATCH request to update booking'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify firstname is updated correctly'):
        assert body['firstname'] == response_data['firstname'], f'Expected firstname to be {body["firstname"]}, but got {response_data["firstname"]}'

    with allure.step('Verify lastname is updated correctly'):
        assert body['lastname'] == response_data['lastname'], f'Expected lastname to be {body["lastname"]}, but got {response_data["lastname"]}'

    with allure.step('Verify totalprice is present in the response'):
        assert 'totalprice' in response_data, 'Totalprice key is missing in the response_data'

    with allure.step('Verify depositpaid is present in the response'):
        assert 'depositpaid' in response_data, 'Depositpaid key is missing in the response_data'

    with allure.step('Verify bookingdates checkin is present in the response'):
        assert 'checkin' in response_data['bookingdates'], 'Checkin key is missing in the response_data'

    with allure.step('Verify bookingdates checkout is present in the response'):
        assert 'checkout' in response_data['bookingdates'], 'Checkout key is missing in the response_data'

    with allure.step('Verify additionalneeds is present in the response'):
        assert 'additionalneeds' in response_data, 'Additionalneeds key is missing in the response_data'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)


@allure.feature('Booking Feature')
@allure.suite('Booking Update Tests')
@allure.title('Patch Booking with Invalid Token')
@allure.description('This test attempts to partially update the booking with an invalid token and expects a 403 Forbidden response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_patch_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown"
    }
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=123835dfvg'}

    with allure.step('Send PATCH request with invalid token'):
        response = requests.patch(
            f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code is 403, but got {response.status_code}'