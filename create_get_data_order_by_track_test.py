import sender_stand_request


def test_data_order_by_track_positive_assert():
    response = sender_stand_request.get_data_order_by_track()
    assert response.status_code == 200