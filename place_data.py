# noinspection PyUnresolvedReferences
import os

import time
import datetime
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys

#
# def todays_date():
#     dt_now = datetime.datetime.now()
#     year = dt_now.year
#     month = str(dt_now.month).zfill(2)
#     day = str(dt_now.day).zfill(2)
#     today_date = f"{year}{month}{day}"
#     return today_date


# def chromedriver_options():
#     # オプション設定
#     options = webdriver.ChromeOptions()
#
#     options.add_argument('--headless')
#     options.add_argument("--window-size=1280,1280")
#     return options
#
#
# driver = webdriver.Chrome(options=chromedriver_options())


driver = webdriver.Chrome()


def main():
    for place_number in range(1, 25):
        time.sleep(2)
        race_info = []
        driver.get("https://kyoteibiyori.com/")
        race_place_text = driver.find_element(By.XPATH,
                                              f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{place_number}]").text
        print(race_place_text)
        x = "出走なし"
        if x in race_place_text:
            pass
            # continue
        else:
            place_name = driver.find_element(By.XPATH, f"/html/body/div[4]/div/section[1]/div[2]/ul/"
                                                       f"li[{place_number}]/a/div[1]").text
            place_name_button = driver.find_element(By.XPATH, f"/html/body/div[4]/div/section[1]/div[2]/ul/"
                                                              f"li[{place_number}]/a/div[1]")
            race_info.append(place_name)
            print(race_info)
    driver.close()
