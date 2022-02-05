# noinspection PyUnresolvedReferences
import os

import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.by import By
# noinspection PyUnresolvedReferences
from selenium.webdriver.common.keys import Keys


def chromedriver_options():
    # オプション設定
    options = webdriver.ChromeOptions()

    options.add_argument('--headless')
    options.add_argument("--window-size=1280,1280")
    return options


# driver = webdriver.Chrome()
driver = webdriver.Chrome(options=chromedriver_options())


def main():
    driver.get("https://kyoteibiyori.com/race_shusso.php?place_no=3&race_no=1&hiduke=20220204&slider=1")
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, "/html/body/div[8]/div[1]/section/div[5]/div[1]/div/ul/li[2]").click()
    driver.implicitly_wait(5)
    race_info = []
    first_win_rate = driver.find_element(By.XPATH,
                                         "/html/body/div[8]/div[1]/section/div[5]/table[1]/tbody/tr[1]/td").text
    race_info.append(first_win_rate)
    for first_win_rate_player in range(1, 7):
        first_win_rate_each = driver.find_element(By.XPATH,
                                                  f"/html/body/div[8]/div[1]/section/div[5]"
                                                  f"/table[1]/tbody/tr[4]/td[{first_win_rate_player + 1}]").text
        race_info.append(first_win_rate_each)

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


if __name__ == '__main__':
    main()
