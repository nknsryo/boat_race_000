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


def todays_date():
    dt_now = datetime.datetime.now()
    year = dt_now.year
    month = str(dt_now.month).zfill(2)
    day = str(dt_now.day).zfill(2)
    today_date = f"{year}{month}{day}"
    return today_date


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
