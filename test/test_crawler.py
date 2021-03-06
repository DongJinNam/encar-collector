import pytest
import pandas as pd
import encar_crawler
import constants
import time

# 10만 키로 ~ 15만 키로 선루프, 통풍시트 1인 신조 차량 조회
def test_very_long_distaince_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.VERY_LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER)
    assert car_count > 0
    print("12만~30만 키로 차량 수(선루프+통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.VERY_LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("12만~30만 키로 차량 수(선루프+통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('12만-30만 용도이력 없음(선루프, 통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


# 10만 키로 ~ 15만 키로 선루프, 통풍시트 1인 신조 차량 조회
def test_long_distaince_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER)
    assert car_count > 0
    print("10만~15만 키로 차량 수(선루프+통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.LONG_DISTANCE_SUNROOF_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("10만~15만 키로 차량 수(선루프+통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('10만-15만 용도이력 없음(선루프, 통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')


# 4만 키로 ~ 6만 키로 선루프, 통풍시트 1인 신조 차량 조회
def test_short_distaince_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.SHORT_DISTANCE_SUNROOF_COOLSEAT_FILTER)
    assert car_count > 0
    print("4만~6만 키로 차량 수(선루프+통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SHORT_DISTANCE_SUNROOF_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("4만~6만 키로 차량 수(선루프+통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('4만-6만 용도이력 없음(선루프, 통풍시트)_' + str(time.strftime("%y%m%d")) + '.xlsx')

# LPG 차량 조회
def test_lpg_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.LPG_COOLSEAT_FILTER)
    assert car_count > 0
    print("LPG차량(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.LPG_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("LPG차량(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('LPG차량(통풍시트)_' + str(time.strftime("%y%m%d")) +'.xlsx')


# 하이브리드 차량 조회
def test_hybrid_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.HYBRID_COOLSEAT_FILTER)
    assert car_count > 0
    print("하이브리드(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.HYBRID_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("하이브리드(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('하이브리드(통풍시트)_' + str(time.strftime("%y%m%d")) +'.xlsx')


# SUV 차량 조회 (10만 이상)
def test_suv_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.SUV_COOL_SEAT_FILTER)
    assert car_count > 0
    print("SUV차량(통풍시트) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SUV_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("SUV차량(통풍시트) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('SUV차량(통풍시트)_' + str(time.strftime("%y%m%d")) +'.xlsx')


# 경차, 준중형 조회 (주행거리 10만 이상)
def test_small_size_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.SMALL_SIZE_FILTER)
    assert car_count > 0
    print("경차, 준중형(10만이상) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SMALL_SIZE_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("경차, 준중형(10만이상) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('경차, 준중형(10만이상)_' + str(time.strftime("%y%m%d")) +'.xlsx')

# 경차, 준중형 조회 (주행거리 4만 ~ 6만미만)
def test_small_size_latest_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.SMALL_SIZE_LATEST_FILTER)
    assert car_count > 0
    print("경차, 준중형(4만~6만미만) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SMALL_SIZE_LATEST_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("경차, 준중형(4만~6만미만) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('경차, 준중형(4만~6만미만)_' + str(time.strftime("%y%m%d")) +'.xlsx')

# 경차만 조회
def test_small_size_only_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.SMALL_SIZE_ONLY_FILTER)
    assert car_count > 0
    print("경차 : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SMALL_SIZE_ONLY_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("경차 : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('경차_' + str(time.strftime("%y%m%d")) +'.xlsx')

def test_homeservice():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.HOMESERVICE_COOLSEAT_FILTER)
    assert car_count > 0
    print("엔카홈서비스(통풍시트+20만미만) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.HOMESERVICE_COOLSEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("엔카홈서비스(통풍시트+20만미만) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('엔카홈서비스(통풍시트+20만미만)_' + str(time.strftime("%y%m%d")) +'.xlsx')

# 수입차
def test_foreign_homeservice():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.FOREIGN_HOMESERVICE_FILTER)
    assert car_count > 0
    print("수입차(15만미만) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.FOREIGN_HOMESERVICE_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("수입차(15만미만) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('수입차(15만미만)_' + str(time.strftime("%y%m%d")) +'.xlsx')


def test_homeservice_long_rentcar():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.RENT_CAR_SUNROOF_FILTER)
    assert car_count > 0
    print("엔카홈서비스(렌트카+20만미만) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.RENT_CAR_SUNROOF_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("엔카홈서비스(렌트카+20만미만) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list, True)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('엔카홈서비스(렌트카+20만미만)_' + str(time.strftime("%y%m%d")) +'.xlsx')


def test_white_homeservice():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                            constants.WHITE_CAR_HOMESERVICE_FILTER)
    assert car_count > 0
    print("엔카홈서비스(흰색+20만미만) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.WHITE_CAR_HOMESERVICE_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("엔카홈서비스(흰색+20만미만) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('엔카홈서비스(흰색+20만미만)_' + str(time.strftime("%y%m%d")) +'.xlsx')