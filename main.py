# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import socket
import requests
import urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

import constants
import encar_crawler

def crawling_test(url):
    try:
        page = requests.get(url)
        soup = bs(page.text, "html.parser")
        elements = soup.select('div.esg-entry-content a.eg-grant-element-0')
        titles = []
        links = []
        for index, element in enumerate(elements, 1):
            titles.append(element.text)
            links.append(element.attrs['href'])
        print(titles)
        print(links)
    except urllib.error.HTTPError as e:
        print("Error code : ", e.code)
        exit()
    except urllib.error.URLError as e:
        print("Error code : ", e.code)
        exit()
    except (RuntimeError, TypeError, NameError):
        print("exception happened")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')
    # todo. 차량 목록 가져온 후 1인 신조차량 구분하기
    car_list = encar_crawler.get_car_list(constants.API_ENCAR_URL + constants.SEARCH_CAR_LIST_URL_PREMIUM,
                                constants.GRANDEUR_COOL_SEAT_FILTER,
                                "ModifiedDate", 400)
    print(len(car_list))
    # unused_car_list = encar_crawler.get_used_car_alone(car_list)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
