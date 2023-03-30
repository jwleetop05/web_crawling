import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import openpyxl


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


def main():

    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("https://danawa.com/")
    search_tag = driver.find_element(By.CLASS_NAME, "search__input")
    search_tag.send_keys("RTX 3080")
    search_tag.send_keys(Keys.ENTER)


    count = 1
    PageNo = 3
    for i in range(count, PageNo):
        driver.execute_script("getPage("+str(i)+")")
        time.sleep(1)
        itemList = driver.find_elements(By.CLASS_NAME, "prod_item")
        for item in itemList:
            if item.get_attribute("id") != "":
                name = item.find_element(By.CLASS_NAME, "prod_name").text
                price = item.find_element(By.CLASS_NAME, "price_sect").find_element(By.TAG_NAME, "a").text
                print(name, "/", price)



if __name__ == '__main__':
    main()
