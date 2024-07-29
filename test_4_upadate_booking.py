import pytest
import requests
import allure

import test_1_create_token
import test_2_create_booking


@allure.feature('Booking Feature')
@allure.suite('Booking Update Tests')
@allure.title('Update Booking Details')
@allure.description('This test updates the booking details and verifies the changes.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.regression

def test_put_booking():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Cookie': f'token={test_1_create_token.my_token}'}

    with allure.step('Send PUT request to update booking'):
        response = requests.put(
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

    with allure.step('Verify totalprice is updated correctly'):
        assert body['totalprice'] == response_data['totalprice'], f'Expected totalprice to be {body["totalprice"]}, but got {response_data["totalprice"]}'

    with allure.step('Verify depositpaid is updated correctly'):
        assert body['depositpaid'] == response_data['depositpaid'], f'Expected depositpaid to be {body["depositpaid"]}, but got {response_data["depositpaid"]}'

    with allure.step('Verify checkin date is updated correctly'):
        assert body['bookingdates']['checkin'] == response_data['bookingdates']['checkin'], 'Check-in dates do not match'

    with allure.step('Verify checkout date is updated correctly'):
        assert body['bookingdates']['checkout'] == response_data['bookingdates']['checkout'], 'Checkout dates do not match'

    with allure.step('Verify additionalneeds is updated correctly'):
        assert body['additionalneeds'] == response_data['additionalneeds'], f'Expected additionalneeds to be {body["additionalneeds"]}, but got {response_data["additionalneeds"]}'

    with allure.step('Printing response'):
        allure.attach(response.text, 'Response', allure.attachment_type.JSON)

@allure.feature('Booking Feature')
@allure.suite('Booking Update Tests')
@allure.title('Update Booking with Invalid Token')
@allure.description('This test attempts to update a booking with an invalid token and expects a 403 Forbidden response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_put_booking_with_invalid_token():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Cookie': 'token=123456xdcv'}

    with allure.step('Send PUT request with invalid token'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code is 403, but got {response.status_code}'


@allure.feature('Booking Feature')
@allure.suite('Booking Update Tests')
@allure.title('Update Booking without Token')
@allure.description('This test attempts to update a booking without providing a token and expects a 403 Forbidden response.')
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
def test_negative_put_booking_without_token():
    body = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

    with allure.step('Send PUT request without token'):
        response = requests.put(
            f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}',
            json=body,
            headers=headers
        )

    with allure.step('Verify response status code is 403'):
        assert response.status_code == 403, f'Expected Status Code is 403, but got {response.status_code}'