from api_helper import post_booking_request


def test_booking_successful():
    test_data = {
                'firstname': 'John',
                'lastname': 'Doe',
                'totalprice': 100,
                'depositpaid': True,
                'bookingdates': {
                                'checkin': '2021-01-01',
                                'checkout': '2021-01-02'
                },
                'additionalneeds': 'Breakfast'
                }
    response = post_booking_request(test_data)
    assert response.status_code == 200
    assert response.json()['bookingid']
    assert response.json()['booking'] == test_data


def test_booking_fails_because_missing_firstname():
    test_data = {'lastname': 'Doe',
                 'totalprice': 100,
                 'depositpaid': True,
                 'bookingdates': {
                     'checkin': '2021-01-01',
                     'checkout': '2021-01-02'},
                 'additionalneeds': 'Breakfast'}
    response = post_booking_request(test_data)
    assert response.status_code == 500
