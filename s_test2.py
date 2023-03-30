import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

wb = openpyxl.Workbook()
ws = wb.active

def main():
    ws.append(["제품명", "순위", "가격"])
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://danawa.com/")
    search_tag = driver.find_element(By.CLASS_NAME, "search__input")
    search_tag.send_keys("CPU")
    search_tag.send_keys(Keys.ENTER)


    count = 1
    PageNo = 2
    for i in range(count, PageNo):
        driver.execute_script("movePage("+str(i)+")")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_layer")
        for item in itemList:
            if item.get_attribute("id") != "":
                name = item.find_element(By.CLASS_NAME, "prod_name").text
                priceList = item.find_element(By.CLASS_NAME, "prod_pricelist")
                for price in priceList.find_elements(By.TAG_NAME, "li"):
                    priceResult = price.find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a")
                    rank = price.find_element(By.CLASS_NAME, "over_preview").text
                    print(name + " / " + rank + " / " + priceResult.text)
                    ws.append([name, rank, priceResult.text])
                # priceOne = priceList.find_element(By.CLASS_NAME, "rank_one").find_element(By.TAG_NAME, "a").text
                # print(name + " / " + priceOne)
    wb.save("save.xlsx")



if __name__ == '__main__':
    main()
