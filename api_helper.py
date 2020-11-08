import requests


def post_booking_request(test_data):
    url = "https://restful-booker.herokuapp.com/booking"
    headers = {
        "Content-Type": "application/json",
    }
    data = test_data
    return requests.post(url, headers=headers, json=data)
