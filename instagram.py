import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import openpyxl
#import passwd

wb = openpyxl.Workbook()
ws = wb.active
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
prefs = {"profile.default_content_setting_values.geolocation":2}
options.add_experimental_option("prefs",prefs)
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
driver.set_window_size(1500, 800)
def main():
    driver.get("https://www.instagram.com/")
    time.sleep(1)
    driver.find_element(By.NAME,"username").send_keys("resten1497")
    driver.find_element(By.NAME,"password").send_keys("sa720315*")
    driver.find_element(By.CLASS_NAME,"_acap").click()
    time.sleep(3)
    wait = WebDriverWait(driver, 10)
    if driver.current_url == "https://www.instagram.com/accounts/" \
                             "onetap/?next=%2F":
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_acao')))
        driver.find_element(By.CLASS_NAME,"_acao").click()
        time.sleep(1)
    driver.find_element(By.CLASS_NAME,"_a9_1").click()
    time.sleep(3)
    driver.find_element(By.CLASS_NAME,"xh8yej3.x1iyjqo2")\
    .find_elements(By.TAG_NAME,"a")[7].click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, '_aa8k')))
    driver.find_element(By.CLASS_NAME,"_aa8k").click()
    time.sleep(1)
    for i in range(10):
        time.sleep(2)
        image = driver.find_element(By.CLASS_NAME, '_aatk')

        try:
            many = image.find_elements(By.CLASS_NAME, "_acnb")
            checkTag = image.find_element(By.CLASS_NAME, "_acaz")
            print(checkTag)
            image_tag = checkTag.find_element(By.TAG_NAME, "img")
            print(image_tag.get_attribute("src"))
            driver.find_element(By.CLASS_NAME, "_afxw").click()
            for i in range(len(many) - 2):
                a = image.find_elements(By.CLASS_NAME, "_acaz")[1].find_element(By.TAG_NAME, "img")
                print(a.get_attribute("src"))
                driver.find_element(By.CLASS_NAME, "_afxw").click()
                time.sleep(1)
        except NoSuchElementException:
            image = driver.find_element(By.CLASS_NAME,"_aagv").find_element(By.TAG_NAME,"img")
            print(image.get_attribute("src"))
        driver.find_element(By.TAG_NAME,"body").send_keys(Keys.ARROW_RIGHT)
        print("------------------------")

if __name__ == '__main__':
    main()