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
    race_info = []
    driver.get(f"https://kyoteibiyori.com/index.php?hiduke={todays_date()}")
    driver.implicitly_wait(5)
    x = "中止順延"
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
        race_info.append(place_name)
        
driver.close()
