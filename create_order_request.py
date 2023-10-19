# Георгий Бакаев, 9-я когорта — Финальный проект. Инженер по тестированию плюс
import configuration
import requests

import data


def create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body, headers=data.headers)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t=" + str(track),
                        json=data.order_body, headers=data.headers)


def positive_assert():
    order_response = create_new_order()
    response = get_order_by_track(order_response.json()["track"])
    assert response.status_code == 200


def test_order_by_track():
    positive_assert()
