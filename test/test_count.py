import pytest
import encar_crawler
import constants

def test_grandeur_filter():
    grandeur_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.GRANDEUR_COOL_SEAT_FILTER)
    print("grandeur count (with cool seat) : " + str(grandeur_count))
    assert grandeur_count > 0

def test_bigsize_filter():
    big_size_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.BIGSIZE_COOL_SEAT_FILTER)
    print("big_size_count (with cool seat) : " + str(big_size_count))
    assert big_size_count > 0

def test_suv_filter():
    suv_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SUV_COOL_SEAT_FILTER)
    print("suv_count (with cool seat) : " + str(suv_count))
    assert suv_count > 0