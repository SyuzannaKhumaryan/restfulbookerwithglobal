import pytest
import requests
import allure

my_bookingid = 0


@allure.feature('Booking Feature')
@allure.suite('Creation Booking Suites')
@allure.title('Create a new booking')
@allure.description('This test creates a new booking and verifies all the fields in the response.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_create_booking():
    data = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    headers = {'Content-Type': 'application/json'}

    with allure.step('Send POST request to create a booking'):
        response = requests.post('https://restful-booker.herokuapp.com/booking', json=data, headers=headers)

    with allure.step('Verify response status code is 200'):
        assert response.status_code == 200, f'Expected Status Code is 200, but got {response.status_code}'

    response_data = response.json()

    with allure.step('Verify response contains bookingid'):
        assert 'bookingid' in response_data, "The response doesn't contain 'bookingid'"

    with allure.step('Verify response contains booking data'):
        assert 'booking' in response_data, "The response doesn't contain 'booking'"

    response_booking = response_data['booking']

    with allure.step('Verify booking contains firstname'):
        assert 'firstname' in response_booking, "The response doesn't contain 'firstname'"

    with allure.step('Verify booking contains lastname'):
        assert 'lastname' in response_booking, "The response doesn't contain 'lastname'"

    with allure.step('Verify booking contains totalprice'):
        assert 'totalprice' in response_booking, "The response doesn't contain 'totalprice'"

    with allure.step('Verify booking contains depositpaid'):
        assert 'depositpaid' in response_booking, "The response doesn't contain 'depositpaid'"

    with allure.step('Verify firstname is correct'):
        assert response_booking['firstname'] == data['firstname'], f'Expected firstname to be {data["firstname"]} but got {response_booking["firstname"]}'

    with allure.step('Verify lastname is correct'):
        assert response_booking['lastname'] == data['lastname'], f'Expected lastname to be {data["lastname"]} but got {response_booking["lastname"]}'

    with allure.step('Verify totalprice is correct'):
        assert response_booking['totalprice'] == data['totalprice'], f'Expected totalprice to be {data["totalprice"]} but got {response_booking["totalprice"]}'

    with allure.step('Verify depositpaid is correct'):
        assert response_booking['depositpaid'] == data['depositpaid'], f'Expected depositpaid to be {data["depositpaid"]} but got {response_booking["depositpaid"]}'

    with allure.step('Verify booking contains bookingdates'):
        assert 'bookingdates' in response_booking, "The response doesn't contain 'bookingdates'"

    with allure.step('Verify bookingdates contains checkin'):
        assert 'checkin' in response_booking['bookingdates'], "The 'bookingdates' doesn't contain 'checkin'"

    with allure.step('Verify bookingdates contains checkout'):
        assert 'checkout' in response_booking['bookingdates'], "The 'bookingdates' doesn't contain 'checkout'"

    with allure.step('Verify booking contains additionalneeds'):
        assert 'additionalneeds' in response_booking, "The response doesn't contain 'additionalneeds'"

    with allure.step('Verify checkin date is correct'):
        assert response_booking['bookingdates']['checkin'] == data['bookingdates']['checkin'], f'Expected checkin to be {data["bookingdates"]["checkin"]} but got {response_booking["bookingdates"]["checkin"]}'

    with allure.step('Verify checkout date is correct'):
        assert response_booking['bookingdates']['checkout'] == data['bookingdates']['checkout'], f'Expected checkout to be {data["bookingdates"]["checkout"]} but got {response_booking["bookingdates"]["checkout"]}'

    with allure.step('Verify additionalneeds is correct'):
        assert response_booking["additionalneeds"] == data['additionalneeds'], f'Expected additionalneeds to be {data["additionalneeds"]} but got {response_booking["additionalneeds"]}'

    global my_bookingid
    my_bookingid = response_data['bookingid']