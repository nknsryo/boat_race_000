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
# def todays_date():
#     dt_now = datetime.datetime.now()
#     year = dt_now.year
#     month = str(dt_now.month).zfill(2)
#     day = str(dt_now.day).zfill(2)
#     today_date = f"{year}{month}{day}"
#     return today_date
#     pass


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

driver.get("https://kyoteibiyori.com/race_shusso.php?place_no=2&race_no=1&hiduke=20220206&slider=1")
time.sleep(3)
text = driver.find_element(By.XPATH,
                           "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[4]/td[2]").text

text_OK = float(text.split("%")[0])
print(text_OK)
driver.close()

data
place_name
race_number
one_3month_1win
two_3month_1win
three_3month_1win
four_3month_1win
five_3month_1win
six_3month_1win
one_3month_2win
two_3month_2win
three_3month_2win
four_3month_2win
five_3month_2win
six_3month_2win
one_6month_escape
two_6month_escaped
