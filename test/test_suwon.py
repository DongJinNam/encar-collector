import pandas as pd
import encar_crawler
import constants
import time

def test_suwon():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.SUWON_COOLSEAT_FILTER)
    assert car_count > 0
    print("도이치오토월드(통풍시트) 전체 : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.SUWON_COOLSEAT_FILTER,
                                "CreatedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0
    print("도이치오토월드(통풍시트) 1인신조 : " + str(len(unused_car_list)))

    df = pd.DataFrame(unused_car_list)
    df.to_excel('도이치오토월드(통풍시트)_1인신조_' + str(time.strftime("%y%m%d")) + '.xlsx')