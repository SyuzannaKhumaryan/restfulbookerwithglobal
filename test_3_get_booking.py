import pytest
import requests
import allure
import test_2_create_booking

@allure.feature('Booking Feature')
@allure.suite('Booking Retrieval Tests')
@allure.title('Retrieve All Bookings')
@allure.description('This test retrieves all bookings and verifies the response.')
@allure.severity('NORMAL')
@pytest.mark.regression
def test_get_all_booking():
    with allure.step('Send GET request to get all booking endpoint'):
        response = requests.get('https://restful-booker.herokuapp.com/booking')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    with allure.step('Verify the booking list is not empty'):
        assert len(response.json()) > 0, "The list shouldn't be empty"

@allure.feature('Booking Feature')
@allure.suite('Booking Retrieval Tests')
@allure.title('Retrieve Booking by ID')
@allure.description('This test retrieves a booking by ID and verifies the response.')
@allure.severity('NORMAL')
@pytest.mark.regression
def test_get_booking_by_id():
    booking_id = test_2_create_booking.my_bookingid

    with allure.step('Send request to get booking by ID'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{booking_id}')

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains firstname'):
        assert 'firstname' in response_data, "The response doesn't contain 'firstname'"

    with allure.step('Verify response contains lastname'):
        assert 'lastname' in response_data, "The response doesn't contain 'lastname'"

    with allure.step('Verify response contains totalprice'):
        assert 'totalprice' in response_data, "The response doesn't contain 'totalprice'"

    with allure.step('Verify response contains depositpaid'):
        assert 'depositpaid' in response_data, "The response doesn't contain 'depositpaid'"

    with allure.step('Verify response contains bookingdates'):
        assert 'bookingdates' in response_data, "The response doesn't contain 'bookingdates'"

    with allure.step('Verify bookingdates contains checkin'):
        assert 'checkin' in response_data['bookingdates'], "The response doesn't contain 'checkin'"

    with allure.step('Verify bookingdates contains checkout'):
        assert 'checkout' in response_data['bookingdates'], "The response doesn't contain 'checkout'"

    with allure.step('Verify response contains additionalneeds'):
        assert 'additionalneeds' in response_data, "The response doesn't contain 'additionalneeds'"

    with allure.step('Verify depositpaid is a boolean'):
        assert response_data['depositpaid'] in [True, False], 'Error: depositpaid is not a boolean'

    with allure.step('Verify totalprice is an int or float'):
        assert isinstance(response_data['totalprice'], (int, float)), 'Error: totalprice is not an int or float'

