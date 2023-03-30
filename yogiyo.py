import time
import openpyxl
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
prefs = {"profile.default_content_setting_values.geolocation": 2}
options.add_experimental_option("prefs", prefs)
wb = openpyxl.Workbook()
ws = wb.active


def main():
    ws.append(["식당명", "별점", "배송시간", "메뉴명", "메뉴이름"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.set_window_size(1500, 800)
    driver.get("https://www.yogiyo.co.kr/mobile/#/")
    inputTag = driver.find_element(By.NAME, "address_input")
    inputTag.send_keys("녹사평역")
    inputTag.send_keys(Keys.ENTER)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-6")))
    selector = Select(driver.find_element(By.CLASS_NAME, "list-option-inner").find_element(By.TAG_NAME, "select"))

    selector.select_by_index(2)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-6")))
    category = driver.find_element(By.ID, "category").find_elements(By.TAG_NAME, "li")
    category[2].click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "col-sm-6")))

    for index in range(10):
        time.sleep(1)
        storeList = driver.find_elements(By.CLASS_NAME, 'col-sm-6')
        storeList[index].click()
        time.sleep(1)
        name = driver.find_element(By.CLASS_NAME, "restaurant-name").text
        star = driver.find_element(By.CLASS_NAME, "star-point").text.replace("★", "")
        delivery_time = driver.find_element(By.CLASS_NAME, "delivery-time-tooltip").text
        time.sleep(1)
        menuList = driver.find_element(By.CLASS_NAME, "photo-menu-container") \
            .find_element(By.CLASS_NAME, "photo-slide") \
            .find_elements(By.CLASS_NAME, "photo-menu")

        for menu in menuList:
            menu_name = menu.find_element(By.CLASS_NAME, "menu-name").text
            menu_price = menu.find_element(By.CLASS_NAME, "menu-price").find_element(By.TAG_NAME, "span").text
            ws.append([name,star,delivery_time,menu_name,menu_price])
        driver.back()
    wb.save("yogiyo.xlsx")


if __name__ == '__main__':
    main()
