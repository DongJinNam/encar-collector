import pytest
import pandas as pd
import encar_crawler
import constants
import time

def test_chevrolet_crawler():
    car_count = encar_crawler.get_car_count(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                                 constants.CHEVROLET_COOL_SEAT_FILTER)
    assert car_count > 0
    print("쉐보레(대우) : " + str(car_count))

    pages = int(car_count / constants.ENCAR_MAX_LIMIT) + 1
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.CHEVROLET_COOL_SEAT_FILTER,
                                "ModifiedDate", constants.ENCAR_MAX_LIMIT, pages)
    assert len(car_list) > 0
    print("쉐보레(대우) : " + str(len(car_list)))

    unused_car_list = encar_crawler.get_used_car_alone(car_list)
    assert len(unused_car_list) > 0

    df = pd.DataFrame(unused_car_list)
    df.to_excel('쉐보레(대우)_' + str(time.strftime("%y%m%d")) + '.xlsx')
