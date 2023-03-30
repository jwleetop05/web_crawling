import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.geolocation":2}
options.add_experimental_option("prefs",prefs)
options.add_argument("headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://danawa.com/")
search_tag = driver.find_element(By.CLASS_NAME, "search__input")
page_count = 1

SEARCH = {
    "cpu": "5600",
    "ram": "삼성 ddr4 16gb",
    "main-board": "b550",
    "power": "750w",
    "gpu": "rtx3060",
    "ssd": "ssd",
}
FILE_LOCATION = "./DATA"


def main():
    result = []
    for item in SEARCH.items():
        driver.get("https://danawa.com/")
        search_tag = driver.find_element(By.CLASS_NAME, "search__input")
        search_tag.send_keys(item[1])
        search_tag.send_keys(Keys.ENTER)
        print(driver.current_url)
        time.sleep(2)
        if "list" in driver.current_url:
            # list_search
            result = list_search_top3(item[0])
        elif "dsearch.php" in driver.current_url:
            # dsearch_search
            result = dsearch_search_top3(item[0])

    df = pd.DataFrame(data=result, )
    df.to_csv(FILE_LOCATION + "Computer.csv")


def dsearch_search():
    for count in range(1, page_count + 1):
        itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
        for item in range(3):
            if item.get_attribute("id") != "":
                name = item.find_element(By.CLASS_NAME, "prod_name")
                price = item.find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a").text
                name.click()
                time.sleep(1)
                spec = get_spec()
                print(name.text, "/", price, "/", spec)
        driver.execute_script("getPage(" + str(count) + ")")
        time.sleep(0.5)


def dsearch_search_top3(key):
    result = []
    itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
    for idx in range(3):
        if itemList[idx].get_attribute("id") != "":
            name = itemList[idx].find_element(By.CLASS_NAME, "prod_name").find_element(By.TAG_NAME, "a")
            price = itemList[idx].find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a").text
            name.click()
            time.sleep(1)
            spec = get_spec()
            result.append([key, name.text, price, spec])
    return result



def list_search():
    for count in range(1, page_count + 1):
        itemList = driver.find_elements(By.CLASS_NAME, "prod_layer")
        for item in itemList:
            if item.get_attribute("id") != "":
                name = item.find_element(By.CLASS_NAME, "prod_name")
                priceList = item.find_element(By.CLASS_NAME, "prod_pricelist")
                # priceOne = priceList.find_element(By.CLASS_NAME, "rank_one").find_element(By.TAG_NAME, "a").text
                # print(name + " / " + priceOne)
                name.click()
                time.sleep(0.5)
                spec = get_spec()
                for price in priceList.find_elements(By.TAG_NAME, "li"):
                    priceResult = price.find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a")
                    print(name.text + " / " + priceResult.text + " / " + spec)
        driver.execute_script("movePage(" + str(count) + ")")
        time.sleep(0.5)


def list_search_top3(key):
    result = []
    itemList = driver.find_elements(By.CLASS_NAME, "prod_layer")
    for idx in range(3):
        if itemList[idx].get_attribute("id") != "":
            name = itemList[idx].find_element(By.CLASS_NAME, "prod_name")
            priceList = itemList[idx].find_element(By.CLASS_NAME, "prod_pricelist")
            # priceOne = priceList.find_element(By.CLASS_NAME, "rank_one").find_element(By.TAG_NAME, "a").text
            # print(name + " / " + priceOne)
            name.click()
            time.sleep(0.5)
            spec = get_spec()
            for price in priceList.find_elements(By.TAG_NAME, "li"):
                priceResult = price.find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a")
            result.append([key, name.text, priceResult, spec])
    return result

def get_spec():
    driver.switch_to.window(driver.window_handles[-1])
    spec = driver.find_element(By.CLASS_NAME, "spec_list").text
    driver.close()
    time.sleep(0.5)
    driver.switch_to.window(driver.window_handles[0])
    return spec


if __name__ == '__main__':
    main()
