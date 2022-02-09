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

# noinspection PyUnresolvedReferences
import os

# noinspection PyUnresolvedReferences
import psycopg2 as psycopg2
from dotenv import load_dotenv

from db import init_db, add_data


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


# driver = webdriver.Chrome(options=chromedriver_options())

driver = webdriver.Chrome()

init_db()

# 24レース場からデータを取得してくる
for race_place in range(1, 25):
    time.sleep(3)
    driver.get(f"https://kyoteibiyori.com/index.php?hiduke={date()}")
    driver.implicitly_wait(20)
    x = "中止"
    y = "出走なし"
    race_place_text = driver.find_element(By.XPATH,
                                          f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]").text
    # "中止"という文字が入っているかどうか
    stop_race = x in race_place_text
    # "出走なし"という文字が入っているかどうか
    none_race = y in race_place_text
    if stop_race:
        continue
    elif none_race:
        continue
    else:
        place_name = driver.find_element(By.XPATH,
                                         f"/html/body/div[4]/div/section[1]/div[2]/ul/li[{race_place}]/a/div[1]").text
        # 1~12レースの情報を回す。
    for race_number in range(1, 13):
        race_info = []
        race_info.append(date())
        race_info.append(place_name)
        time.sleep(2)
        driver.get(f"https://kyoteibiyori.com/race_shusso.php?"
                   f"place_no={race_place}&race_no={race_number}&hiduke={date()}&slider=1")
        driver.implicitly_wait(5)
        driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/section/div[5]/div[1]/div/ul/li[2]").click()
        driver.implicitly_wait(3)
        first_win_rate = driver.find_element(By.XPATH,
                                             "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text
        race_info.append(f"{race_number}R")
        race_info.append(first_win_rate)
        # 1~6号艇の1着率
        for first_win_rate_player in range(1, 7):
            first_win_rate_each = driver.find_element(By.XPATH,
                                                      f"/html/body/div[8]/div[1]/section/div[5]"
                                                      f"/table[1]/tbody/tr[4]/td[{first_win_rate_player + 1}]").text
            first_win_rate_each = float(first_win_rate_each.split("%")[0])
            race_info.append(first_win_rate_each)
        driver.implicitly_wait(2)
        second_in_rate = driver.find_element(By.XPATH,
                                             f"/html/body/div[8]/div[1]/section/div[5]"
                                             f"/table[1]/tbody/tr[6]/td").text
        race_info.append(second_in_rate)
        # 1~6号艇の2連対率
        for second_in_rate_player in range(1, 7):
            second_in_rate_each = driver.find_element(By.XPATH,
                                                      f"/html/body/div[8]/div[1]/section/div[5]"
                                                      f"/table[1]/tbody/tr[9]/td[{second_in_rate_player + 1}]").text
            second_in_rate_each = float(second_in_rate_each.split("%")[0])
            race_info.append(second_in_rate_each)
        third_in_rate = driver.find_element(By.XPATH,
                                            f"/html/body/div[8]/div[1]/section/div[5]/"
                                            f"table[1]/tbody/tr[11]/td").text
        race_info.append(third_in_rate)
        for third_in_rate_player in range(1, 7):
            three_month_3win = driver.find_element(By.XPATH,
                                                   f"/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/"
                                                   f"tr[14]/td[{third_in_rate_player + 1}]").text
            # 情報が"-"の時は"0"として表示する
            if three_month_3win == "-":
                three_month_3win = "0.0%1"
            else:
                pass
            # %より前に記載してある数字の部分のみを表示してリストに追加
            three_month_3win = three_month_3win.split("%")[0]
            three_month_3win = int(three_month_3win.split(".")[0])
            race_info.append(three_month_3win)

        # 逃げ率text
        determination_way = driver.find_element(By.XPATH,
                                                f"/html/body/div[8]/div[1]/section/div[5]"
                                                f"/table[1]/tbody/tr[26]/td").text
        race_info.append(determination_way)
        # 逃げ率
        escape_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                    f"/table[1]/tbody/tr[29]/td[1]").text
        # 逃し率
        escaped_rate = driver.find_element(By.XPATH, f"/html/body/div[8]/div[1]/section/div[5]"
                                                     f"/table[1]/tbody/tr[29]/td[2]").text
        escape_rate = float(escape_rate.split("%")[0])
        escaped_rate = float(escaped_rate.split("%")[0])
        race_info.append(escape_rate)
        race_info.append(escaped_rate)
        driver.implicitly_wait(5)

        race_info = tuple(race_info)
        # csv_02(1レース分)に書き込み
        with open("test_02.csv", 'r+') as f:
            f.truncate(0)
        with open("test_02.csv", "a", encoding='utf_8_sig') as csv_file:
            print(race_info, file=csv_file)
        with open("test_02.csv", "r", encoding="utf-8_sig") as f:
            s = f.read()
        s = s.replace("'", "")
        s = s.replace("(", "")
        s = s.replace(")", "")
        s = s.replace("[", "")
        s = s.replace("]", "")
        # csv(累計レース)書き込み
        with open("test_02.csv", "w", encoding="utf-8_sig") as f:
            f.write(s)

        add_data()

        with open("test.csv", "a", encoding='utf_8_sig') as csv_file:
            print(race_info, file=csv_file)
        print(race_info)
    driver.close()
# csvファイルの加工(",","()","[]")削除、更新
with open("test.csv", "r", encoding="utf-8_sig") as f:
    s = f.read()
s = s.replace("'", "")
s = s.replace("(", "")
s = s.replace(")", "")
s = s.replace("[", "")
s = s.replace("]", "")
with open("test.csv", "w", encoding="utf-8_sig") as f:
    f.write(s)

# csvデータをデータベースに反映させる
