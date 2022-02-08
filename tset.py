# #
# # with open("test.csv", "a", encoding='utf_8_sig') as csv_file:
# #     {test.csv}
#
# with open("test.csv", "r", encoding="utf-8_sig") as f:
#     s = f.read()
# s = s.replace("'", "")
# s = s.replace("(", "")
# s = s.replace(")", "")
#
#
# with open("test.csv", "w", encoding="utf-8_sig") as f:
#     f.write(s)
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
# noinspection PyUnresolvedReferences
import csv


def date():
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
driver.get("https://kyoteibiyori.com/race_shusso.php?place_no=1&race_no=2&hiduke=20220208&slider=1")
time.sleep(2)
# test_text = driver.find_element(By.XPATH, F"/html/body/div[8]/div[1]/section/div[3]/h2").text
# test_text = test_text.split("締切")[1]
# test_text = test_text.split("お気")[0]
# print(test_text)
# driver.close()
for player_name in range(1, 7):
    players_name = driver.find_element(By.XPATH,
                                       f"/html/body/div[8]/div[1]/section/div[3]/div[2]/table/tbody/"
                                       f"tr[3]/td[{player_name}]").text
    players_name_1 = players_name.split("\n")[0]
    players_name_2 = players_name.split("\n")[1]
    players_name = f"{players_name_1} {players_name_2}"

    print(players_name)

driver.close()
