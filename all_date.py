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
import csv

#
def todays_date():
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = str(dt_now.month).zfill(2)
    day = str(dt_now.day).zfill(2)
    today_date = f"{year}{month}{day}"
    return today_date
    pass


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options
    pass


driver = webdriver.Chrome(options=chromedriver_options())

# driver = webdriver.Chrome()

for race_place in range(1, 25):
    time.sleep(3)
    driver.get(f"https://kyoteibiyori.com/index.php?hiduke={todays_date()}")
    driver.implicitly_wait(5)
    x = "中止"
    y = "出走なし"
    race_place_text = driver.find_element(By.XPATH,
                                          f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]").text
    stop_race = x in race_place_text
    none_race = y in race_place_text

    if stop_race:
        continue
    elif none_race:
        continue
    else:
        place_name = driver.find_element(By.XPATH,
                                         f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]/a/div[1]").text
    for race_number in range(1, 13):
        race_info = []
        race_info.append(place_name)
        time.sleep(2)
        driver.get(f"https://kyoteibiyori.com/race_shusso.php?"
                   f"place_no=2&race_no={race_number}&hiduke={todays_date()}&slider=1")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/section/div[5]/div[1]/div/ul/li[2]").click()
        driver.implicitly_wait(3)
        first_win_rate = driver.find_element(By.XPATH,
                                             "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text
        race_info.append(f"{race_number}R")
        race_info.append(first_win_rate)
        for first_win_rate_player in range(1, 7):
            first_win_rate_each = driver.find_element(By.XPATH,
                                                      f"/html/body/div[8]/div[1]/section/div[5]"
                                                      f"/table[1]/tbody/tr[4]/td[{first_win_rate_player + 1}]").text
            race_info.append(first_win_rate_each)
        driver.implicitly_wait(2)
        second_in_rate = driver.find_element(By.XPATH,
                                             f"/html/body/div[8]/div[1]/section/div[5]"
                                             f"/table[1]/tbody/tr[6]/td").text
        race_info.append(second_in_rate)

        for second_in_rate_player in range(1, 7):
            second_in_rate_each = driver.find_element(By.XPATH,
                                                      f"/html/body/div[8]/div[1]/section/div[5]"
                                                      f"/table[1]/tbody/tr[9]/td[{second_in_rate_player + 1}]").text
            race_info.append(second_in_rate_each)

        determination_way = driver.find_element(By.XPATH,
                                                f"/html/body/div[8]/div[1]/section/div[5]"
                                                f"/table[1]/tbody/tr[26]/td").text
        race_info.append(determination_way)
        escape_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                    f"/table[1]/tbody/tr[29]/td[1]").text
        escaped_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                     f"/table[1]/tbody/tr[29]/td[2]").text
        race_info.append(escape_rate)
        race_info.append(escaped_rate)
        driver.implicitly_wait(5)

        print(race_info)

driver.close()
