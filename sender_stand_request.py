import configuration
import requests
import data


def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body,
                         headers=data.headers)


response = post_new_order(data.order_body)
print(response.status_code)
print(response.json())


def get_data_order_by_track():
    post_new_order_response = post_new_order(data.order_body)
    order_track = post_new_order_response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_DATA_ORDER_BY_TRACK,
                        params={"t": order_track})


response = get_data_order_by_track()
print(response.status_code)
print(response.json())
