import json
import requests
import urllib.error
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

import constants
from carhistory import CarHistory

def get_car_count(url, filter):
    # set params
    params = {}
    params['count'] = True
    params['q'] = filter
    count = 0
    try:
        response = requests.get(url, params)
        response_json = json.loads(response.text)
        count = response_json["Count"]
    except urllib.error.HTTPError as e:
        print("Error code : ", e.code)
        exit()
    except urllib.error.URLError as e:
        print("Error code : ", e.code)
        exit()
    except (RuntimeError, TypeError, NameError) as e:
        print("Error code : ", e)
        exit()

    return count

def get_car_list(url, filter, sort_key, limit, pages):
    # set params
    params = {}
    params['count'] = True
    params['q'] = filter
    car_list = []
    unused_car_list = []
    try:
        response = requests.get(url, params)
        response_json = json.loads(response.text)
        # pages = 1 if int(response_json["Count"] / limit) == 0 else int(response_json["Count"] / limit)
        # search all
        for page in range(0, pages):
            start_time = time.time()
            params['sr'] = "|" + sort_key + "|" + str(page * limit) + "|" + str(limit)
            detail_response = requests.get(url, params)
            detail_response_json = json.loads(detail_response.text)
            search_results = detail_response_json["SearchResults"]
            for result in search_results:
                car_list.append(result)
            # unused_car_list.append(get_used_car_alone(car_list))
    except urllib.error.HTTPError as e:
        print("Error code : ", e.code)
        exit()
    except urllib.error.URLError as e:
        print("Error code : ", e.code)
        exit()
    except (RuntimeError, TypeError, NameError) as e:
        print("Error code : ", e)
        exit()

    return car_list


def get_used_car_alone(car_list, is_rent = False):
    # todo car_list ????????? ?????? ??????????????? ???????????????, ???????????? ?????? ???????????? ?????? 1??? ????????? ????????? ??????.
    unused_car_list = []
    for car in car_list:
        if not "Photo" in car.keys():
            continue
        second_car_id = car["Photo"].split("/")[-1][0:8]
        new_url = constants.INSURANCE_URL + second_car_id
        web_page = requests.get(new_url)
        soup = bs(web_page.text, "html.parser")
        smlist = soup.find("div","smlist")
        features = []
        if smlist is not None:
            for td in smlist.find_all("td"):
                if td.text.strip():
                    features.append(td.text.strip())
            car_history = CarHistory(car["Id"], second_car_id, features[0], features[1],
                                     features[2], features[3], features[4], features[5])
            if is_rent is False:
                # 1??? ?????? + ????????? ?????? ??????
                if car_history.car_used == False and car_history.car_num_changed <= 0 and car_history.car_owner_changed <= 1 \
                        and "?????????" not in car_history.my_car_damage and "?????????" not in car_history.other_car_damage:
                    car["Detail"] = constants.CAR_DETAIL_URL + car["Id"]
                    unused_car_list.append(car)
            else:
                if car_history.car_used == True and car_history.car_num_changed <= 1 and car_history.car_owner_changed <= 1 \
                        and "?????????" not in car_history.my_car_damage and "?????????" not in car_history.other_car_damage:
                    car["Detail"] = constants.CAR_DETAIL_URL + car["Id"]
                    unused_car_list.append(car)

    return unused_car_list
