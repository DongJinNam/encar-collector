import pytest
import pandas as pd
import encar_crawler
import constants
import time

def test_grandeur_rent_crawler():
    grandeur_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.GRANDEUR_COOL_SEAT_FILTER)
    assert grandeur_count > 0
    print("그랜저(선루프+통풍시트) : " + str(grandeur_count))

    pages = int(grandeur_count / constants.ENCAR_MAX_LIMIT) + 1
    grandeur_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.GRANDEUR_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(grandeur_list) > 0
    print("그랜저(선루프+통풍시트) : " + str(len(grandeur_list)))

    unused_grandeur_list = encar_crawler.get_used_car_alone(grandeur_list, True)
    assert len(unused_grandeur_list) > 0

    df = pd.DataFrame(unused_grandeur_list)
    df.to_excel('그랜저(선루프+통풍시트)_렌트_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_grandeur_crawler():
    grandeur_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.GRANDEUR_COOL_SEAT_FILTER)
    assert grandeur_count > 0
    print("그랜저(선루프+통풍시트) : " + str(grandeur_count))

    pages = int(grandeur_count / constants.ENCAR_MAX_LIMIT) + 1
    grandeur_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.GRANDEUR_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(grandeur_list) > 0
    print("그랜저(선루프+통풍시트) : " + str(len(grandeur_list)))

    unused_grandeur_list = encar_crawler.get_used_car_alone(grandeur_list)
    assert len(unused_grandeur_list) > 0

    df = pd.DataFrame(unused_grandeur_list)
    df.to_excel('그랜저(선루프+통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_white_grandeur_crawler():
    grandeur_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.GRANDEUR_WHITE_COOL_SEAT_FILTER)
    assert grandeur_count > 0
    print("흰색그랜저(선루프+통풍시트) : " + str(grandeur_count))

    pages = int(grandeur_count / constants.ENCAR_MAX_LIMIT) + 1
    grandeur_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.GRANDEUR_WHITE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(grandeur_list) > 0
    print("흰색그랜저(선루프+통풍시트) : " + str(len(grandeur_list)))

    unused_grandeur_list = encar_crawler.get_used_car_alone(grandeur_list)
    assert len(unused_grandeur_list) > 0

    df = pd.DataFrame(unused_grandeur_list)
    df.to_excel('흰색그랜저(선루프+통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')

def test_sonata_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SONATA_COOL_SEAT_FILTER)
    assert car_count > 0
    print("쏘나타(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SONATA_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("쏘나타(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('쏘나타(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_avante_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.AVANTE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("아반떼(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.AVANTE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("아반떼(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('아반떼(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_kona_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.KONA_COOL_SEAT_FILTER)
    assert car_count > 0
    print("코나(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.KONA_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("코나(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('코나(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_tucson_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.TUCSON_COOL_SEAT_FILTER)
    assert car_count > 0
    print("투싼(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.TUCSON_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("투싼(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('투싼(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


def test_santafe_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SANTAFE_COOL_SEAT_FILTER)
    assert car_count > 0
    print("싼타페(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SANTAFE_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("싼타페(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('싼타페(통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')