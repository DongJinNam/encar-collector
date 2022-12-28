import pytest
import pandas as pd
import encar_crawler
import constants
import time

def test_white_k7_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.K7_WHITE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("흰색k7(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.K7_WHITE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("흰색k7(통풍시트)_1인신조 : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('흰색k7(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_white_k5_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.K5_WHITE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("흰색k5(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.K5_WHITE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("흰색k5(통풍시트)_1인신조 : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('흰색k5(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_k3_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.K3_COOL_SEAT_FILTER)
    assert car_count > 0
    print("k3(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.K3_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("k3(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('k3(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_white_seltos_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SELTOS_WHITE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("흰색셀토스(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SELTOS_WHITE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("흰색셀토스(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('흰색셀토스(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_white_sportage_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SPORTAGE_WHITE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("흰색스포티지(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SPORTAGE_WHITE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("흰색스포티지(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('흰색스포티지(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_sorento_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SORENTO_COOL_SEAT_FILTER)
    assert car_count > 0
    print("쏘렌토(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SORENTO_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("쏘렌토(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('쏘렌토(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_niro_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.NIRO_COOL_SEAT_FILTER)
    assert car_count > 0
    print("니로(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.NIRO_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("니로(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('니로(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_ray_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.RAY_FILTER)
    assert car_count > 0
    print("레이 : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.RAY_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("레이 : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('레이_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_morning_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.MORNING_FILTER)
    assert car_count > 0
    print("모닝 : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.MORNING_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("모닝 : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('모닝_' + str(time.strftime("%y%m%d")) + '.xlsx')