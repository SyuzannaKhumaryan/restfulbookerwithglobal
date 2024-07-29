import pytest
import requests
import allure

import test_1_create_token
import test_2_create_booking


@allure.feature('Booking Feature')
@allure.suite('Booking Deletion Tests')
@allure.title('Delete Booking by ID')
@allure.description('This test deletes a booking by ID and verifies the deletion.')
@allure.severity(allure.severity_level.BLOCKER)
@pytest.mark.smoke
@pytest.mark.regression
def test_delete_booking_by_id():
    headers = {'Content-Type': 'application/json', 'Accept': 'application/json',
               'Cookie': f'token={test_1_create_token.my_token}'}

    with allure.step('Send DELETE request to remove booking'):
        response = requests.delete(
            f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}',
            headers=headers
        )

    with allure.step('Verify response status code is 201'):
        assert response.status_code == 201, f'Expected Status Code is 201, but got {response.status_code}'

    # Optionally, verify the booking has been deleted
    with allure.step('Verify booking has been deleted'):
        response = requests.get(f'https://restful-booker.herokuapp.com/booking/{test_2_create_booking.my_bookingid}')
    assert response.status_code == 404, f'Expected Status Code is 404 for non-existing booking, but got {response.status_code}'